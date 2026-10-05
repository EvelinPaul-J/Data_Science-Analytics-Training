import pandas as pd
def analyze_sales_data(raw_records):
    df=pd.DataFrame(raw_records)
    df=df.drop_duplicates()
    df["price"]=df["price"].fillna(df["price"].mean())
    df["revenue"]=df["price"]*df["quantity"]
    result=df.groupby("category")["revenue"].agg(["sum","mean"]).reset_index()
    result=result.rename(columns={"sum":"total_revenue","mean":"avg_revenue"})
    return result.to_dict("records")
sample_sales=[
    {"txn_id":"T1","category":"Electronics","price":1000.0,"quantity":2},
    {"txn_id":"T2","category":"Furniture","price":300.0,"quantity":1},
    {"txn_id":"T3","category":"Electronics","price":None,"quantity":1},
    {"txn_id":"T1","category":"Electronics","price":1000.0,"quantity":2}
]
print(analyze_sales_data(sample_sales))