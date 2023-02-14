from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name', 'description']

class EducationSerialzizer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id','name','start_date','end_date']

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['name', 'description']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['name', 'position', 'type', 'start_date', 'end_date']

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
        partial = True
        fields = ['first_name', 'last_name', 'dob', 'Field', 'profile_description', 'talks_about', 'phone_num', 'designation', 'department', 'education', 'experience', 'publication', 'self_events']
    
    department = DepartmentSerializer(many = True)
    education = EducationSerialzizer(many = True)
    experience = ExperienceSerializer(many = True)
    publication = PublicationSerializer(many = True)
    self_events = TeacherEventSerializer(many = True)

class TeacherEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        partial = True
        fields = ['id', 'first_name', 'last_name', 'dob', 'Field', 'profile_description', 'talks_about', 'phone_num', 'designation']

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['id', 'name', 'org_name', 'org_description', 'contact', 'website', 'email', 'position', 'linkedin', 'address', 'country', 'city', 'working_since', 'github', 'looking_for', 'document']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['position', 'cgpa', 'requirements', 'job_description', 'recruiter_id']

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['question', 'a', 'b', 'c', 'd', 'correct']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'time', 'questions', 'level', 'passingmarks', 'quiz_description', 'questions', 'passing_percentage']

    questions = QuizQuestionSerializer(many = True)
    passing_percentage = serializers.SerializerMethodField()

    def get_passing_percentage(self, obj):

        total_quizes_taken = QuizGrade.objects.filter(student_id_id = obj.id)
        total_quizes_passed = QuizGrade.objects.filter(student_id_id = obj.id, marks__gte = obj.passingmarks)

        return len(total_quizes_passed)/len(total_quizes_taken) * 100 if len(total_quizes_taken) != 0 else 0

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'course_code', 'course_type', 'semester', 'enrollment_date', 'faculty', 'total_marks', 'passing_marks']

class QuizGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizGrade
        fields = ['id', 'marks']

class CourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseGrade
        fields = ['id', 'marks']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class FreelancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancing
        fields = ['name', 'position', 'rating', 'level' ,'start_date', 'end_date']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freelancing
        fields = ['name', 'description', 'top_skill1', 'top_skill2', 'top_skill3']

class StudentSerializer(serializers.ModelSerializer):

    # quiz_grade = QuizSerializer(many = True)
    # courses_grade = CourseSerializer(many = True)
    # skill = SkillSerializer(many = True)
    # experience = ExperienceSerializer(many = True)
    # freelancing = FreelancingSerializer(many = True)
    # project = ProjectSerializer(many = True)

    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name', 'dob', 'department', 'portfolio', 'semester', 'profile_description', 'talks_about', 'phone_num']

class EndorsementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endorsement
        fields = ['giver_student_id', 'reciever_student_id', 'endorsement', 'datetime']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'datetime']