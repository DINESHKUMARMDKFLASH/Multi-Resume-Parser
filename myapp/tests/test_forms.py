from django.test import SimpleTestCase
from ..forms import StudentsForm


class TestForms(SimpleTestCase):

    def test_student_form_data_is_valid(self):
        form = StudentsForm(data={
            'fname': 'fname1',
            'lname': 'lname1',
            'mail': 'email@gmail.com',
            'phno': "1234567890",
            'st': 'street',
            'city': 'city1',
            'state': 'state1',
            'country': 'country1',
            'pincode': '456789',
            'work': 'abcdef',
            'edu': 'cse',
            'skill': 'python',
            'workexp': '5 years'
        })

        self.assertTrue(form.is_valid())

    def test_student_form_data_is_invalid(self):
        form = StudentsForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 13)
