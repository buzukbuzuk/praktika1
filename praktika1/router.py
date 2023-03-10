from studentApp.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student', StudentViewSet)
