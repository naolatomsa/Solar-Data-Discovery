import matplotlib.pyplot as plt

def plot_sensor_readings(data, timestamp_col='Timestamp', cleaning_col='Cleaning', mod_a_col='ModA', mod_b_col='ModB'):

    # Separate data into cleaned and uncleaned periods
    cleaned = data[data[cleaning_col] == 1]
    not_cleaned = data[data[cleaning_col] == 0]

    # Plot sensor readings
    plt.figure(figsize=(12, 6))
    plt.plot(cleaned[timestamp_col], cleaned[mod_a_col], label=f'{mod_a_col} (Cleaned)', alpha=0.7)
    plt.plot(cleaned[timestamp_col], cleaned[mod_b_col], label=f'{mod_b_col} (Cleaned)', alpha=0.7)
    plt.plot(not_cleaned[timestamp_col], not_cleaned[mod_a_col], label=f'{mod_a_col} (Not Cleaned)', linestyle='--', alpha=0.7)
    plt.plot(not_cleaned[timestamp_col], not_cleaned[mod_b_col], label=f'{mod_b_col} (Not Cleaned)', linestyle='--', alpha=0.7)

    # Customize the plot
    plt.title('Sensor Readings Before and After Cleaning', fontsize=14)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Sensor Values', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


## compare and anomolies 


def detect_and_plot_anomalies(data, value_col, timestamp_col, threshold_percentile=0.95):

    # Calculate the threshold value
    threshold = data[value_col].quantile(threshold_percentile)
    
    # Identify anomalies
    anomalies = data[data[value_col] > threshold]

    # Plot data and anomalies
    plt.figure(figsize=(10, 6))
    plt.plot(data[timestamp_col], data[value_col], label=value_col)
    plt.scatter(anomalies[timestamp_col], anomalies[value_col], color='red', label='Anomalies')
    plt.title(f'{value_col} Over Time with Anomalies Highlighted')
    plt.xlabel('Time')
    plt.ylabel(value_col)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    return anomalies