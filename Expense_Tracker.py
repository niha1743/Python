# Personal Expense Tracker – Python + CSV + Pandas
import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

file_name = 'expenses.csv'

# Ensure the CSV file exists
def init_file():
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount'])

def add_expense(date, category, amount):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

def summarize_expenses():
    df = pd.read_csv(file_name)
    print(df.groupby('Category')['Amount'].sum())
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.resample('M')['Amount'].sum().plot(kind='bar')
    plt.title("Monthly Expenses")
    plt.ylabel("Amount")
    plt.show()

# Example usage
init_file()
add_expense(datetime.today().strftime('%Y-%m-%d'), 'Food', 150)
summarize_expenses()