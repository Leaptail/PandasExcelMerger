import pandas as pd
import os

path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Stockdataset"
output_path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Stockdataset"

files = os.listdir(path)
files_csv = [f for f in files if f[-3:] == 'csv']

for f in files_csv:
    filextention = '.xlsx'
    DataName = os.path.splitext(f)[0] + filextention
    Stock_data = pd.read_csv(os.path.join(path,f))
    Stock_data.to_excel(os.path.join(output_path,DataName), index=None, header=True)
