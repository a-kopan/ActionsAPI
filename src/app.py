from flask import Flask, request, jsonify
import flask_methods as fm

app = Flask(__name__)


@app.route("/")
def show_options():
    return fm.help_message

@app.route("/company_list/<company_list>")
def get_companies(company_list):
    fm.get_attributes(company_list)
    
if __name__=="__main__":
    app.run(debug=True)