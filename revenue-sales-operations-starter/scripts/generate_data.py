from pathlib import Path
from datetime import date, timedelta
import csv
import random

RNG = random.Random(42)
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'data' / 'raw'
OUT.mkdir(parents=True, exist_ok=True)


def save(filename, rows, columns):
    with (OUT / filename).open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    print(f'{filename}: {len(rows):,} rows')

regions = ['South', 'North', 'West', 'East']
cities = {'South': ['Chennai', 'Bengaluru', 'Hyderabad'], 'North': ['Delhi', 'Gurugram', 'Noida'], 'West': ['Mumbai', 'Pune', 'Ahmedabad'], 'East': ['Kolkata', 'Bhubaneswar', 'Guwahati']}
industries = ['Banking', 'Retail', 'Healthcare', 'Manufacturing', 'Technology', 'Logistics']
segments = ['SMB', 'Mid-Market', 'Enterprise']
customers = []
for i in range(1, 501):
    region = RNG.choice(regions)
    customers.append({'customer_id': f'C{i:04d}', 'customer_name': f'Nexa Client {i:04d}', 'industry': RNG.choice(industries), 'segment': RNG.choices(segments, weights=[50, 35, 15])[0], 'region': region, 'city': RNG.choice(cities[region])})
save('customers.csv', customers, list(customers[0]))

products = [
    {'product_id': 'P001', 'product_name': 'CRM Essentials', 'category': 'CRM', 'annual_list_price_inr': 120000},
    {'product_id': 'P002', 'product_name': 'CRM Enterprise', 'category': 'CRM', 'annual_list_price_inr': 420000},
    {'product_id': 'P003', 'product_name': 'Workflow Automate', 'category': 'Automation', 'annual_list_price_inr': 240000},
    {'product_id': 'P004', 'product_name': 'Analytics Cloud', 'category': 'Analytics', 'annual_list_price_inr': 300000},
    {'product_id': 'P005', 'product_name': 'Support Desk', 'category': 'Service', 'annual_list_price_inr': 180000},
    {'product_id': 'P006', 'product_name': 'Security Suite', 'category': 'Security', 'annual_list_price_inr': 360000},
]
save('products.csv', products, list(products[0]))

reps = []
for i in range(1, 21):
    region = regions[(i-1)//5]
    reps.append({'rep_id': f'R{i:03d}', 'rep_name': f'Sales Rep {i:02d}', 'region': region, 'team': f'{region} Sales', 'annual_target_inr': RNG.choice([12000000, 15000000, 18000000, 21000000])})
save('sales_reps.csv', reps, list(reps[0]))

start = date(2025, 1, 1)
end = date(2025, 12, 31)
opp_rows = []
activity_rows = []
activity_num = 0
for i in range(1, 3001):
    customer = RNG.choice(customers)
    product = RNG.choice(products)
    rep = RNG.choice([r for r in reps if r['region'] == customer['region']])
    created = start + timedelta(days=RNG.randint(0, 364))
    stage = RNG.choices(['Won', 'Lost', 'Open'], weights=[35, 40, 25])[0]
    sales_cycle = RNG.randint(7, 85)
    expected_close = created + timedelta(days=sales_cycle)
    # Opportunities still open at year-end have no actual close date.
    if stage != 'Open' and expected_close > end:
        stage = 'Open'
    actual_close = expected_close if stage != 'Open' else None
    units = RNG.choice([1, 1, 1, 2, 3])
    discount = RNG.choice([0, 5, 10, 15, 20])
    amount = int(product['annual_list_price_inr'] * units * (100-discount)/100)
    probability = {'Won': 100, 'Lost': 0, 'Open': RNG.choice([20, 40, 60, 80])}[stage]
    oid = f'O{i:05d}'
    opp_rows.append({'opportunity_id': oid, 'customer_id': customer['customer_id'], 'product_id': product['product_id'], 'rep_id': rep['rep_id'], 'created_date': created.isoformat(), 'expected_close_date': expected_close.isoformat(), 'actual_close_date': actual_close.isoformat() if actual_close else '', 'stage': stage, 'units': units, 'discount_pct': discount, 'deal_value_inr': amount, 'probability_pct': probability, 'lost_reason': RNG.choice(['Price', 'Competition', 'Budget', 'No decision', 'Feature gap']) if stage == 'Lost' else ''})
    # Activities occur after opportunity creation, never after a completed deal closes.
    activity_end = actual_close if actual_close else min(end, expected_close)
    days_available = max(0, (activity_end-created).days)
    for _ in range(RNG.randint(2, 5)):
        activity_num += 1
        activity_date = created + timedelta(days=RNG.randint(0, days_available))
        activity_rows.append({'activity_id': f'A{activity_num:06d}', 'opportunity_id': oid, 'rep_id': rep['rep_id'], 'activity_date': activity_date.isoformat(), 'activity_type': RNG.choice(['Call', 'Email', 'Demo', 'Meeting', 'Follow-up']), 'outcome': RNG.choice(['Completed', 'Customer responded', 'Next step scheduled'])})
save('opportunities.csv', opp_rows, list(opp_rows[0]))
save('sales_activities.csv', activity_rows, list(activity_rows[0]))
print('Done. All data is synthetic; currency INR; period 2025.')
