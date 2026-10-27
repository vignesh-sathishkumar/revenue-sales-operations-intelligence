# KPI Definition Plan (draft)

| KPI | Proposed definition | Notes |
|---|---|---|
| Closed-won revenue | Sum of opportunity amount where stage = Closed Won | Recognition differs from booked sales; treat as bookings |
| Win rate | Closed-won opportunities / (Closed Won + Closed Lost opportunities) | Exclude open opportunities |
| Average deal size | Closed-won amount / count of closed-won opportunities | Avoid divide-by-zero |
| Sales cycle | Average days from opportunity creation to close, for closed deals | Compare won vs lost |
| Pipeline value | Sum of amount for open opportunities | As-of-date convention needed |
| Weighted pipeline | Sum of open opportunity amount x probability | Probability assumptions documented |
| Forecast accuracy | 1 - absolute(forecast - actual) / actual | Handle zero actual separately |
| Activity-to-win relationship | Compare activity counts by won/lost outcomes | Correlation is not causation |

**Important:** Definitions will be finalized before dashboard development; date logic must avoid mixing historical and current snapshots.
