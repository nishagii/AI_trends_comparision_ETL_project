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

