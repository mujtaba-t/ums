from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from .models import *

# Create your tests here.

class ManagementAPITest(APITestCase):
    def test_quiz_endpoint(self):

        # Make a request to the endpoint
        response = self.client.get('/management/quizes/')
        # Assert that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

    def test_teacher_endpoint(self):

        response = self.client.get('/management/teacher-list/')
        self.assertEqual(response.status_code, 200)

class EndorsementCreateTestCase(APITestCase):
    def setUp(self):
        self.giver = Student.objects.create(first_name='John', last_name='Doe', dob='2000-01-01T00:00:00Z', semester='1', phone_num='+1234567890')
        self.reciever = Student.objects.create(first_name='Jane', last_name='Doe', dob='2000-01-01T00:00:00Z', semester='1', phone_num='+1234567890')
        self.data = {
            'giver_student_id': self.giver.id,
            'reciever_student_id': self.reciever.id,
            'endorsement': 'This student is a hard worker.',
            'datetime': '2022-01-01T12:00:00Z'
        }

    def test_endorsement_create(self):
        response = self.client.post('/management/endorsement-create/', self.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Endorsement.objects.count(), 1)
        self.assertEqual(Endorsement.objects.get().giver_student_id, self.giver)
        self.assertEqual(Endorsement.objects.get().reciever_student_id, self.reciever)
        self.assertEqual(Endorsement.objects.get().endorsement, 'This student is a hard worker.')

class CertificateConfirmationTestCase(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(first_name='Moiz', last_name='Ahmed', dob='2000-01-01T00:00:00Z', semester='1', phone_num='+1234567890')
        self.data = {
                "platform" : "Udemy",
                "datetime" : "2022-01-01T12:00:00Z",
                "link" : "https://www.udemy.com/certificate/UC-01757b49-c3bf-467a-afa0-1e2f3cf824e0/",
                "student_name" : str(self.student.first_name) + " " + str(self.student.last_name),
                "student_id" : 1
        }

    def test_certificate_verification(self):
        response = self.client.post('/management/certificate/', self.data)
        self.assertEqual(response.content, b'"The text \'Moiz Ahmed\' was found on the website."')
        self.assertEqual(response.status_code, 200)
