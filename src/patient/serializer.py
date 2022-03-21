from rest_framework import serializers

from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    diagnoses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Patient
        fields = ('id', 'date_of_birth', 'created_at', 'diagnoses')
