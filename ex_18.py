import pandas as pd

# df = pd. read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name=2)
# print(df)
#
#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67


df = pd. read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name='marks')
print(df)

#        Name  Marks
# 0    Aditya     79
# 1    Sameer     81
# 2  Dharwish     70
# 3      Joel     67

data = pd.ExcelFile('excel_with_multiple_sheets-1.xlsx')
print(data.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name=data.sheet_names[0])
print(df)
print("@@@@@@@@@@@@@@")
df = pd.read_excel('excel_with_multiple_sheets-1.xlsx', sheet_name="marks", usecols=["Name"])
print(df)

print("!!!!!!!!!!!!!!")
df = data.parse("height")
print(df.head())  # 5 pierwszych wierszy

print(df.tail()) # 5 ostatnich wierszy

print("!!!!!!!!!!!!")
print(df.columns)
print(df.columns.tolist())

