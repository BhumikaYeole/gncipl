import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

athlete = pd.read_csv("athlete_events.csv")

# print(athlete.head())

medalists = athlete.dropna(subset=["Medal"])
count = medalists.groupby(["Year","NOC"])["Medal"].count().reset_index()
data_2016 = medalists[medalists['Year'] == 2016]
top_countries = data_2016['NOC'].value_counts().head(15)

sns.barplot(x=top_countries.index, y=top_countries.values)
plt.title("Top 15 Countries - Olympic Medals in 2016")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.show()

usa_medals = medalists[medalists['NOC'] == 'USA']
usa_trend = usa_medals.groupby('Year').size()

usa_trend.plot(kind='barh', title='USA Olympic Medal Trend Over Time')
plt.xlabel("Year")
plt.ylabel("Medals")
plt.show()

# country wise dominance 

sport_dominance = medalists.groupby(['Sport', 'NOC']).size().reset_index(name='Medals')

top_sport_countries = sport_dominance.sort_values('Medals', ascending=False).groupby('Sport').head(1)
print(top_sport_countries)