from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from patient.models import Patient
from patient.serializer import PatientSerializer


class PatientViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
