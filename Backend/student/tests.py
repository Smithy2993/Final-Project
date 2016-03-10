from django.test import TestCase
from student.models import student

class StudentTestCase(TestCase):

##These tests are intended to pass
##The records intended to fail are below

        def setUp(self): 
                student.objects.create(student_ID="406783796", first_name="Thomas", middle_name="Victor", last_name="Ronaldo", gender="M", year="3", degree="Information Technology")
                student.objects.create(student_ID="647838992", first_name="Gerald", middle_name="b", last_name="Messi", gender="M", year="3", degree="Information Technology")
                
                
                student.objects.create(student_ID="9999999999", first_name="Bill", middle_name="Victor", last_name="Ronaldo34", gender="M", year="3rd", degree="Information Technology")
                student.objects.create(student_ID="529348992", first_name="Fred", middle_name="b", last_name="Messi", gender="Female", year="3", degree="Information Technology")
                

        def test_student(self):
                Tom = student.objects.get(first_name="Thomas")
                Gez = student.objects.get(first_name="Gerald")
                Bill = student.objects.get(first_name="Bill")
                Fred = student.objects.get(first_name="Fred")
                self.assertTrue(isinstance(Tom, student))
                self.assertTrue(isinstance(Gez, student))
                self.assertTrue(isinstance(Bill, student))
                self.assertTrue(isinstance(Fred, student))

