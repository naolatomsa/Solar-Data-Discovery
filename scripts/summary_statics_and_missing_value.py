import pandas as pd
def calculate_summary(data):
    return data.drop(columns='Comments').describe()

def missing_values(data):
    return data.isnull().sum()

def remove_missing_values(data, column):
    return data.drop(columns=column)


