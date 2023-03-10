from rest_framework import serializers
from studentApp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'surname', 'email', 'phoneNum', 'gpa')
