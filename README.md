# Revenue & Sales Operations Intelligence

**End-to-End Sales Performance Analytics | NexaCloud (Synthetic Business Case Study)**

A sales operations analytics project built around a fictional B2B SaaS company. This project demonstrates how raw CRM-style data can be transformed into actionable management insights using Python, Excel Power Query, PivotTables, PivotCharts, and an interactive sales performance dashboard.

The central business question: **Where is revenue coming from, how effectively is the sales team converting opportunities, and are representatives achieving their targets?**

## Executive Summary

| Business KPI | Result |
|---|---:|
| Total opportunities | 3,000 |
| Won opportunities | 907 |
| Lost opportunities | 1,067 |
| Open opportunities | 1,026 |
| Closed opportunity win rate | 45.95% |
| Won revenue | ₹34,34,97,000 |
| Target achievement | 106.02% |

**Key takeaway:** The simulated business achieves 106.02% of its aggregate sales target. However, differences across regions, products, and sales representatives provide opportunities for deeper performance investigation.

> **Data disclosure:** NexaCloud is a fictional business case study. All datasets, financial values, targets, and findings are synthetic and do not represent an actual company's performance.

## 1. Business Problem

Sales operations teams need reliable visibility into their sales pipeline, revenue contribution, regional performance, product performance, and representative-level target achievement.

When information is spread across multiple CRM exports and spreadsheets, management may struggle to:

- Monitor opportunity conversion and pipeline outcomes.
- Identify high-performing and underperforming regions.
- Understand which products contribute most to revenue.
- Compare individual sales representative performance.
- Track actual revenue against assigned targets.
- Convert raw sales data into actionable business insights.

**Project objective:** Build a centralized, interactive sales performance dashboard that consolidates these metrics and supports data-driven sales operations decisions.

## 2. Dataset Overview

The project uses five synthetic datasets generated to represent a B2B SaaS sales environment.

| Dataset | Records | Business purpose |
|---|---:|---|
| Customers | 500 | Customer-level attributes and segmentation |
| Products | 6 | Product catalog and product reference data |
| Sales Representatives | 20 | Sales team reference information |
| Opportunities | 3,000 | Pipeline stages, deal values, and outcomes |
| Sales Activities | 10,482 | Activities associated with the sales process |
| **Total records** | **13,008** | **Combined dataset records** |

Opportunity distribution:

| Opportunity Status | Records |
|---|---:|
| Won | 907 |
| Lost | 1,067 |
| Open | 1,026 |
| **Total** | **3,000** |

## 3. Tools and Methodology

| Tool | Application |
|---|---|
| Python | Synthetic dataset generation and validation |
| Microsoft Excel | Data analysis and dashboard development |
| Excel Power Query | Data import, cleaning, transformation, and preparation |
| Excel PivotTables | Aggregation and multidimensional analysis |
| Excel PivotCharts | Visual representation of sales performance |
| Excel Formulas | KPI calculations and business insights |
| Excel Slicers | Interactive regional filtering |
| Git & GitHub | Version control and project documentation |

### Analytical workflow

1. **Data generation:** Created five synthetic datasets representing customers, products, sales representatives, opportunities, and sales activities.
2. **Data preparation:** Imported datasets into Excel Power Query and performed data cleaning and transformation.
3. **Data analysis:** Used PivotTables to analyze regional revenue, product contribution, opportunity outcomes, and representative performance.
4. **KPI development:** Calculated sales KPIs, closed opportunity win rate, won revenue, and target achievement.
5. **Dashboard development:** Combined KPI cards, PivotCharts, and interactive slicers into a management dashboard.
6. **Business interpretation:** Translated analytical results into findings and recommended sales operations actions.

## 4. Dashboard and Visual Analysis

The interactive Excel dashboard consolidates sales performance across multiple business dimensions.

### 4.1 Complete Dashboard Overview

![Complete Dashboard Overview](screenshots/NexaCloud_Complete_Dashboard_Overview.png)

The complete dashboard provides a consolidated view of sales performance, combining key KPIs, revenue analysis, win-rate comparisons, representative rankings, and business insights.

### 4.2 KPI Summary, Revenue Contribution and Business Insights

![KPIs Revenue and Business Insights](screenshots/NexaCloud_Dashboard_KPIs_Revenue_Insights.png)

This section highlights:
- Total opportunities and won opportunities.
- Closed opportunity win rate.
- Won revenue and target achievement.
- Revenue contribution across regions and products.
- Dynamically linked business performance insights.

### 4.3 Win Rate and Sales Representative Performance

![Win Rate and Sales Representative Performance](screenshots/NexaCloud_Dashboard_WinRate_SalesRep.png)

This section examines:
- Regional win-rate comparison.
- Product-level win-rate comparison.
- Top 10 representatives by won revenue.
- Individual sales representative target achievement.

### Interactive Dashboard Feature

