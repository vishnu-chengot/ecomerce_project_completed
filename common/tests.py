from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse ,resolve

# Create your tests here.

class Testcommon(TestCase):
    def setup(self):
       self.client =APIClient
    
    def test_index(self):
       url =reverse('common:index')
       res =self.client.get(url)
      #  print(res.data)

      #  self.assertEqual(res.status_code,200)

       self.assertEqual(res.data,'congratulation, you have created an api')

    def test_float(self):
      url = reverse('common:float')
      res =self.client.get(url) 
      data =res.data
      if type(data) != float:
        raise AssertionError('error')

      return True
    
