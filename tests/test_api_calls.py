import unittest
import requests
import json
from responses_api_calls import *

"""
File made for purposes of testing the whole API call mechanism
Requires API to be running
"""

base_url = "http://127.0.0.1:5000/companies/"
#Apple&Alphabet&Amazon&Netflix?date_s=2021-12-06&date_e=2021-12-10'

class TestApiCalls(unittest.TestCase):
    #test_ammountOfCompanies_date/rangeOfDates
    
    #Single company, single date
    def test_single_date(self):
        url = base_url+"Apple?date=2021-12-06"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_single_date, "Single company and single date test.")
    
    #Single company, date range 
    def test_single_range(self):
        url = base_url+"Apple?date_s=2021-12-06&date_e=2021-12-08"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_single_range, "Single company and date range test.")
    #
    # Multiple companies, single date
    def test_multi_date(self):
        url = base_url+"Apple&Amazon?date=2021-12-06"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_multi_date, "Multiple companies and single date test.")
        
    #Multiple companies, date range
    def test_multi_range(self):
        url = base_url+"Apple&Alphabet?date_s=2020-12-07&date_e=2020-12-09"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_multi_range, "Multiple companies and date range test.")
    
    #Multiple companies, single date and date range
    def test_multi_both(self):
        url = base_url+"Meta&Netflix?date=2021-12-06&date_s=2021-12-06&date_e=2022-12-06"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_multi_both, "Multiple companies and both date and date range test.")
        
    #Test cases in which there should be an negative response
    def test_wrong_arg_response(self):
        url = base_url+"Meta&Netflix?dae=2021-12-06"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_wrong_arg, "Wrongly assembled url test.")
    
    #Date which is on a weekend
    def test_no_data_response(self): 
        url = base_url+"Meta&Netflix?date=2021-12-05"
        response = json.loads(requests.get(url).text)
        self.assertEqual(response,response_no_data, "Url with date on a weekend test.")
    

if __name__=="__main__":
    unittest.main()