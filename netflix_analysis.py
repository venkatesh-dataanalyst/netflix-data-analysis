import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())

type_counts= df['type'].value_counts()


plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

top_country = df['country'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_country.values, y=top_country.index)
plt.title("Top 10 Countries producing Netflix content")
plt.show()

year_count = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(year_count.index, year_count.values)
plt.title("Netflix Content by Release Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

fig = px.line(
    x=year_count.index,
    y=year_count.values,
    title="Netflix Content Trend Over Years"
)

fig.show()


rating_count = df['rating'].value_counts()

plt.figure(figsize=(8,5))
sns.countplot(y="rating", data=df)

plt.title("Netflix Rating Distribution")
plt.show()

top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_directors.values, y=top_directors.index)

plt.title("Top Directors on Netflix")
plt.show()

added_year = df['date_added'].dropna()

added_year = pd.to_datetime(added_year)

year_added = added_year.dt.year.value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.plot(year_added.index, year_added.values)

plt.title("Content Added to Netflix Over Years")
plt.xlabel("Year")
plt.ylabel("Count")

plt.show()

