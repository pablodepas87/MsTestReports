from django.urls import path
from . import views

app_name = 'apo'

urlpatterns = [
    path('', views.ReportListView.as_view(), name='reportList'),
    path('PDFReport/<int:pk>', views.PDFReportView.as_view(), name='pdf_report'),
    path('api/reportlist', views.ReportListApiView.as_view(), name ='apiReportList'),
    path('api/reportlist/<int:pk>', views.SingleReportApiView.as_view(), name='apiSingleReport')
]
