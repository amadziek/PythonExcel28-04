import pandas as pd
# import xlsxwriter as qwe


# pip install pandas
# pip install xlsxwriter

# tylko do tworzenia nowych plików
#dośc szybka
# tylko xlsx

writer = pd.ExcelWriter('empty_file.xlsx')
empty_dataframe = pd.DataFrame()
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()
