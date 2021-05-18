from rest_framework import serializers
from .models import TagliaviniReport
from django.contrib.auth.models import User


class TagliaviniReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TagliaviniReport
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'report'
        ]
