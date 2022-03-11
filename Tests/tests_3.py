#

import os
import inspect
from TwosComplement.models import UserProfile, Questionnaire
from population_script import populate
from django.test import TestCase
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class FormClassTests(TestCase):
    """
    Do the Form classes exist, and do they contain the correct instance variables?
    """
    def test_module_exists(self):
        """
        Tests that the forms.py module exists in the expected location.
        """
        project_path = os.getcwd()
        TwosComplement_app_path = os.path.join(project_path, 'TwosComplement')
        forms_module_path = os.path.join(TwosComplement_app_path, 'forms.py')

        self.assertTrue(os.path.exists(forms_module_path), f"{FAILURE_HEADER}We couldn't find Rango's new forms.py module. This is required to be created at the top of Section 7.2. This module should be storing your two form classes.{FAILURE_FOOTER}")
    
    def test_UserProfile_form_class(self):
        """
        Does the UserProfileForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import UserProfileForm.
        import TwosComplement.forms
        self.assertTrue('UserProfileForm' in dir(TwosComplement.forms), f"{FAILURE_HEADER}The class UserProfile could not be found in TwosComplement's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from TwosComplement.forms import UserProfileForm
        UserProfile_form = UserProfileForm()

        # Do you correctly link UserProfile to UserProfileForm?
        self.assertEqual(type(UserProfile_form.__dict__['instance']), UserProfile, f"{FAILURE_HEADER}The UserProfileForm does not link to the UserProfile model. Have a look in the CategoryForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = UserProfile_form.fields

        expected_fields = {
            'age' : django_fields.IntegerField,
            'name' : django_fields.CharField,
            'phone' : django_fields.CharField,
            'photo' : django_fields.ImageField,
            'bio' : django_fields.CharField,
            'gender' : django_fields.CharField,
            'sexualPreference' : django_fields.CharField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your UserProfileForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in UserProfileForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")


class UserProfileFormAncillaryTests(TestCase):
    """
    Performs checks to see if all the additional requirements for adding a UserProfileForm have been implemented correctly.
    Checks URL mappings and server output.
    """
    def test_UserProfile_url_mapping(self):
        """
        Tests whether the URL mapping for adding a category is resolvable.
        """
        try:
            resolved_name = resolve('/TwosComplement/register/').view_name
        except:
            resolved_name = ''
        
        self.assertEqual(resolved_name, 'TwosComplement:register', f"{FAILURE_HEADER}The lookup of URL '/TwosComplement/register/' didn't return a mapping name of 'TwosComplement:register'. Check you have the correct URL mapping for registering, and try again.{FAILURE_FOOTER}")
    
    
    def test_register_template(self):
        """
        Checks whether a template was used for the add_category() view.
        """
        response = self.client.get(reverse('TwosComplement:register'))
        self.assertTemplateUsed(response, 'TwosComplement/register.html', f"{FAILURE_HEADER}The register.html template is not used for the UserProfile() view. The specification requires this.{FAILURE_FOOTER}")

class QuestionnaireClassTests(TestCase):
    """
    Checks whether the Questionnaire form class has been implemented correctly.
    """
    def test_Questionnaire_form_class(self):
        """
        Does the QuestionnaireForm implementation exist, and does it contain the correct instance variables?
        """
        # Check that we can import QuestionnaireForm.
        import TwosComplement.forms
        self.assertTrue('QuestionnaireForm' in dir(TwosComplement.forms), f"{FAILURE_HEADER}The class QuestionnaireForm could not be found in TwosComplement's forms.py module. Check you have created this class in the correct location, and try again.{FAILURE_FOOTER}")

        from TwosComplement.forms import QuestionnaireForm
        Questionnaire_form = QuestionnaireForm()

        # Do you correctly link Questionnaire to QuestionnaireForm?
        self.assertEqual(type(Questionnaire_form.__dict__['instance']), Questionnaire, f"{FAILURE_HEADER}The QuestionnaireForm does not link to the Questionnaire model. Have a look in the QuestionnaireForm's nested Meta class for the model attribute.{FAILURE_FOOTER}")

        # Now check that all the required fields are present, and of the correct form field type.
        fields = Questionnaire_form.fields

        expected_fields = {
            'Q1' : django_fields.CharField,
            'Q2' : django_fields.CharField,
            'Q3' : django_fields.CharField,
            'Q4' : django_fields.CharField,
            'Q5' : django_fields.CharField,
            'Q6' : django_fields.CharField,
            'Q7' : django_fields.CharField,
            'Q8' : django_fields.CharField,
            'Q9' : django_fields.CharField,
            'Q10' : django_fields.CharField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field '{expected_field_name}' was not found in your QuestionnaireForm implementation. Check you have all required fields, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field '{expected_field_name}' in QuestionnaireForm was not of the expected type '{type(fields[expected_field_name])}'.{FAILURE_FOOTER}")

