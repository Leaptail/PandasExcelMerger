import pandas as pd
import os

path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Stockdataset"
output_path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Stockdataset"

files = os.listdir(path)
files_csv = [f for f in files if f[-3:] == 'csv']
x = ['1.xlsx','2.xlsx']
y = 0

for f in files_csv:
    Stock_data = pd.read_csv(os.path.join(path,f))
    Stock_data.to_excel(os.path.join(output_path,x[y]), index=None, header=True)
    y = y + 1