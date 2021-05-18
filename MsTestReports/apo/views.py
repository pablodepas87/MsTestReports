from .models import ApoReport
from django.views import generic
from .utils import render_html_to_pdf
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.db.models import Q
from .serializers import ApoReportSerializer, UserSerializer
from rest_framework import permissions , generics
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class ReportListView(generic.ListView):
    template_name = 'apo/reportsList.html'
    paginate_by = 25

    def get_queryset(self):
        query_filter =self.request.GET.get("query", None)
        if query_filter is not None:
            return ApoReport.objects.filter(Q(board_serial__contains=query_filter) |
                                            Q(tester_name__contains=query_filter) |
                                            Q(tester_surname__contains=query_filter)).order_by('-dt_start_test')

        return ApoReport.objects.order_by('-dt_start_test')


class PDFReportView(generic.DetailView):
    model = ApoReport
    template_name = 'apo/pdf_report.html'

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except ApoReport.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        template = get_template('apo/pdf_report.html')
        report = self.get_object(pk)
        data = {
            'board_serial': report.board_serial,
            'tester_name': report.tester_name,
            'tester_surname': report.tester_surname,
            'dt_start_test': report.dt_start_test,
            'dt_end_test': report.dt_end_test,
            'touchscreen': report.touchscreen,
            'brightness': report.brightness,
            'buzzer': report.buzzer,
            'fan': report.fan,
            'usb': report.usb,
            'rotary': report.rotary,
            'serial_work': report.serial_work,
            'certs_downloaded': report.certs_downloaded,
            'certsId': report.certs_id,
            'sw_version': report.sw_version
        }
        html = template.render(data)
        pdf = render_html_to_pdf(self.template_name, data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "%s_report.pdf" %report.board_serial
            content = "inline; filename=%s" %filename
            response['Content-Disposition'] = content
            return response
        return Http404


class ReportListApiView(generics.ListCreateAPIView):
    queryset = ApoReport.objects.all()
    serializer_class = ApoReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleReportApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApoReport.objects.all()
    serializer_class = ApoReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

