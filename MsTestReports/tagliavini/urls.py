from django.urls import path
from . import views

app_name = 'tagliavini'

urlpatterns = [
    path('', views.ReportsListView.as_view(), name='reportList'),
    path('pdfreport/<int:pk>', views.PDFReportView.as_view(), name='pdfreport'),
    path('api/reportlist', views.ReportListApiView.as_view(), name='apiReportList'),
    path('api/reportlist/<int:pk>', views.SingleReportApiView.as_view(), name='apiSingleReport')
]