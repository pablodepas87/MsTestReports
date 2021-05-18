from rest_framework import serializers
from .models import ApoReport
from django.contrib.auth.models import User


class ApoReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ApoReport
        fields = [
            'id',
            'tester_name',
            'tester_surname',
            'board_serial',
            'dt_start_test',
            'touchscreen',
            'brightness',
            'buzzer',
            'usb',
            'serial_work',
            'fan',
            'rotary',
            'certs_downloaded',
            'certs_id',
            'dt_end_test',
            'sw_version',
            'owner',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'report',
        ]