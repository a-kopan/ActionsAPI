import unittest
import os
import sys
from .responses_db_interactions import *

#Add repo dir to path so tests can access the database and db_interactions methods
current = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current,os.pardir))
sys.path.append(parent_dir)

from src.db_interactions import *

"""
Tests database queries
"""

# Method made to create a pretend request
def assemble_data(company,date,date_s,date_e):
    raw_data:dict = dict()
    raw_data['companies'] = company
    raw_data['date']      = date
    raw_data['date_s']    = date_s
    raw_data['date_e']    = date_e
    return raw_data

db_path = r"database\company_actions.db"
    
class TestDatabaseQueries(unittest.TestCase):
    #Template for test naming convention:
    #test_(date/date range)_(single/multiple companies)
    def test_date_single(self): 
        data = assemble_data(["Meta"],'2020-12-09',None,None)
        records = get_records(data,db_path,True)
        self.assertEqual(records,response_date_single,msg="Single company and date test.")
         
    def test_range_single(self): 
        data = assemble_data(["Amazon"],None,'2020-11-05','2020-11-06')
        records = get_records(data,db_path,False)
        self.assertEqual(records,response_range_single,msg="Single company and date range test.")
    
    def test_date_multiple(self):
        data = assemble_data(["Meta","Netflix"],'2020-12-09',None,None)
        records = get_records(data,db_path,True)
        self.assertEqual(records,response_date_multiple,msg="Single company and date test.")
    
    def test_range_multiple(self):
        data = assemble_data(["Apple","Alphabet"],None,'2017-11-06','2017-11-07')
        records = get_records(data,db_path,False)
        self.assertEqual(records,response_range_multiple,msg="Multiple companies and date range test.")
         