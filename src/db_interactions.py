import sqlite3

"""
Based on single_day variable fetches records from db
"""


# yyyy-mm-dd
# Assembles the query based on the single_day flag
def assemble_query(data: dict, single_day: bool, company: str) -> str:
    if single_day:  # SQLite query for a single date
        query = f"""
        SELECT *
        FROM {company}
        WHERE Date
        = \"{data['date']}\";"""
    else:  # SQLite query for a range of dates
        query = f"""
        SELECT *
        FROM {company}
        WHERE Date
        BETWEEN \'{data['date_s']}\'
        AND \'{data['date_e']}\';"""
    return query


# Fetches the records from db
def get_records(data: dict, db_path: str, single_day: bool) -> list:
    # cursor and connection to the database
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    response = []
    for company in data["companies"]:
        # Assembling and executing of the query
        query = assemble_query(data, single_day, company)
        rows = cur.execute(query).fetchall()
        response.append((company, rows))
    return response
