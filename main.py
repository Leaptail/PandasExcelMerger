import pandas as pd
import os

path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Merge"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']

#code to read excel files from pandas
df_list = []
for f in files_xlsx:
    data = pd.read_excel(os.path.join(path,f))
    df_list.append(data)
df = pd.concat(df_list)

output_path = "D:\Programming\github py\Pandas Programming\PandasExcelMerger\Mergedexcel.xlsx"
df.to_excel(output_path, index=False)