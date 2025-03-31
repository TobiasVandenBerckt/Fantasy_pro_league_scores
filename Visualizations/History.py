import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import duckdb

data = pd.read_excel('../Data/jpl_fantasy_data.xlsx')

con = duckdb.connect('../Data/jpl_fantasy_data.db')
con.execute("CREATE TABLE IF NOT EXISTS fantasy_scores AS SELECT * FROM data")

User1Points = con.execute("SELECT Speeldag, Punten, Naam FROM fantasy_scores WHERE Naam LIKE 'Boerenhart'").fetchall()
User2Points = con.execute("SELECT Speeldag, Punten, Naam FROM fantasy_scores WHERE Naam LIKE 'Grootste mauve ooit'").fetchall()
User3Points = con.execute("SELECT Speeldag, Punten, Naam FROM fantasy_scores WHERE Naam LIKE 'Smurfenhart'").fetchall()
User4Points = con.execute("SELECT Speeldag, Punten, Naam FROM fantasy_scores WHERE Naam LIKE 'Mauvenhart'").fetchall()
User5Points = con.execute("SELECT Speeldag, Punten, Naam FROM fantasy_scores WHERE Naam LIKE 'Emiel'").fetchall()

df = pd.DataFrame({
    "Speeldag": [x[0] for x in User1Points + User2Points + User3Points + User4Points+ User5Points], 
    "Punten": [x[1] for x in User1Points + User2Points + User3Points + User4Points+ User5Points], 
    "Speler": [x[2] for x in User1Points + User2Points + User3Points + User4Points+ User5Points]
})

sns.barplot(df, x="Speeldag", y="Punten", hue="Speler")
plt.legend()
plt.title("Verkregen punten over de eerste 30 speeldagen")
plt.show()
con.close()

     
