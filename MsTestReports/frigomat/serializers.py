from rest_framework import serializers
from .models import FrigomatReport
from django.contrib.auth.models import User


class FrigomatReportSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.surname')

    class Meta:
        model = FrigomatReport
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
            'dt_end_test',
            'sw_version',
            'owner',
        ]


class UserSerializer(serializers.Serializer):
    model = User
    class Meta:
        fields = [
            'id',
            'username',
            'report'
        ]

