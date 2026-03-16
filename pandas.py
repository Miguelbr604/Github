import pandas as pd
df = pd.read_excel("C:/Users/MIGUEL/Downloads/default_of_credit_card_clients__courseware_version_1_21_19.xls")
print(df.shape)
print(df.shape[0])
print(df.columns)
print(df.describe())
print(df.isnull().sum())


