from django.db import models

# Create your models here.

class ApoReport(models.Model):
    tester_name = models.CharField(max_length=30)
    tester_surname = models.CharField(max_length=30)
    board_serial = models.CharField(max_length=6)
    dt_start_test = models.DateTimeField('start_test')
    touchscreen = models.BooleanField()
    brightness = models.BooleanField()
    buzzer = models.BooleanField()
    usb = models.BooleanField()
    serial_work = models.BooleanField()
    fan = models.BooleanField()
    rotary = models.BooleanField()
    certs_downloaded = models.BooleanField()
    certs_id = models.CharField(max_length=250)
    dt_end_test = models.DateTimeField('end_test')
    sw_version = models.CharField(max_length=10)
    owner = models.ForeignKey('auth.User', related_name='report', on_delete=models.CASCADE, default= 1)

    def __str__(self):
        return "Board: "+self.board_serial+" Tester: "+self.tester_name+" "+self.tester_surname