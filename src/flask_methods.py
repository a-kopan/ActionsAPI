from flask import request, jsonify

wrong_arg_message = {}

help_message = (
    """
    {
    "Company" : "For a single company",
    "Companies":"For multiple companies",
    "Day":"Singular day" 
    "Days":"Range of days"
    "Companies" = ["Apple", "Alphabet", "Amazon", "Netflix", "Meta Platform"]
    }
    """,
    200
)

def get_attributes():   
    companies_data = {}
    
    company = request.args.get('Company',None)
    companies = request.args.get('Companies',[])
    date = request.args.get('date',None)
    dates = request.args.get('dates',[])