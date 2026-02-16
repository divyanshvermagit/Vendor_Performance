# 📊 Vendor Performance Analysis

## 📌 Project Overview
This project analyzes vendor performance, inventory efficiency, and sales trends to help businesses optimize profitability in retail and wholesale operations. The analysis focuses on identifying cost inefficiencies, improving vendor selection, and optimizing inventory management using data-driven insights.

The project uses multiple datasets related to sales, inventory, and vendor transactions to uncover patterns in purchasing behavior, pricing strategies, and vendor contributions to overall business performance.

---

## 🎯 Business Problem
Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies must ensure they are not incurring losses due to inefficient pricing, poor inventory turnover, or over-dependence on specific vendors.

This analysis aims to:

- Identify underperforming brands that require promotional or pricing adjustments.
- Determine top vendors contributing to sales and gross profit.
- Analyze the impact of bulk purchasing on unit costs.
- Assess inventory turnover to reduce holding costs and improve efficiency.
- Investigate profitability differences between high-performing and low-performing vendors.

---

## 🗂️ Dataset Information

The project uses **6 relational tables**:

| Table Name | Description |
|---|---|
| **Sales** | Contains sales transactions and revenue data |
| **Begin Inventory** | Opening inventory levels for products |
| **End Inventory** | Closing inventory levels for products |
| **Vendor Invoice** | Vendor billing and transaction details |
| **Purchase** | Purchase transactions from vendors |
| **Purchase Price** | Pricing details for products purchased from vendors |

These datasets enable end-to-end analysis of procurement, inventory flow, and vendor performance.

---

## 🔍 Key Analysis Performed

- Vendor contribution to total sales and profit
- Gross profit analysis by vendor and brand
- Bulk purchase impact on unit pricing
- Inventory turnover analysis
- Cost and pricing efficiency evaluation
- Performance comparison across vendors

---

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy)
- SQL (SQLite)
- Data Visualization (Matplotlib, Seaborn)
- Jupyter Notebook
- Power BI (KPI & Dashboarding)
---

## 📈 Key Insights

- Identified high-performing vendors contributing the most revenue.
- Detected underperforming brands with low sales performance.
- Found cost advantages associated with bulk purchasing.
- Evaluated inventory turnover to identify inefficiencies.
- Highlighted vendor dependency risks.

---

## 🚀 Project Structure

```
Vendor_Performance/
│
├── data/            # Raw datasets and files
├── notebooks/       # Jupyter notebooks for analysis
├── scripts/         # Data ingestion and processing scripts
├── inventory.db     # SQLite database
└── README.md
```

