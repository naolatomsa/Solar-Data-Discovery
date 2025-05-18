
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def detect_outliers(data):
    outlier = {}
    for column in data.columns:
        if data[column].dtype in ['float64', 'int64']:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outlier_condition = (data[column] < lower_bound) | (data[column] > upper_bound)
            outlier[column] = data[column][outlier_condition].values
    return outlier



def plot_outliers(data, outliers):
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):  # Check if column is numeric
            plt.figure(figsize=(8, 6))
            
            # Drop missing values for the column
            column_data = data[column].dropna()
            
            if not column_data.empty:  # Ensure there's data to plot
            
                sns.boxplot(y=column_data)
                plt.title(f"Boxplot for {column}")

            if column in outliers:
                plt.show()
            else:
                print(f"Skipping column {column}: No data to plot after handling NaNs.")
                
                
def remove_outliers(data, columns=None, exclude_columns=None):
    
    # Make a copy of the original DataFrame to avoid modifying it directly
    cleaned_data = data.copy()
    
    # If no columns are specified, process all numeric columns
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns.tolist()
    
    # Exclude specified columns from processing
    if exclude_columns:
        columns = [col for col in columns if col not in exclude_columns]
    
    # Process each column
    for column in columns:
        Q1 = cleaned_data[column].quantile(0.25)  # First quartile
        Q3 = cleaned_data[column].quantile(0.75)  # Third quartile
        
        IQR = Q3 - Q1  # Interquartile range
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Clip outliers to within bounds
        cleaned_data[column] = cleaned_data[column].clip(lower_bound, upper_bound)
    
    return cleaned_data
