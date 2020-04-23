from django.test import TestCase
from ..models import Students


class TestModels(TestCase):

    def setUp(self):
        self.form1 = Students.objects.create(
            fname='fname1',
            lname='lname1',
            mail='email@gmail.com',
            phno="1234567890",
            st='street',
            city='city1',
            state='state1',
            country='country1',
            pincode='456789',
            work='abcdef',
            edu='cse',
            skill='python',
            workexp='5years'
        )

    def test_model_values_is_assigned_on_creation(self):
        self.assertEquals(self.form1.fname, 'fname1')
