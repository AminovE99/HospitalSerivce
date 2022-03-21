from rest_framework import serializers

from django.conf import settings
from patient.models import Patient, CustomToken


class PatientSerializer(serializers.ModelSerializer):
    diagnoses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Patient
        fields = ('id', 'date_of_birth', 'created_at', 'diagnoses')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomToken
        fields = ("auth_token", 'is_doctor')

    def validate(self, attrs):
        if not attrs.get('is_doctor'):
            raise serializers.ValidationError('Is doctor must be true')
