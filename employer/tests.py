from django.test import TestCase, Client
from django.urls import reverse
from employer.forms import EmployeeForm  
from employer.models import Employee  
import unittest
import json
class Setup_Class(TestCase):

    def setUp(self):
        self.user = Employee.objects.create(eid="2", ename="user1", eemail="user@gmail.com", econtact="12345678")

    def test_model_str(self):
        emp = Employee.objects.create(eid="2", ename="priyanka", eemail="user@gmail.com", econtact="12345678")
        self.assertEqual(str(emp), "priyanka")

class User_Form_Test(TestCase):

    def test_UserForm_valid(self):
        form = EmployeeForm(data={'eid':"3", 'ename':"user2", 'eemail':"user1@gmail.com", 'econtact':"2345678"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = EmployeeForm(data={'eid':"3", 'ename':"", 'eemail':"user1@gmail.com", 'econtact':"2345678"})
        self.assertFalse(form.is_valid())
    
class TestAPI(TestCase):
    def setUp(self):
        self.client = Client()
        emp4=Employee.objects.create(eid="4", ename="user4", eemail="user4@gmail.com", econtact="1235678")
        emp5=Employee.objects.create(eid="5", ename="user5", eemail="user5@gmail.com", econtact="12345678")
        emp6=Employee.objects.create(eid="6", ename="user6", eemail="user6@gmail.com", econtact="123d458")
        emp7=Employee.objects.create(eid="7", ename="user7", eemail="user7@gmail.com", econtact="123d456")
    def test_get_all(self):
        response = self.client.get(reverse('show'))
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        
    def test_get_all_return_none(self):
        response = self.client.get(reverse('show'))
        self.assertIsNotNone(response)

    def test_get_valid_single_employee(self):
            response = self.client.get(
            reverse('show'), kwargs={'eid':1})
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 200)
            
    def test_get_invalid_single_employee(self):
            client = Client()
            response = client.post('/edit/', {'eid':456})
            self.assertIsNotNone(response)
            self.assertEqual(response.status_code, 404)
        
    def test_create_valid_employee(self):
        valid_payload={'eid':"10", 'ename':"abc", 'eemail':"user10@gmail.com", 'econtact':"234511678"}
        response = self.client.post(
            reverse('emp'),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
     
    def test_create_invalid_employee(self):
        valid_payload={'eid':"10", 'ename':'','eemail':"user10@gmail.com", 'econtact':"234511678"}
        response = self.client.post(
            reverse('emp'),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
       

class DeleteEmployeeTest(TestCase):

    def setUp(self):
        self.emp4= Employee.objects.create(eid="4", ename="user4", eemail="user4@gmail.com", econtact="1235678")
        self.emp5= Employee.objects.create(eid="5", ename="user5", eemail="user5@gmail.com", econtact="1278898")

    def test_valid_delete_employee(self):
        client = Client()
        response = client.delete(
            reverse('delete', kwargs={'id': self.emp5.id}))
        self.assertEqual(response.status_code,302)

    def test_invalid_delete_employee(self):
        client = Client()
        response = client.delete('delete', kwargs={'id':4 })
        self.assertEqual(response.status_code,404)
