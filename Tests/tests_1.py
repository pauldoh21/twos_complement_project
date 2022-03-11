
# This is the initial test file that will test to make sure that the project has been correctly setup and exists correctly

import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class InitialProjectLaunchTest(TestCase):
    """
    Simple tests to probe the file structure of the project.
    There is also a test to check that you TwosComplement is added to the list of INSTALLED_APPS.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.TwosComplement_app_dir = os.path.join(self.project_base_dir, 'TwosComplement')
    
    def test_project_created(self):
        """
        Tests whether the twos_complement_project configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'twos_complement_project'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'twos_complement_project', 'urls.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The twos_complement_project configuration directory doesn't seem to exist. Did you use the correct name?{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}The project's urls.py module does not exist. Did you use the startproject command?{FAILURE_FOOTER}")
    
    def test_TwosComplement_app_created(self):
        """
        Determines whether the TwosComplement app has been created.
        """
        directory_exists = os.path.isdir(self.TwosComplement_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.TwosComplement_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.TwosComplement_app_dir, 'views.py'))
        
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The TwosComplement app directory does not exist. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The TwosComplement directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The TwosComplement directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
    
    def test_TwosComplement_has_urls_module(self):
        """
        Did you create a separate urls.py module for TwosComplement?
        """
        module_exists = os.path.isfile(os.path.join(self.TwosComplement_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The TwosComplement app's urls.py module is missing.{FAILURE_FOOTER}")
    
    def test_is_TwosComplement_app_configured(self):
        """
        Did you add the new TwosComplement app to your INSTALLED_APPS list?
        """
        is_app_configured = 'TwosComplement' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The TwosComplement app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
    
class Chapter3IndexPageTests(TestCase):
    """
    Testing the basics of the index view and URL mapping.
    Also runs tests to check the response from the server.
    """
    def setUp(self):
        self.views_module = importlib.import_module('TwosComplement.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('twos_complement_project.urls')
    
    def test_view_exists(self):
        """
        Does the index() view exist in TwosComplement's views.py module?
        """
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.index)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}The index() view for TwosComplement does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check that you have created the index() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
    
    def test_mappings_exists(self):
        """
        Are the two required URL mappings present and correct?
        One should be in the project's urls.py, the second in TwosComplement's urls.py.
        We have the 'index' view named twice -- it should resolve to '/TwosComplement/'.
        """
        index_mapping_exists = False
        
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'index':
                    index_mapping_exists = True
        
        self.assertTrue(index_mapping_exists, f"{FAILURE_HEADER}The index URL mapping could not be found. Check your PROJECT'S urls.py module.{FAILURE_FOOTER}")
        self.assertEquals(reverse('TwosComplement:index'), '/TwosComplement/', f"{FAILURE_HEADER}The index URL lookup failed. Check TwosComplement's urls.py module. You're missing something in there.{FAILURE_FOOTER}")
  