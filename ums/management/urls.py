from django.urls import path
from . import views
app_name = 'management'

urlpatterns = [

    # Teacher APIs
    path('teacher-detail/<int:pk>/', views.TeacherDetail.as_view(), name='teacher'),
    path('teacher-list/', views.TeacherList.as_view(), name='teacher_list'),
    path('teacher-edit/', views.TeacherEdit.as_view(), name='teacher_create'),
    path('teacher-department/', views.TeacherDepartmentCreateDelete.as_view(), name='teacher_department'),
    path('teacher-education/', views.TeacherEducationCreateDelete.as_view(), name='teacher_education'),
    path('teacher-experience/', views.TeacherExperienceCreateDelete.as_view(), name='teacher_experience'),
    path('teacher-publication/', views.TeacherPublicationCreateDelete.as_view(), name='teacher_publication'),
    path('teacher-event/', views.TeacherEventCreateDelete.as_view(), name='teacher_event'),

    # Recruiter APIs
    path('recruiter-detail/<int:pk>/', views.RecruiterDetail.as_view(), name='recruiter'),
    path('recruiter-list/', views.RecruiterList.as_view(), name='recruiter_list'),
    path('recruiter-create/', views.RecruiterCreate.as_view(), name='add_recruiter'),
    path('recruiter-edit/', views.TeacherEdit.as_view(), name='recruiter_edit'),
    path('job-list/<int:pk>/', views.JobList.as_view(), name='job_list'),
    path('job-create/', views.JobCreate.as_view(), name='job_create'),

    # Quiz APIs
    path('quizes/', views.QuizList.as_view(), name='quiz_list'),

    # Student APIs
    path('student-list/', views.StudentList.as_view(), name='student_list'),
    path('student-detail/<int:pk>/', views.StudentDetail.as_view(), name='student'),
    path('student-edit/', views.StudentEdit.as_view(), name='student_edit'),
    path('quiz-update/', views.QuizUpdate.as_view(), name='quiz_update'),
    path('skill/', views.SkillCreateDelete.as_view(), name='skill'),
    path('experience/', views.ExperienceCreateDelete.as_view(), name='experience'),
    path('freelance/', views.FreelancingCreateDelete.as_view(), name='freelance'),
    path('project/', views.ProjectCreateDelete.as_view(), name='project'),
    path('certificate/', views.CertificateVerification.as_view(), name='certificate_verification'),
    path('kpi/', views.Kpi.as_view(), name = 'kpi_view'),

    # Endorsement APIs
    path('endorsement-create/', views.EndorsementCreate.as_view(), name='add_endorsement'),


    # Events
    path('event-list/', views.Event.as_view(), name='event_list'),
]