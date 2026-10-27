from pathlib import Path
from datetime import date
import csv

BASE = Path(__file__).resolve().parent.parent / 'data' / 'raw'

def read(name):
    with (BASE / name).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

customers, products, reps, opps, acts = [read(x) for x in ['customers.csv','products.csv','sales_reps.csv','opportunities.csv','sales_activities.csv']]
assert len(customers) == 500
assert len(products) == 6
assert len(reps) == 20
assert len(opps) == 3000
assert len(acts) >= 8000
for rows, key in [(customers,'customer_id'),(products,'product_id'),(reps,'rep_id'),(opps,'opportunity_id'),(acts,'activity_id')]:
    assert len({r[key] for r in rows}) == len(rows), f'Duplicate {key}'
cs, ps, rs = [{r[k] for r in rows} for rows,k in [(customers,'customer_id'),(products,'product_id'),(reps,'rep_id')]]
os = {r['opportunity_id']:r for r in opps}
assert all(o['customer_id'] in cs and o['product_id'] in ps and o['rep_id'] in rs for o in opps)
assert all(a['opportunity_id'] in os and a['rep_id'] == os[a['opportunity_id']]['rep_id'] for a in acts)
assert all(o['stage'] in {'Won','Lost','Open'} for o in opps)
assert all((o['stage']=='Open') == (o['actual_close_date']=='') for o in opps)
assert all(0 <= int(o['discount_pct']) <= 20 and int(o['deal_value_inr']) > 0 for o in opps)
assert all(date(2025,1,1) <= date.fromisoformat(o['created_date']) <= date(2025,12,31) for o in opps)
assert all(date.fromisoformat(a['activity_date']) >= date.fromisoformat(os[a['opportunity_id']]['created_date']) for a in acts)
assert all(date.fromisoformat(a['activity_date']) <= date.fromisoformat(os[a['opportunity_id']]['actual_close_date']) for a in acts if os[a['opportunity_id']]['actual_close_date'])
print('PASS: row counts, unique IDs, foreign keys, dates, stage logic, and values.')
for name, rows in [('customers',customers),('products',products),('sales_reps',reps),('opportunities',opps),('sales_activities',acts)]:
    print(f'{name}: {len(rows):,} rows')
print('Won:',sum(o['stage']=='Won' for o in opps),'Lost:',sum(o['stage']=='Lost' for o in opps),'Open:',sum(o['stage']=='Open' for o in opps))
