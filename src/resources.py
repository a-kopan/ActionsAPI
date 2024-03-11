from .db_interactions import get_records


wrong_arg_message:dict = dict(
    cod=404,
    message = "Wrong arguments provided. For more info..."
)
no_data_message:dict = dict(
    cod=404,
    message = "There is no existing record for the date provided"
)

company_names:list = ["Apple", "Alphabet", "Amazon", "Netflix", "Meta"]
help_message:dict = dict(
    cod = 200,
    data = dict(
    Company = "Folder for list of companies, separated by &",
    Day = "Singular day",
    Days ="Range of days",
    Companies_args = company_names,
    Templates = [
        "URL/companies/<companies>?date=12-12-2012>",
        "URL/companies/<companies>?date_start=...&date_finish=..."
    ]
    )
)

#Get and verify if the url is correct, otherwise rise an exception
#When an exception is raised, the main will return wrong args message
def filter_data(data:dict,db_path:str) -> list:
    #Check if all companies are intact.
    #If any is wrong, return wrong message
    for company in data['companies']:
        if not company in company_names:
            raise Exception("Wrong arguments.")

    #If a singular date was provided, return it no matter
    #if the range of dates was provided aswell
    if data['date']:
        rows = get_records(data,db_path=db_path,single_day=True)
    elif data['date_s'] and data['date_e']:
        rows = get_records(data,db_path=db_path,single_day=False)
    else: raise Exception
    
    return rows

def format_responses(response:list[tuple]) -> dict:
    #Check if every company has an empty list. If so, return no data message
    is_empty = True
    for comp in response: 
        if comp[1]: 
            is_empty = False
            break    
    if not response or is_empty: raise ValueError
    
    final_data = []
    for (company_name,rows) in response:
        company_data = dict(
            company=company_name,
            cod=200,
            data=[]
        )
        for row in rows:
            temp_date_data = dict(
                Date=row[0],
                Open=row[1],
                High=row[2],
                Low=row[3],
                Close=row[4],
                Adj_Close=row[5],
                Volume=row[6],
            )
            company_data['data'].append(temp_date_data)
        final_data.append(company_data)
    return final_data 