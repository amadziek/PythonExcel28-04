import pandas as pd

df = pd.read_excel('excel_with_multiple_sheets-1.xlsx')
print(df)

suma = df['Height'].sum(skipna=False) # omin barkujace
print("Suma:", suma)