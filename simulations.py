import datetime
import json
import random

from synchrony import get_next_purchase_item

with open('test_products.json') as data_file:
    products = json.load(data_file)

with open('all_synchrony_data.json') as synchrony_file:
    categories = json.load(synchrony_file)

def base_case(options):
    cum_revenue = []
    dates = []

    end_date = datetime.datetime.utcnow() + datetime.timedelta(days=options['num_years'] * 365)

    while len(dates) == 0 or dates[-1] < end_date:
        random_category = random.choice(list(products.keys()))
        cum_revenue.append((0 if len(cum_revenue) == 0 else cum_revenue[-1]) + products[random_category])
        dates.append(datetime.datetime.utcnow() if len(dates) == 0 else datetime.timedelta(days=7) + dates[-1])

    return dates, cum_revenue

def pred_case(options):
    cum_revenue = []
    dates = []

    end_date = datetime.datetime.utcnow() + datetime.timedelta(days=options['num_years'] * 365)

    while len(dates) == 0 or dates[-1] < end_date:
        synchrony_prediction = categories[str(random.randrange(100000, 105000))]

        random_category = synchrony_prediction['probability'] < options['baseline'] * 100

        category = synchrony_prediction['categoryName'] if random_category else random.choice(list(products.keys()))
        accepted = False if random_category else random.uniform(0, 1) < options['acceptance_rate']

        cum_revenue.append((0 if len(cum_revenue) == 0 else cum_revenue[-1]) + (products[category] * (1 - (options['coupon_rate'] if accepted else 0))))
        dates.append(datetime.datetime.utcnow() if len(dates) == 0 else datetime.timedelta(days=(options['acceptance_period'] if accepted else 7)) + dates[-1])

    return dates, cum_revenue
