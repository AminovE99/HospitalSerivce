from rest_framework.routers import SimpleRouter

from patient.views import PatientViewSet

router = SimpleRouter()
router.register(r'patient', PatientViewSet, basename='patient')

urlpatterns = router.urls