The dashboard includes a **Sales Rep Region slicer**, allowing users to filter the dashboard by region and explore how sales performance changes across different geographical segments.

## 5. Key Business Findings

### 5.1 Regional Revenue Performance

The South region contributes the highest won revenue, at approximately **₹91.3 million**.

**Business interpretation:** Regional revenue concentration provides an opportunity to investigate successful sales practices and understand differences in opportunity mix across regions.

### 5.2 Product Revenue Contribution

**Security Suite** is the highest revenue-contributing product, generating approximately **₹82.1 million** in won revenue.

**Business interpretation:** Product-level revenue visibility helps management understand which offerings contribute most to overall sales performance.

### 5.3 Opportunity Conversion Performance

The closed opportunity win rate is **45.95%**.

Win rate is calculated as:

**Won Opportunities ÷ (Won Opportunities + Lost Opportunities) × 100**

Open opportunities are excluded from the closed opportunity win-rate calculation.

**Business interpretation:** The remaining lost opportunities provide an area for further investigation into conversion performance and potential sales process improvements.

### 5.4 Sales Target Achievement

The dashboard reports aggregate target achievement of **106.02%**.

**Business interpretation:** Overall simulated sales performance exceeds the modeled target. Representative-level analysis is useful for identifying differences in individual achievement.

## 6. Recommended Business Actions

| Area | Recommended action | Business objective |
|---|---|---|
| Regional performance | Investigate revenue contribution and conversion differences across regions | Identify opportunities for regional improvement |
| Product performance | Compare product revenue, opportunity volume, and win rates | Understand product-level sales effectiveness |
| Pipeline management | Analyze lost opportunities and open pipeline distribution | Improve pipeline visibility and conversion |
| Sales representative performance | Review target achievement and won revenue by representative | Identify coaching and performance improvement opportunities |
| Sales operations reporting | Maintain a consistent KPI dashboard and periodic reporting process | Improve management visibility and decision-making |

These recommendations are proposed actions based on the descriptive findings. They have not been independently tested for business impact.

## 7. KPI Definitions

| KPI | Calculation |
|---|---|
| Total Opportunities | Count of all opportunity records |
| Won Opportunities | Count of opportunities with Won status |
| Lost Opportunities | Count of opportunities with Lost status |
| Open Opportunities | Count of opportunities with Open status |
| Closed Opportunity Win Rate | Won ÷ (Won + Lost) × 100 |
| Won Revenue | Sum of deal values for Won opportunities |
| Target Achievement | Actual Won Revenue ÷ Sales Target × 100 |

All financial metrics are based on the synthetic NexaCloud dataset.

## 8. Repository Structure

The following are the confirmed dashboard and screenshot paths referenced by this project:

```text
revenue-sales-operations-intelligence/
│
├── excel_dashboard/
│   └── NexaCloud_PowerQuery_Workbook.xlsx
│
├── screenshots/
│   ├── NexaCloud_Complete_Dashboard_Overview.png
│   ├── NexaCloud_Dashboard_KPIs_Revenue_Insights.png
│   └── NexaCloud_Dashboard_WinRate_SalesRep.png
│
└── README.md
```

The project also uses five synthetic CSV datasets and Python generation/validation scripts. Their exact directory and file names should be reflected in this tree when the complete repository contents are verified.

## 9. How to Explore the Project

1. Open the `excel_dashboard` folder.
2. Download `NexaCloud_PowerQuery_Workbook.xlsx`.
3. Open the workbook using desktop Microsoft Excel.
4. Navigate to the **Sales_Dashboard** worksheet.
5. Review the KPI cards, revenue charts, win-rate comparisons, and representative performance.
6. Use the **Sales Rep Region** slicer to explore regional performance.
7. Review the business insights generated from the dashboard.

**Important:** Excel may display warnings about external data connections. Review the source paths and connections before refreshing or enabling them. The dashboard can be inspected without enabling untrusted connections.

## 10. Project Limitations

- NexaCloud is a fictional company; results are simulated.
- The dataset is designed for portfolio demonstration rather than real-world financial reporting.
- The dashboard describes observed patterns within the generated dataset and does not establish causal relationships.
- Target achievement is based on modeled sales targets.
- The analysis does not independently validate the effectiveness of the recommended business actions.
- Results should not be interpreted as actual company revenue or sales performance.

## 11. Skills Demonstrated

**Business & Operations:** Sales Operations Analytics, Business Performance Reporting, KPI Development, Pipeline Analysis, Revenue Analysis, Target Achievement Monitoring, Business Insights.

**Data & Technical:** Python, Excel Power Query, PivotTables, PivotCharts, Excel Formulas, Data Cleaning, Data Validation, Interactive Dashboards, Git, GitHub.

---

**Project Type:** Business Analytics | Sales Operations | Management Reporting

**Case Study:** NexaCloud – Synthetic B2B SaaS Sales Environment
