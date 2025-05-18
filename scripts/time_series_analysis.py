import pandas as pd
import matplotlib.pyplot as plt
def check_negative_entries(data, columns):

    return data[columns][data[columns] < 0]

def replace_negative_with_zero(data, columns):

    data[columns] = data[columns].apply(lambda col: col.map(lambda x: max(x, 0)))
    return data

def validate_no_negative(data, columns):

    negative_counts = (data[columns] < 0).sum()
    return negative_counts.sum() == 0  # True if all columns have zero negative values



##series

def preprocess_timestamp(data, timestamp_col='Timestamp'):

    data[timestamp_col] = pd.to_datetime(data[timestamp_col])
    data['Month'] = data[timestamp_col].dt.month
    data['Hour'] = data[timestamp_col].dt.hour
    return data

def analyze_and_plot_monthly_trends(data, columns, timestamp_col='Timestamp'):

    # Preprocess timestamp if not already done
    if 'Month' not in data.columns:
        data = preprocess_timestamp(data, timestamp_col)

    # Group by month and calculate mean
    monthly_data = data.groupby('Month')[columns].mean()

    # Plot monthly trends
    monthly_data.plot(kind='bar', figsize=(10, 6))
    plt.title('Monthly Averages of Solar Irradiance and Temperature')
    plt.xlabel('Month')
    plt.ylabel('Values')
    plt.legend(title='Variable')
    plt.show()

def analyze_and_plot_hourly_trends(data, columns, timestamp_col='Timestamp'):
    
    # Preprocess timestamp if not already done
    if 'Hour' not in data.columns:
        data = preprocess_timestamp(data, timestamp_col)

    # Group by hour and calculate mean
    hourly_data = data.groupby('Hour')[columns].mean()

    # Plot hourly trends
    hourly_data.plot(kind='line', figsize=(10, 6))
    plt.title('Average Solar Irradiance and Temperature Throughout the Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Values')
    plt.legend(title='Variable')
    plt.show()
