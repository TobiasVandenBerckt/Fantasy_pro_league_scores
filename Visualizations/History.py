import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import duckdb

data = pd.read_excel('../Data/jpl_fantasy_data.xlsx')

con = duckdb.connect('../Data/jpl_fantasy_data.db')
con.execute("CREATE TABLE IF NOT EXISTS fantasy_scores AS SELECT * FROM data")

result = con.execute("SELECT Punten FROM fantasy_scores WHERE Naam LIKE 'Mauvenhart'").fetchall()
print(result)
con.close()

     
