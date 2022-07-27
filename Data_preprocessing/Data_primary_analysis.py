import pandas as pd

db_1 = pd.read_csv(r'C:\projects\laboratory\MRI_project\Database\mri1.csv')
db_2 = pd.read_csv(r'C:\projects\laboratory\MRI_project\Database\mri2.csv')

db = pd.concat([db_1, db_2], axis=0)

