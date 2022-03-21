import pandas as pd
from sodapy import Socrata
def Import_VDH_COVID_Data():
    #!/usr/bin/env python
    # make sure to install these packages before running:
    # pip install pandas

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    # client = Socrata("data.virginia.gov", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.virginia.gov,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    with open('data/MyAppToken.txt', 'r') as file:
        Token = file.readline().strip('\n')
        Key_ID = file.readline().strip('\n')
        Key_Secret = file.readline().strip('\n')

    client = Socrata('data.virginia.gov', Token, username = Key_ID, password = Key_Secret)

    # First 15000 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("bre9-aqqr")

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df

def Update_VDH_COVID_Data(dates_list):
    with open('data/MyAppToken.txt', 'r') as file:
        Token = file.readline().strip('\n')
        Key_ID = file.readline().strip('\n')
        Key_Secret = file.readline().strip('\n')

    client = Socrata('data.virginia.gov', Token, username = Key_ID, password = Key_Secret)
    
    results = client.get("bre9-aqqr", report_date = dates_list[0])
    for d in dates_list[1:]:
        results += client.get("bre9-aqqr", report_date = d)
    
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df