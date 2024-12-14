#collecting data from google trends
"""
This script collects data from Google Trends using the pytrends library and saves it to a CSV file.

Functions:
    None

Usage:
    Run the script to collect Google Trends data for specified keywords over the past 5 years.

Dependencies:
    - pytrends
    - pandas

Steps:
    1. Initialize the pytrends request object.
    2. Define the keywords and regions for the Google Trends search.
    3. Build the payload with the specified parameters.
    4. Retrieve the interest over time data.
    5. Check if data is available and save it to a CSV file if it is.
"""


from pytrends.request import TrendReq
import pandas as pd

# initialize pytrends
pytrends=TrendReq()

# define the keyword and regions
keywords = ["chatGPT", "Generative AI", "GPT-4", "Artificial Intelligence"]
geo=""
timeframe="today 5-y"

#build the payload
pytrends.build_payload(keywords,geo=geo,timeframe=timeframe)

#get interest over time
data=pytrends.interest_over_time()

#check if data available
if not data.empty:
    data.to_csv("ai_trends.csv")

else:
    print("No data available")

