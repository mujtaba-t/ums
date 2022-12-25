from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length= 200)
    description = models.TextField()

class Education(models.Model):
    name = models.CharField(max_length= 200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Courses(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField()

class Experience(models.Model):
    name = models.CharField(max_length= 200)
    position = models.CharField(max_length= 200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Publication(models.Model):
    name = models.CharField(max_length= 50)
    doi = models.CharField(max_length= 50)
    publish_date = models.DateTimeField()

class TeacherEvent(models.Model):
    name = models.CharField(max_length= 200)
    date = models.DateTimeField()


class Teacher(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    dob = models.DateTimeField()
    Field = models.CharField(max_length= 200)
    department = models.ManyToManyField(Department, verbose_name='list of departments')
    education = models.ManyToManyField(Education, verbose_name='list of qualifications')
    experience = models.ManyToManyField(Experience, verbose_name='list of experiences')
    publication = models.ManyToManyField(Publication, verbose_name='list of publications')
    self_events = models.ManyToManyField(TeacherEvent, verbose_name='list of events')

class Recruiter(models.Model):
    name = models.CharField(max_length = 200)
    org_name = models.CharField(max_length = 50)
    org_description = models.TextField()
    contact = models.CharField(max_length = 50)
    website = models.CharField(max_length = 50)
    position = models.CharField(max_length = 100)
    linkedin = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    country = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)

    