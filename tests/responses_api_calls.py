import json

"""
File which holds predicted responses of api calls test
Used for assertions (equality comparison)
"""

response_single_date = json.loads(
    """[
    {
        "cod": 200,
        "company": "Apple",
        "data": [
            {
                "Adj_Close": 163.244141,
                "Close": 165.320007,
                "Date": "2021-12-06",
                "High": 167.880005,
                "Low": 164.279999,
                "Open": 164.289993,
                "Volume": 107497000
            }
        ]
    }
]"""
)

response_single_range = json.loads(
    """[
    {
        "cod": 200,
        "company": "Apple",
        "data": [
            {
                "Adj_Close": 163.244141,
                "Close": 165.320007,
                "Date": "2021-12-06",
                "High": 167.880005,
                "Low": 164.279999,
                "Open": 164.289993,
                "Volume": 107497000
            },
            {
                "Adj_Close": 169.030533,
                "Close": 171.179993,
                "Date": "2021-12-07",
                "High": 171.580002,
                "Low": 168.339996,
                "Open": 169.080002,
                "Volume": 120405400
            },
            {
                "Adj_Close": 172.881577,
                "Close": 175.080002,
                "Date": "2021-12-08",
                "High": 175.960007,
                "Low": 170.699997,
                "Open": 172.130005,
                "Volume": 116998900
            }
        ]
    }
]"""
)

response_multi_date = json.loads(
    """[
    {
        "cod": 200,
        "company": "Apple",
        "data": [
            {
                "Adj_Close": 163.244141,
                "Close": 165.320007,
                "Date": "2021-12-06",
                "High": 167.880005,
                "Low": 164.279999,
                "Open": 164.289993,
                "Volume": 107497000
            }
        ]
    },
    {
        "cod": 200,
        "company": "Amazon",
        "data": [
            {
                "Adj_Close": 171.3685,
                "Close": 171.3685,
                "Date": "2021-12-06",
                "High": 173.695496,
                "Low": 166.934494,
                "Open": 169.649994,
                "Volume": 68860000
            }
        ]
    }
]"""
)

response_multi_range = json.loads(
    """[
    {
        "cod": 200,
        "company": "Apple",
        "data": [
            {
                "Adj_Close": 121.447418,
                "Close": 123.75,
                "Date": "2020-12-07",
                "High": 124.57,
                "Low": 122.25,
                "Open": 122.309998,
                "Volume": 86712000
            },
            {
                "Adj_Close": 122.065697,
                "Close": 124.379997,
                "Date": "2020-12-08",
                "High": 124.980003,
                "Low": 123.089996,
                "Open": 124.370003,
                "Volume": 82225500
            },
            {
                "Adj_Close": 119.514069,
                "Close": 121.779999,
                "Date": "2020-12-09",
                "High": 125.949997,
                "Low": 121,
                "Open": 124.529999,
                "Volume": 115089200
            }
        ]
    },
    {
        "cod": 200,
        "company": "Alphabet",
        "data": [
            {
                "Adj_Close": 90.973999,
                "Close": 90.973999,
                "Date": "2020-12-07",
                "High": 91.6185,
                "Low": 90.289001,
                "Open": 90.949997,
                "Volume": 26418000
            },
            {
                "Adj_Close": 90.927498,
                "Close": 90.927498,
                "Date": "2020-12-08",
                "High": 91.095001,
                "Low": 89.810249,
                "Open": 90.504997,
                "Volume": 21926000
            },
            {
                "Adj_Close": 89.206497,
                "Close": 89.206497,
                "Date": "2020-12-09",
                "High": 91.713501,
                "Low": 88.390503,
                "Open": 90.600502,
                "Volume": 30152000
            }
        ]
    }
]"""
)

response_multi_both = json.loads(
    """[
    {
        "cod": 200,
        "company": "Meta",
        "data": [
            {
                "Adj_Close": 317.533081,
                "Close": 317.869995,
                "Date": "2021-12-06",
                "High": 320.100006,
                "Low": 306.339996,
                "Open": 308.130005,
                "Volume": 21758300
            }
        ]
    },
    {
        "cod": 200,
        "company": "Netflix",
        "data": [
            {
                "Adj_Close": 612.690002,
                "Close": 612.690002,
                "Date": "2021-12-06",
                "High": 617.289978,
                "Low": 601,
                "Open": 606.01001,
                "Volume": 3075700
            }
        ]
    }
]"""
)

response_wrong_arg = json.loads(
    """{
    "cod": 404,
    "message": "Wrong arguments provided. For more info..."
}"""
)

response_no_data = json.loads(
    """{
    "cod": 404,
    "message": "There is no existing record for the date provided"
}"""
)
