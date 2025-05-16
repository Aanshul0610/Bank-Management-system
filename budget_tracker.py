import json
from datetime import datetime

def get_budget_data(budget_file):
    with open(budget_file, 'r') as f:
        data = json.load(f)
    return data

def get_budget_data_by_date(budget_file, date):
    data = get_budget_data(budget_file)
    total_amount = 0
    for category in data['categories']:
        for transaction in category['transactions']:
            if transaction['date'] == date:
                total_amount += transaction['amount']
    return total_amount

def get_budget_data_by_category(budget_file, category):
    data = get_budget_data(budget_file)
    for category_data in data['categories']:
        if category_data['name'].lower() == category.lower():
            return category_data['transactions']
    return []  # Return empty if not found

def get_budget_data_by_category_and_date(budget_file, category, date):
    data = get_budget_data(budget_file)
    total_amount = 0
    for category_data in data['categories']:
        if category_data['name'].lower() == category.lower():
            for transaction in category_data['transactions']:
                if transaction['date'] == date:
                    total_amount += transaction['amount']
    return total_amount
