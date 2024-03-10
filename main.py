from flask import Flask, request, jsonify
import src.resources as rc

app = Flask(__name__)


@app.route("/")
def show_help():
    return jsonify(rc.help_message)

#filter should raise wrong arg exception
#after that wrong_arg_message and id should be sent

#URL/companies/<companies>?date=12-12-2012>
#URL/companies/<companies>?date_start=...&date_finish=...
@app.route("/companies/<company>")
def get_company(company):
    #db_path = str(Path(__file__).parent / "database/company_actions.db")
    db_path = r"database\company_actions.db"
    #raw_data holds all potential arguments
    #For not provided arguments holds None
    raw_data:dict = dict()
    raw_data['companies'] = company.split('&')
    raw_data['date']      = request.args.get('date',None)
    raw_data['date_s']    = request.args.get('date_s',None)
    raw_data['date_e']    = request.args.get('date_e',None)
    
    #Try to get the right format of the data
    try: 
        rows = rc.filter_data(raw_data,db_path)
        rows = rc.format_responses(rows)
    #If the arguments were provided in a wrong way
    #return an error message
    except ValueError: return jsonify(rc.no_data_message)
    except Exception: return jsonify(rc.wrong_arg_message)
    #If the data was correctly input the data is returned
    else: return jsonify(rows)
    
if __name__=="__main__":
    app.run(debug=True) 