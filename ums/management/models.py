from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length= 200)
    description = models.TextField()

    def __str__(self):
        return self.department_name

class Education(models.Model):
    name = models.CharField(max_length= 200)
    start_date = models.DateTimeField(null = True, blank = True)
    end_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length= 200)
    position = models.CharField(max_length= 200)
    type = models.CharField(max_length= 200)
    start_date = models.DateTimeField(null = True, blank = True)
    end_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length= 50)
    doi = models.CharField(max_length= 50)
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.name

class TeacherEvent(models.Model):
    name = models.CharField(max_length= 200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    dob = models.DateTimeField()
    Field = models.CharField(max_length= 200)
    profile_description = models.CharField(max_length = 200)
    talks_about = models.CharField(max_length = 200)
    phone_num = models.CharField(max_length=17)
    designation = models.TextField()
    department = models.ManyToManyField(Department, verbose_name='list of departments')
    education = models.ManyToManyField(Education, verbose_name='list of qualifications')
    experience = models.ManyToManyField(Experience, verbose_name='list of experiences')
    publication = models.ManyToManyField(Publication, verbose_name='list of publications')
    self_events = models.ManyToManyField(TeacherEvent, verbose_name='list of events')

    def __str__(self):
        return self.first_name

class Recruiter(models.Model):
    name = models.CharField(max_length = 200)
    org_name = models.CharField(max_length = 50)
    org_description = models.TextField()
    contact = models.CharField(max_length = 50)
    website = models.CharField(max_length = 50)
    position = models.CharField(max_length = 100)
    email = models.CharField(max_length = 150)
    linkedin = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    country = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    working_since = models.CharField(max_length = 100)
    github = models.CharField(max_length = 100)
    looking_for = models.CharField(max_length = 100)
    document = models.FileField(upload_to="document/", max_length=250, null=True, default=None)

    def __str__(self):
        return self.name

class Job(models.Model):
    position = models.CharField(max_length = 200)
    cgpa = models.FloatField()
    requirements = models.TextField()
    job_description = models.TextField()
    recruiter_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

class QuizQuestion(models.Model):
    question = models.TextField()
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    correct = models.TextField()

    def __str__(self):
        return self.question

class Quiz(models.Model):
    name = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)
    questions = models.CharField(max_length = 50)
    level = models.CharField(max_length = 50)
    passingmarks = models.CharField(max_length = 50)
    quiz_description = models.TextField()
    questions = models.ManyToManyField(QuizQuestion)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 50)
    course_code = models.CharField(max_length = 50)
    course_type = models.CharField(max_length = 50)
    semester = models.CharField(max_length = 50)
    enrollment_date = models.DateTimeField()
    faculty = models.CharField(max_length = 100)
    total_marks = models.IntegerField()
    passing_marks = models.IntegerField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Freelancing(models.Model):
    name = models.CharField(max_length= 200)
    position = models.CharField(max_length= 200)
    rating = models.CharField(max_length= 10)
    level = models.CharField(max_length=200)
    start_date = models.DateTimeField(null = True, blank = True)
    end_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length= 200)
    discription = models.TextField()
    top_skill1 = models.CharField(max_length= 200)
    top_skill2 = models.CharField(max_length= 200)
    top_skill3 = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Sports(models.Model):
    name = models.CharField(max_length= 200)
    date = models.DateField()
    played = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Debate(models.Model):
    name = models.CharField(max_length= 200)
    date = models.DateField()
    participate = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    dob = models.DateTimeField()
    department = models.TextField()
    semester = models.CharField(max_length=100)
    enrollment_year = models.IntegerField()
    portfolio = models.TextField()
    profile_description = models.TextField()
    talks_about = models.CharField(max_length = 200)
    phone_num = models.CharField(max_length=17)
    quiz_grade = models.ManyToManyField(Quiz, through='QuizGrade')
    courses_grade = models.ManyToManyField(Course, through='CourseGrade')
    skill = models.ManyToManyField(Skill)
    experience = models.ManyToManyField(Experience)
    freelancing = models.ManyToManyField(Freelancing)
    project = models.ManyToManyField(Project)
    sports = models.ManyToManyField(Sports)
    debate = models.ManyToManyField(Debate)

    def __str__(self):
        return self.first_name

class QuizGrade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    marks = models.IntegerField()

class CourseGrade(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    coourse_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def grade(self):
        if self.marks > 90:
            return 4.0
        elif self.marks > 80:
            return 3.5
        elif self.marks > 70:
            return 3.0
        elif self.marks > 60:
            return 2.5
        elif self.marks > 50:
            return 2.0
        elif self.marks > 40:
            return 1.5
        else:
            return 0

class Endorsement(models.Model):
    giver_student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='endorsement_giver')
    reciever_student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='endorsement_reciever')
    endorsement = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.endorsement

class Certification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_name = models.TextField()
    platform = models.TextField()
    datetime = models.DateTimeField()
    link = models.TextField()
    student_name = models.TextField()

    def __str__(self):
        return self.certificate_name

class Event(models.Model):
    name = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name
