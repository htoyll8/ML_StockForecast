import requests
import pandas as pd

def fetch_stock_data(symbol, api_key):
    API_URL = "https://www.alphavantage.co/query" 
   
    data = {
        "function": "TIME_SERIES_WEEKLY",
        "symbol": symbol,
        "outputsize": "full",
        "datatype": "json",
        "apikey": api_key,
    }

    response = requests.get(API_URL, data)
    response_json = response.json()

    # Convert the data to a pandas dataframe
    # The columns in the DataFrame have the following meanings:
    # 1. open: The opening price of the stock for the week
    # 2. high: The highest price at which the stock traded during the week
    # 3. low: The lowest price at which the stock traded during the week
    # 4. close: The closing price of the stock for the week
    # 5. volume: The total number of shares of the stock that were traded during the week
    df = pd.DataFrame.from_dict(response_json['Weekly Time Series'], orient='index')

    # Convert the index to datetime
    df.index = pd.to_datetime(df.index)

    # Sort the data by date
    df.sort_index(inplace=True)

    return df

def main():
    API_KEY = "XTZ9LKGP9RPH0UNB"
    SYMBOL = "AAPL"  # replace this with the stock symbol

    df = fetch_stock_data(SYMBOL, API_KEY)

    # Save the data to a csv file for later use
    df.to_csv('stock_data.csv')

    print(df.head())  # print the first 5 rows of the dataframe

if __name__ == "__main__":
    main()
