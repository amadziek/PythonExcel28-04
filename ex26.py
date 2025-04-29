import pandas as pd

df=pd.DataFrame({
    "Imię": ["Anna", "tomek", "jan", "Anna", "Jan"],
    "Miasto": ["Krakow", "Warszawa", "Gdansk", "Kraków", "Gdańsk"],
    "Wyniki" : [88, 95, 70, 91, 60]
})

df_sorted = df.sort_values(by="Imię")
print(df_sorted.head)

# <bound method NDFrame.head of     Imię    Miasto  Wyniki
# 0   Anna    Krakow      88
# 3   Anna    Kraków      91
# 4    Jan    Gdańsk      60
# 2    jan    Gdansk      70
# 1  tomek  Warszawa      95>

df_sorted_2 = df.sort_values(by="Wyniki", ascending=False)
print(df_sorted_2.head)

# <bound method NDFrame.head of     Imię    Miasto  Wyniki
# 1  tomek  Warszawa      95
# 3   Anna    Kraków      91
# 0   Anna    Krakow      88
# 2    jan    Gdansk      70
# 4    Jan    Gdańsk      60>

df_sorted3 = df.sort_values(by=["Miasto","Wyniki"], ascending=[True, False])
print(df_sorted3)

#     Imię    Miasto  Wyniki
# 2    jan    Gdansk      70
# 4    Jan    Gdańsk      60
# 0   Anna    Krakow      88
# 3   Anna    Kraków      91
# 1  tomek  Warszawa      95
print("!!!!!!!!!!")
df_grouped = df.groupby("Imię", as_index=False)["Wyniki"].mean()
print(df_grouped)
#     Imię  Wyniki
# 0   Anna    89.5
# 1    Jan    60.0
# 2    jan    70.0
# 3  tomek    95.0
# df_sum = df.groupby("Imię", as)


print("!!!!!!!!!!")
df_sum = df.groupby("Imię", as_index=False)["Wyniki"].sum()
print(df_sum)
#     Imię  Wyniki
# 0   Anna     179
# 1    Jan      60
# 2    jan      70
# 3  tomek      95

df_count = df.groupby("Imię").size().reset_index(name="Ilośc wpisow")
print(df_count)

#     Imię  Ilośc wpisow
# 0   Anna             2
# 1    Jan             1
# 2    jan             1
# 3  tomek             1

with pd.ExcelWriter("raport.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Oryginalne", index=False)
    df_sorted.to_excel(writer, sheet_name="Posortowane", index=False)
    df_grouped.to_excel(writer, sheet_name="Średnie", index=False)