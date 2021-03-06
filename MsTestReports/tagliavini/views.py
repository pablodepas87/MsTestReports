from .models import TagliaviniReport
from django.views import generic
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.db.models import Q
from .utils import render_html_to_pdf
from .serializers import TagliaviniReportSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


class ReportsListView(generic.ListView):
    template_name = 'tagliavini/reportsList.html'
    context_object_name = 'report_list'
    paginate_by = 75
    def get_queryset(self):
        query_filter =self.request.GET.get("query",None)
        if query_filter is not None:
            return TagliaviniReport.objects.filter(Q(board_serial__contains=query_filter)|
                                                   Q(tester_name__contains=query_filter)|
                                                   Q(tester_surname__contains=query_filter)).order_by('dt_start_test')

        return TagliaviniReport.objects.order_by('-dt_start_test')


class PDFReportView(generic.DetailView):
    model = TagliaviniReport
    template_name = 'tagliavini/pdf_report.html'

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except TagliaviniReport.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        template = get_template('tagliavini/pdf_report.html')
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
            'usb': report.usb,
            'serial_work': report.serial_work,
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
    queryset = TagliaviniReport.objects.all()
    serializer_class = TagliaviniReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SingleReportApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagliaviniReport.objects.all()
    serializer_class = TagliaviniReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]