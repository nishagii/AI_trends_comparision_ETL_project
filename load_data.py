# Load data from CSV to PostgreSQL

import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv("chatgpt_popularity_and_internet_usage_data.csv")

# Convert the 'date' column to datetime
data["date"] = pd.to_datetime(data["date"])

# Create a connection to the PostgreSQL database
engine = create_engine("postgresql://nishagi:@localhost:5432/nishagi")

# Store DataFrame to PostgreSQL
data.to_sql("chatgpt_trends_data", engine, if_exists="replace", index=False)

print("Data inserted successfully")
