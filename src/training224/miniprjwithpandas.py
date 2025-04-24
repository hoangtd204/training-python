import pandas as pd
import os

class SalesAnalyzer:
    def __init__(self, relative_csv_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(os.path.join(current_dir, relative_csv_path))
        self.df = pd.read_csv(full_path, parse_dates=['date'])
    #caculating total revenue
    def total_revenue(self):
        return self.df['revenue'].sum()


    def filter_high_revenue(self, threshold=900):
        return self.df[self.df['revenue'] > threshold]

    def export_filtered_data(self, filtered_df, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        export_path = os.path.abspath(os.path.join(current_dir, "../../data/processed", filename))
        filtered_df.to_csv(export_path, index=False)
        print(f"Filtered data saved to: {export_path}")


#
def filter_data():
    analyzer = SalesAnalyzer("../../data/raw/sales_data_mini.csv")
    filename = "filter_sales_data.csv"
    total = analyzer.total_revenue()
    print("Total revenue:", total)

    high_revenue_df = analyzer.filter_high_revenue()
    print("Filtered data (revenue > 900):")
    print(high_revenue_df)
    analyzer.export_filtered_data(high_revenue_df,filename)



