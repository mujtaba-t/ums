from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from collections import defaultdict
from statistics import mean
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.db.models import Q
from django.db.models import Count

# Create your views here.

# Teacher APIs
class TeacherDetail(RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class TeacherList(ListAPIView):
    serializer_class = TeacherEditSerializer
    queryset = Teacher.objects.all()

class TeacherEdit(APIView):

    def post(self, request):
        data = request.data
        teacher = get_object_or_404(Teacher, pk = request.data.get('id'))
        serializer = TeacherEditSerializer(teacher, data=data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class TeacherDepartmentCreateDelete(APIView):
    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        department_name = request.data.get('department_name')
        description = request.data.get('description')

        department = Department.objects.filter(department_name = department_name)

        if len(department) != 0:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            teacher.department.add(*department)
        else:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            new_department = Department(department_name = department_name, description = description)
            new_department.save()
            teacher.department.add(new_department)

        return Response("The Skill was successfully added")

    def delete(self, request):
        teacher_id = request.data.get('teacher_id')
        department_name = request.data.get('department_name')

        department = Department.objects.filter( department_name = department_name)
        teacher = get_object_or_404(Teacher, pk = teacher_id)
        teacher.department.remove(department)

class TeacherEducationCreateDelete(APIView):
    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        education = Education.objects.filter(name = name)

        if len(education) != 0:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            teacher.education.add(*education)
        else:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            new_education = Education(name = name, start_date = start_date, end_date = end_date)
            new_education.save()
            teacher.education.add(new_education)

        return Response("The Education was successfully added")

    def delete(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')

        education = Education.objects.filter( name = name)
        teacher = get_object_or_404(Teacher, pk = teacher_id)
        teacher.education.remove(education)

class TeacherExperienceCreateDelete(APIView):
    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')
        position = request.data.get('position')
        type = request.data.get('type')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        experience = Experience.objects.filter(name = name)

        if len(experience) != 0:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            teacher.experience.add(*experience)
        else:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            new_experience = Experience(name = name, position = position, type = type, start_date = start_date, end_date = end_date)
            new_experience.save()
            teacher.experience.add(new_experience)

        return Response("The Experience was successfully added")

    def delete(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')

        experience = Experience.objects.filter(name = name)
        teacher = get_object_or_404(Teacher, pk = teacher_id)
        teacher.experience.remove(experience)

class TeacherPublicationCreateDelete(APIView):
    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')
        doi = request.data.get('doi')
        publish_date = request.data.get('publish_date')

        publication = Publication.objects.filter(name = name)

        if len(publication) != 0:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            teacher.publication.add(*publication)
        else:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            new_publication = Publication(name = name, doi = doi, publish_date = publish_date)
            new_publication.save()
            teacher.publication.add(new_publication)

        return Response("The Publication was successfully added")

    def delete(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')

        publication = Publication.objects.filter(name = name)
        teacher = get_object_or_404(Teacher, pk = teacher_id)
        teacher.publication.remove(publication)

class TeacherEventCreateDelete(APIView):
    def post(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')
        date = request.data.get('date')

        event = TeacherEvent.objects.filter(name = name)

        if len(event) != 0:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            teacher.self_events.add(*event)
        else:
            teacher = get_object_or_404(Teacher, pk = teacher_id)
            new_event = TeacherEvent(name = name, date = date)
            new_event.save()
            teacher.self_events.add(new_event)

        return Response("The Event was successfully added")

    def delete(self, request):
        teacher_id = request.data.get('teacher_id')
        name = request.data.get('name')

        event = TeacherEvent.objects.filter(name = name)
        teacher = get_object_or_404(Teacher, pk = teacher_id)
        teacher.self_events.remove(event)

# Recruiter APIs
class RecruiterCreate(CreateAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

class RecruiterList(ListAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

class RecruiterDetail(RetrieveAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

class RecruiterEdit(APIView):

    def post(self, request):
        data = request.data
        recruiter = get_object_or_404(Recruiter, pk = request.data.get('id'))
        serializer = RecruiterSerializer(recruiter, data=data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class JobCreate(CreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

class JobList(APIView):

    def get(self, request, pk):
        jobs = Job.objects.filter(recruiter_id = pk)
        serializer = JobSerializer(jobs, many = True)
        return Response(serializer.data)

# Quiz APIs
class QuizList(ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

# StudentAPIs
class StudentList(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentEdit(APIView):

    def post(self, request):
        data = request.data
        student = get_object_or_404(Student, pk = request.data.get('id'))
        serializer = StudentSerializer(student, data=data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentDetail(APIView):

    def get(self, request, pk):

        skill_list = ['Java', 'Python', 'Html', 'React', 'SEO', 'Machine learning', 'Object Oriented Programming', 'Cyber Security', 'AWS', 'Javascript']

        dictionary = {}

        student = get_object_or_404(Student, pk = pk)

        dictionary['name'] = str(student.first_name) + " " + str(student.last_name)

        dictionary['dob'] = student.dob

        dictionary['department'] = student.department

        dictionary['semester'] = student.semester

        dictionary['portfolio'] = student.portfolio

        dictionary['profile_description'] = student.profile_description

        dictionary['talks_about'] = student.talks_about

        dictionary['p_num'] = student.phone_num

        dictionary['courses_done'] = (len(student.courses_grade.all().values()))

        dictionary['courses_total'] = (40)

        courses = CourseGrade.objects.filter(student_id = pk).select_related('student_id', 'coourse_id')

        gpa = defaultdict(list)

        courses_list = []

        for semester in range (1,9):
            for course in courses:
                if(int(course.coourse_id.semester) == semester):
                    gpa[semester].append(course.grade())
            try:
                gpa[semester] = mean(gpa[semester])
            except:
                pass
            
        cgpa = {key: round(sum([gpa for i,gpa in gpa.items() if i<=key and gpa])/sum([1 for i,gpa in gpa.items() if i<=key and gpa]), 2) if gpa[key] else [] for key in gpa.keys()}

        gpa = {key: 0 if type(value) == list else value for key, value in gpa.items()}
        cgpa = {key: 0 if type(value) == list else value for key, value in cgpa.items()}

        dictionary['gpa'] = gpa
        dictionary['cgpa'] = cgpa

        skills = student.skill.all()

        dictionary['skills'] = skills.values()

        experience = student.experience.all()

        dictionary['experience'] = experience.values()

        freelancing = student.freelancing.all()

        dictionary['freelancing'] = freelancing.values()

        projects = student.project.all()

        dictionary['projects'] = projects.values()

        courses_list.append([course.coourse_id.name, course.coourse_id.course_code, course.coourse_id.course_type, course.coourse_id.semester,
                            course.coourse_id.enrollment_date, course.coourse_id.faculty, course.coourse_id.total_marks, course.coourse_id.passing_marks,
                            course.marks] for course in courses)

        dictionary['courses'] = courses_list

        endorsements_given = Endorsement.objects.filter(giver_student_id =pk).select_related('giver_student_id', 'reciever_student_id')
        endorsements_taken = Endorsement.objects.filter(reciever_student_id =pk).select_related('giver_student_id', 'reciever_student_id')

        student_endoresement_given = []
        student_endoresement_taken = []

        for endoresement in endorsements_given:
            student_endoresement_given.append({'endoresement':endoresement.endorsement, 'datetime':endoresement.datetime, 
                                        'giver_name': str(endoresement.giver_student_id.first_name) + " " + str(endoresement.giver_student_id.last_name),
                                        'giver_profile': endoresement.giver_student_id.profile_description,
                                        'receiver_name': str(endoresement.reciever_student_id.first_name) + " " + str(endoresement.reciever_student_id.last_name),
                                        'receiver_profile': endoresement.reciever_student_id.profile_description})

        for endoresement in endorsements_taken:
            student_endoresement_taken.append({'endoresement':endoresement.endorsement, 'datetime':endoresement.datetime, 
                                        'giver_name': str(endoresement.giver_student_id.first_name) + " " + str(endoresement.giver_student_id.last_name),
                                        'giver_profile': endoresement.giver_student_id.profile_description,
                                        'receiver_name': str(endoresement.reciever_student_id.first_name) + " " + str(endoresement.reciever_student_id.last_name),
                                        'receiver_profile': endoresement.reciever_student_id.profile_description})

        dictionary['endorsements_given'] = student_endoresement_given
        dictionary['endorsements_taken'] = student_endoresement_taken

        quizes = QuizGrade.objects.filter(student_id = pk).select_related('student_id', 'quiz_id')

        quizes_all = Quiz.objects.all()

        dictionary['quizes'] = [[ quiz.quiz_id.name, quiz.quiz_id.passingmarks, quiz.marks, "Pass" if int(quiz.marks) > int(quiz.quiz_id.passingmarks) else "Retake"] for quiz in quizes]

        for quiz in quizes_all:
            templist = []
            for i in dictionary['quizes']:
                templist.append(i[0].lower())
            if quiz.name.lower() in templist:
                continue
            else:
                dictionary['quizes'].append([quiz.name, quiz.passingmarks, 'null', "Not Taken"])

        certificates = Certification.objects.filter(student_id = pk)

        certificates = certificates.values()

        for i in range(len(certificates)):
            certificates[i]['link'] = certificates[i]['link'].rsplit("/", 2)[-2]

        dictionary['certificates'] = certificates

        kpi = {}

        last_sem_cgpa = next((val for val in reversed(cgpa.values()) if val != 0), None)

        kpi = {
                'java': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'python': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'html': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'react': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'seo': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'machine learning': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'object oriented programming': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'cyber security': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'aws': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                },
                'javascript': {
                    'affective': 0,
                    'cognitive': 0,
                    'psychometric': 0
                }
            }

        student_with_most_projects = Student.objects.annotate(num_projects=Count('project')).order_by('-num_projects').first()

        certifications = Certification.objects.values('student_id').annotate(count=Count('student_id'))
        most_certified_student = certifications.order_by('-count')[0]

        for i in skill_list:
            # Calculation of Cognitive Percentile
            for quiz in quizes:
                if (quiz.quiz_id.name).lower() == i.lower():
                    kpi[i.lower()]['cognitive'] = (quiz.marks / 3 * 16.665)

            certificate_count = 0
            for certifacte in certificates:
                if i.lower() in certifacte.get('certificate_name').lower():
                    certificate_count += 1
            
            kpi[i.lower()]['cognitive'] += (certificate_count/most_certified_student['count']*10000*16.665)

            # Calculation of AFfective Percentile

            kpi[i.lower()]['affective'] = next((val/4 * 33.33 for val in reversed(cgpa.values()) if val != 0), None)

            # Calculate the Psychometric Percentiles

            for project in projects:
                if(project.top_skill1.lower() == i.lower() or project.top_skill2.lower() == i.lower() or project.top_skill3.lower() == i.lower()):
                    kpi[i.lower()]['psychometric'] = (len(student.project.all())/student_with_most_projects.num_projects*100*0.2)
        
        sorted_dict = dict(sorted(kpi.items(), key=lambda x: sum(x[1].values()),reverse = True))
 
        kpi_values = {k: v for i, (k, v) in enumerate(sorted_dict.items()) if i < 3}

        dictionary['kpi_values'] = kpi_values

        sports = student.sports.all()

        dictionary['sports'] = sports.values()

        debate = student.debate.all()

        dictionary['debate'] = debate.values()

        return Response(dictionary)

class CertificateVerification(APIView):
    
    def post(self,request):
        
        platform = request.data.get('platform')
        datetime = request.data.get('datetime')
        link = request.data.get('link')
        certificate_name = request.data.get('certificate_name')
        student_name = request.data.get('student_name')
        student_id = request.data.get('student_id')

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')

        # create a new headless Chrome browser instance
        driver = webdriver.Chrome(chrome_options=options)

        # navigate to the website
        driver.get(link)

        # wait for the text to be rendered
        text_to_search = student_name
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + text_to_search + "')]"))
            )
            driver.close()
            student = get_object_or_404(Student, pk = student_id)
            certificate = Certification(student_id = student, platform = platform, certificate_name = certificate_name, datetime = datetime, link = link, student_name = student_name)
            certificate.save()
            return Response(f"The text '{text_to_search}' was found on the website.")
        except:
            driver.close()
            return Response(f"The text '{text_to_search}' was not found on the website.")

class QuizUpdate(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        quiz_id = request.data.get('quiz_id')
        marks_obtained = request.data.get('marks_obtained')

        marks = QuizGrade.objects.filter(student_id_id = student_id, quiz_id_id = quiz_id)

        if len(marks) == 1:
            marks.update(marks = marks_obtained)
        else:
            marks_ = QuizGrade(student_id_id = student_id, quiz_id_id = quiz_id, marks = marks_obtained)
            marks_.save()

        serializer = QuizGradeSerializer(marks, many = True)

        return Response(serializer.data)

class SkillCreateDelete(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        skill = request.data.get('skill')

        skill_set = Skill.objects.filter(name = skill)

        if len(skill_set) != 0:
            student = get_object_or_404(Student, pk = student_id)
            student.skill.add(*skill_set)
        else:
            student = get_object_or_404(Student, pk = student_id)
            new_skill = Skill(name = skill)
            new_skill.save()
            student.skill.add(new_skill)

        return Response("The Skill was successfully added")

    def delete(self, request):
        student_id = request.data.get('student_id')
        skill = request.data.get('skill')

        skill_set = Skill.objects.filter( name = skill)
        student = get_object_or_404(Student, pk = student_id)
        student.skill.remove(skill_set)

class ExperienceCreateDelete(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('company_name')
        position = request.data.get('position')
        type = request.data.get('type')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        experience = Experience.objects.filter(name = name, position = position, type = type, start_date = start_date, end_date = end_date)

        if len(experience) != 0:
            student = get_object_or_404(Student, pk = student_id)
            student.experience.add(*experience)
        else:
            student = get_object_or_404(Student, pk = student_id)
            experience = Experience(name = name, position = position, type = type, start_date = start_date, end_date = end_date)
            experience.save()
            student.experience.add(experience)

        return Response("The Experience was successfully added")

    def delete(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('company_name')
        position = request.data.get('position')
        type = request.data.get('type')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        experience = Experience.objects.filter(name = name, position = position, type = type, start_date = start_date, end_date = end_date)
        student = get_object_or_404(Student, pk = student_id)
        student.experience.remove(*experience)

class FreelancingCreateDelete(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('company_name')
        position = request.data.get('position')
        level = request.data.get('level')
        rating = request.data.get('rating')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        freelance = Freelancing.objects.filter(name = name, position = position, level = level, rating = rating,start_date = start_date, end_date = end_date)

        if len(freelance) != 0:
            student = get_object_or_404(Student, pk = student_id)
            student.freelancing.add(*freelance)
        else:
            student = get_object_or_404(Student, pk = student_id)
            freelance = Freelancing(name = name, position = position, level = level, rating = rating,start_date = start_date, end_date = end_date)
            freelance.save()
            student.freelancing.add(freelance)

        return Response("The Freelancing Field was successfully added")

    def delete(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('company_name')
        position = request.data.get('position')
        level = request.data.get('level')
        rating = request.data.get('rating')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        freelance = Freelancing.objects.filter(name = name, position = position, level = level, rating = rating,start_date = start_date, end_date = end_date)
        student = get_object_or_404(Student, pk = student_id)
        student.freelancing.remove(*freelance)

class ProjectCreateDelete(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('name')
        description = request.data.get('description')
        top_skill1 = request.data.get('top_skill1')
        top_skill2 = request.data.get('top_skill2')
        top_skill3 = request.data.get('top_skill3')

        project = Project.objects.filter(name = name, discription = description, top_skill1 = top_skill1, top_skill2 = top_skill2, top_skill3 = top_skill3)

        if len(project) != 0:
            student = get_object_or_404(Student, pk = student_id)
            student.project.add(*project)
        else:
            student = get_object_or_404(Student, pk = student_id)
            project = Project(name = name, discription = description, top_skill1 = top_skill1, top_skill2 = top_skill2, top_skill3 = top_skill3)
            project.save()
            student.project.add(project)

        return Response("The Project Field was successfully added")

    def delete(self, request):
        student_id = request.data.get('student_id')
        name = request.data.get('company_name')
        description = request.data.get('description')
        top_skill1 = request.data.get('top_skill1')
        top_skill2 = request.data.get('top_skill2')
        top_skill3 = request.data.get('top_skill3')

        project = Project.objects.filter(name = name, discription = description, top_skill1 = top_skill1, top_skill2 = top_skill2, top_skill3 = top_skill3)
        student = get_object_or_404(Student, pk = student_id)
        student.project.remove(*project)

class Kpi(APIView):
    def get(self, request):
        
        kpi_list = []

        students = Student.objects.all().prefetch_related('courses_grade', 'quiz_grade', 'project', 'skill')

        student_with_most_projects = Student.objects.annotate(num_projects=Count('project')).order_by('-num_projects').first()

        certifications = Certification.objects.values('student_id').annotate(count=Count('student_id'))
        most_certified_student = certifications.order_by('-count')[0]

        for student in students:
            sum_marks = 0
            courses = CourseGrade.objects.filter(student_id = student.id).select_related('student_id', 'coourse_id')
            for course in courses:
                sum_marks += course.marks
            course_score = (sum_marks/37*0.2)

            gpa = defaultdict(list)

            for semester in range (1,9):
                for course in courses:
                    if(int(course.coourse_id.semester) == semester):
                        gpa[semester].append(course.grade())
                try:
                    gpa[semester] = mean(gpa[semester])
                except:
                    pass
            
            cgpa = {key: round(sum([gpa for i,gpa in gpa.items() if i<=key and gpa])/sum([1 for i,gpa in gpa.items() if i<=key and gpa]), 2) if gpa[key] else [] for key in gpa.keys()}
            cgpa = {key: 0 if type(value) == list else value for key, value in cgpa.items()}
            last_sem_cgpa = next((val for val in reversed(cgpa.values()) if val != 0), None)

            quizes = QuizGrade.objects.filter(student_id = student.id).select_related('student_id', 'quiz_id')
            quiz_marks = 0
            for quiz in quizes:
                quiz_marks += (quiz.marks/3)
            
            try:
                quiz_score = (quiz_marks/len(quizes)*100*0.4)
            except:
                quiz_score = 0


            project_score = (len(student.project.all())/student_with_most_projects.num_projects*100*0.2)

            certificates = Certification.objects.filter(student_id = student.id)

            certifcate_score = (len(certificates)/most_certified_student['count']*100*0.2)

            experience_years = 0.00

            for experience in student.experience.all():
                time_diff = experience.end_date - experience.start_date
                experience_years += time_diff.days / 365.25

            kpi_list.append(
                                {
                                    'student_id': student.id, 
                                    'student_name': student.first_name + " " + student.last_name , 
                                    'score': course_score + quiz_score + project_score + certifcate_score,
                                    'department': student.department,
                                    'batch': student.enrollment_year + 4,
                                    'Semester': student.semester,
                                    'skills': student.skill.all().values(),
                                    'experiance': f'{experience_years:.2f}',
                                    'cgpa': last_sem_cgpa
                                }
                            )

        sorted_list = sorted(kpi_list, key=lambda x: x['score'], reverse=True)

        return Response(sorted_list)

# Endoresement APIs
class EndorsementCreate(CreateAPIView):

    serializer_class = EndorsementSerializer
    queryset = Endorsement.objects.all()

class Event(ListAPIView):

    serializer_class = EventSerializer
    queryset = Event.objects.all()