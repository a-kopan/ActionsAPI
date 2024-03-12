# ActionsAPI

An Flask-made API, which returns data about target companies actions.

## About

The application uses SQLite3 database to hold the data about each company.

Based on a provided date and list of companies, returns a json with information on that action.

## Installation

```bash
pip install requirements.txt
```

Just an instalation of requirements.txt file.

If prefered, that can be done in a [virtual enviroment](https://docs.python.org/3/library/venv.html).

## Usage

Starting the application with Flask:

```bash
Flask --app <path>\src\main.py run
```

Or

```bash
python -m Flask --app <path>\src\main.py run
```

If something went wrong and errors appeard, feel free to use the [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/).

In the command line in which the application started there is the ip along with port with which the api can be accessed.

## Endpoints

#### http://127.0.0.1:5000/company_list?date

The API structure allows to send a single request for data about multiple companies.

In the case of sending for multiple companies, just provide them separated by '&' sign.

It is also allowed to send data about either a single date or range of days (both boundaries included).

API only allows GET methods.

You can also send the request to the / folder (typically http://127.0.0.1:5000/) for a help message.

Company list:

* Alphabet
* Amazon
* Apple
* Meta
* Netflix

Keywords:

* date - specify a date from which to take the data from (yyyy-mm-dd)
* date_s - specify a start of the date range.
* date_e - specify an end of the data range.

### Remarks

* If date keyword is present, date_s and date_e will not be considered.
* The database doesn't have the data on weekends (each saturday and sunday)
* The date range has to be in a correct order - date_s comes before date_e (time-wise).
* Single-digit numbers have to have leading 0's.

### Example URLs

* /Apple?date="2020-12-09" (leading 0 case)
* /Apple&Alphabet?date_s=2020-12-07&date_e=2020-12-09 (multiple companies date range)

## Response data

In each response there are 2 fields:

##### cod - holds response code

##### data - holds data about action from each day

* Adj_Close
* Close
* Date
* High
* Low
* Open
* Volume

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
