import datetime
import json
import random

with open('test_products.json') as data_file:
    products = json.load(data_file)

def base_case(num_years = 1):
    cum_revenue = []
    dates = []

    end_date = datetime.datetime.utcnow() + datetime.timedelta(days=num_years * 365)

    while len(dates) == 0 or dates[-1] < end_date:
        random_category = random.choice(products.keys())
        cum_revenue.append((0 if len(cum_revenue) == 0 else cum_revenue[-1]) + products[random_category])
        dates.append(datetime.datetime.utcnow() if len(dates) == 0 else datetime.timedelta(days=7) + dates[-1])

    return dates, cum_revenue

def pred_case(num_years = 1, coupon_rate = 0.10, acceptance_rate = 0.20, acceptance_period = 3, baseline = 0.80):
    cum_revenue = []
    dates = []

    end_date = datetime.datetime.utcnow() + datetime.timedelta(days=num_years * 365)

    while len(dates) == 0 or dates[-1] < end_date:
        random_category = random.choice(products.keys())
        accepted = random.uniform(0, 1) < acceptance_rate
        cum_revenue.append((0 if len(cum_revenue) == 0 else cum_revenue[-1]) + (products[random_category] * (1 - (coupon_rate if accepted else 0))))
        dates.append(datetime.datetime.utcnow() if len(dates) == 0 else datetime.timedelta(days=(acceptance_period if accepted else 7)) + dates[-1])

    return dates, cum_revenue
