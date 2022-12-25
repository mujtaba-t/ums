from rest_framework import serializers
from .models import Department, Education, Courses, Experience, Publication, TeacherEvent, Teacher, Recruiter

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name', 'description']

class EducationSerialzizer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['name','start_date','end_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['name', 'description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['name', 'position', 'start_date', 'end_date']

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['name', 'doi', 'publish_date']

class TeacherEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherEvent
        fields = ['name', 'date']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'dob', 'Field', 'department', 'education', 'experience', 'publication', 'self_events']
    
    department = DepartmentSerializer(many = True)
    education = EducationSerialzizer(many = True)
    experience = ExperienceSerializer(many = True)
    publication = PublicationSerializer(many = True)
    self_events = TeacherEventSerializer(many = True)

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['name', 'org_name', 'org_description', 'contact', 'website', 'position', 'linkedin', 'address', 'country', 'city']
