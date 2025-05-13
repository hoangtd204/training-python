import pandas as pd
import os

class SalesAnalyzer:
    def __init__(self, relative_csv_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(os.path.join(current_dir, relative_csv_path))
        self.df = pd.read_csv(full_path)

    def count_employee(self):
        department_counts = self.df['Department'].value_counts()
        department_df = department_counts.reset_index()
        department_df.columns = ['Department', 'Count']
        return department_df

    def export_filtered_data_28_4(self, filtered_df, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        export_path = os.path.abspath(os.path.join(current_dir, "../../data/processed", filename))
        filtered_df.to_csv(export_path, index=False)
        print(f"Filtered data saved to: {export_path}")


#
def filter_data_miniprj():
    analyzer = SalesAnalyzer("../../data/raw/employee_data.csv")
    filename = "filter_count.csv"
    count= analyzer.count_employee()
    analyzer.export_filtered_data_28_4(count,filename)





