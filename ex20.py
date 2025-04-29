import pandas as pd

df = pd.read_excel('excel_with_multiple_sheets-1.xlsx')
print(df)

print(df[df["Height"] > 175 ])
suma = df['Height'].sum(skipna=False) # omiń barkujace
print("Suma:", suma)

print(df.info)
print(df.describe)