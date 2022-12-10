import pandas as pd
import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

headers = {
	"X-RapidAPI-Key": "734e4c39c1msheb017ea994fcef2p1b45d4jsn458c4b8f2005",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# create a function that uses response.text to create a dataframe
def get_stock_prices(response):
	# convert the response.text to a dictionary
	response_dict = eval(response.text)
	# get the time series data
	time_series = response_dict['Time Series (5min)']
	# create a dataframe from the time series data
	df = pd.DataFrame.from_dict(time_series, orient='index')
	#print (df)
	print(df.head())

#call the get_stock_prices function
get_stock_prices(response)

# create a main function that takes a stock symbol as an argument
def main(symbol):
	# create the querystring
	querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":symbol,"datatype":"json","output_size":"compact"}
	# create the headers
	headers = {
		"X-RapidAPI-Key": "734e4c39c1msheb017ea994fcef2p1b45d4jsn458c4b8f2005",
		"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
	}
	# create the response
	response = requests.request("GET", url, headers=headers, params=querystring)
	# call the get_stock_prices function
	df = get_stock_prices(response)
	# call the plot_stock_prices function
	plot_stock_prices(df)
	