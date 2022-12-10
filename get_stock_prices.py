import requests
import pandas as pd
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
    # rename the columns
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    # convert the index to a datetime object
    df.index = pd.to_datetime(df.index)
    # sort the dataframe by index
    df.sort_index(inplace=True)
    # return the dataframe
    return df

# call the function
df = get_stock_prices(response)
# print the first 5 rows
print(df.head())

# create a function that plots the results of the get_stock_prices function
def plot_stock_prices(df):
    # import the necessary libraries
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    # create a figure
    fig = plt.figure()
    # create an axis
    ax = fig.add_subplot(111)
    # plot the close price
    ax.plot(df.index, df['close'])
    # set the x axis major locator
    ax.xaxis.set_major_locator(mdates.DayLocator())
    # set the x axis major formatter
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # set the x axis minor locator
    ax.xaxis.set_minor_locator(mdates.HourLocator())
    # set the x axis minor formatter
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    # show the plot
    plt.show()

# call the function
plot_stock_prices(df)
