from django.test import TestCase
from alumni.models import alumni
from unittest import skip

class AlumniTest(TestCase):
        def setUp(self):
                alumni.objects.create(first_name='John',last_name='Tomkins',course='Information Technology',faculty='Eng',sector='IT',self_employed='Yes')
                alumni.objects.create(first_name='Bill',last_name='Nials',course='Computer Science',faculty='Eng',sector='IT',self_employed='Yes')
                alumni.objects.create(first_name='Fred',last_name='Tilsley',course='Information Technology',faculty='Eng',sector='Law',self_employed='No')
                alumni.objects.create(first_name='Jake',last_name='Rooney',course='Computer Science',faculty='Eng',sector='Healthcare',self_employed='No')
                alumni.objects.create(first_name='Tom',last_name='Jacobs',course='Information Technology',faculty='Eng',sector='IT',self_employed='Yes')
                
                

        def empty_strings(self):
                self.fail('cannot be empty strings')
