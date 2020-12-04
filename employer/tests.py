from django.test import TestCase, Client
from django.urls import reverse
from employer.forms import EmployeeForm  
from employer.models import Employee  

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
    
class TestUserRegistrationView(TestCase):
    
  def setUp(self):
    self.client = Client()

  def test_registration(self):
    url = reverse('emp')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

    response = self.client.post(url, {})
    self.assertEqual(response.status_code, 200)
   
    req_data = {
      'eid':"5", 'ename':"priyanka", 'eemail':"user1@gmail.com", 'econtact':"2345678"
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Employee.objects.count(), 1)

    req_data = {
      'eid':"4", 'ename':"", 'eemail':"user1@gmail.com", 'econtact':"2345678"
    }
    response = self.client.post(url, req_data)
    self.assertEqual(response.status_code, 302)
   