import pandas as pd

products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")

merged_df = pd.merge(products_df, sales_df, on="sku", how="left")
merged_df["quantity_sold"] = merged_df["quantity_sold"].fillna(0).astype(int)

def apply_pricing_rules(row):
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    
    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.70
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.90
    else:
        new_price = current_price

    minimum_price = cost_price * 1.20
    if new_price < minimum_price:
        new_price = minimum_price

    return round(new_price, 2)

merged_df['new_price'] = merged_df.apply(apply_pricing_rules, axis=1)

merged_df["old_price"] = merged_df["current_price"].apply(lambda x: f"${x:.2f}")
merged_df["new_price"] = merged_df["new_price"].apply(lambda x: f"${x:.2f}")

output_df = merged_df[["sku", "old_price", "new_price"]]

output_df.to_csv("updated_prices.csv", index=False)

print("Output saved to 'updated_prices.csv'")
