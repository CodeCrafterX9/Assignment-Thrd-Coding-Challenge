# Assignment-Thrd-Coding-Challenge
This repository contains a solution for the Thrd Coding Challenge, implemented using a Jupyter Notebook (`Assignment.ipynb`). The goal is to dynamically adjust product prices based on inventory and recent sales using well-defined business rules.

---

## Files in This Repo

| File Name             | Description                                  |
|-----------------------|----------------------------------------------|
| `Assignment.ipynb`    | Jupyter notebook with the full implementation of the pricing engine logic. |
| `products.csv`        | Contains the product catalog with current prices, cost, and stock. |
| `sales.csv`           | Contains 30-day sales data per product.      |
| `updated_prices.csv`  | Final output file with updated product prices (with currency units). |

---

## Problem Statement (Summary)

Given a list of products and their recent sales data:
- Adjust prices based on inventory levels and demand.
- Ensure every product still maintains a minimum 20% profit margin over cost.
- Output the final updated prices in a structured CSV file.

---

## Pricing Rules Used (In Priority Order)

### Rule 1 – Low Stock, High Demand
- **Condition:** `stock < 20` and `quantity_sold > 30`
- **Action:** Increase price by 15%

### Rule 2 – Dead Stock
- **Condition:** `stock > 200` and `quantity_sold == 0`
- **Action:** Decrease price by 30%

### Rule 3 – Overstocked Inventory
- **Condition:** `stock > 100` and `quantity_sold < 20`
- **Action:** Decrease price by 10%

### Rule 4 – Minimum Profit Constraint
- Ensures price is at least 20% above the cost price.
- If not, resets the price to `cost_price * 1.2`.

> Only the first applicable rule from Rules 1–3 is applied. Rule 4 is always applied afterward.

---

## Approach

1. **Read input files**: `products.csv` and `sales.csv` using `pandas`.
2. **Merge datasets**: Combine product info and sales data using SKU as key.
3. **Apply pricing rules**: A function processes each product row by row based on defined conditions.
4. **Format final prices**: Rounded to 2 decimals and prefixed with `$`.
5. **Export results**: Save updated data as `updated_prices.csv`.


