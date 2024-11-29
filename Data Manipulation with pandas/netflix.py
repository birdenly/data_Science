# Importing pandas and matplotlib
import os

import matplotlib.pyplot as plt
import pandas as pd

# Read in the Netflix CSV as a DataFrame
file_path = os.path.join(os.path.dirname(__file__), 'netflix_data.csv') # get current directory
netflix_df = pd.read_csv(file_path)

# Print the DataFrame and shows number of rows and columns
print(netflix_df)

print("---------choose column-----------")

# simple way to choose a column
simple = netflix_df[["title","genre"]]
print(simple)

print("---------filter----------")

#filter
simple_filter = ["Action","Comedies"]
print(simple[(simple["genre"] == "Action") | (simple["genre"] == "Comedies")])
print("####") # both the same
print(simple[simple["genre"].isin(simple_filter)])

print("---------filter2----------")

#filter
simple_filter2 = netflix_df[(netflix_df["cast"].str.contains("Elijah Wood")) & (netflix_df["genre"] == "Action")]

print(simple_filter2[["title","cast","genre"]])

print("---------info-----------")

# Gives the columns names and their data types object, int etc
print(netflix_df.info())

print("--------shape-----------")

# Only gives the number of rows and columns
print(netflix_df.shape)

print("--------describe----------")

# Gives info about numerical columns, count = number of non-null values, mean, std, min, 25%, 50%, 75%, max
print(netflix_df.describe())

print("--------values-----------")

# values of the DataFrame
print(netflix_df.values)

print("-------columns----------")

#give the columns names as an array
print(netflix_df.columns)

print("-------index----------")

print(netflix_df.index)

print("-------head----------")
# Print the first five rows of the DataFrame
print(netflix_df.head())

print("--------sort--------")

#Sorting either pass one string or a list of strings, will sort by the first string and within that group sort by the second string. ascending can also be a list
print(netflix_df.sort_values(by=["release_year","duration"],ascending=False))

print("--------new column--------")

netflix_df["new_column"] = netflix_df["release_year"] - netflix_df["duration"]
print(netflix_df.head())

print("--------drop duplicate--------")
# dumb but yea
print(netflix_df["release_year"].value_counts(sort=True))
duplicates = netflix_df.drop_duplicates(subset=["release_year","duration"]) # more unique with more columns
print(duplicates)
print(duplicates["release_year"].value_counts(sort=True))

print("--------sumary by type--------")
#avg duration by genre
print(netflix_df.groupby("genre")["duration"].mean().sort_values(ascending=False))
#avg duration by genre and by year as matrix
print(netflix_df.pivot_table(values="duration",index="genre",columns="release_year",fill_value=0,margins=True)) #aggfunc

print("--------column to index--------")
#turn  a column to a index
#changes from a column to an index**
netflix_index = netflix_df.set_index(["title","genre"]).sort_index()
print(netflix_index)

#outer index level
print(netflix_index.loc["The Lord of the Rings: The Return of the King":"The Lost Okoroshi"])

#inner index level
print(netflix_index.loc[("The Lord of the Rings: The Return of the King","Action"):("The Lost Okoroshi","Comedies")])

#slice
print(netflix_index.loc[("The Lord of the Rings: The Return of the King","Action"):("The Lost Okoroshi","Comedies"),"show_id":"release_year"])

# Reset the temperatures_ind index, keeping its contents
print(netflix_index.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(netflix_index.reset_index(drop=True))

"""
summary statistics

.mean() - Compute mean of columns
.median() - Compute median of columns | mediana - middle value
.mode() - Compute mode of columns | moda - most appears
.min() - Compute minimum of columns 
.max() - Compute maximum of columns
.count() - Compute count of columns | returns amout of null values
.var() - Compute variance of columns | basically calculates the distance from the avarage - a higher variance indicates more spread out data.
.std() - Compute standard deviation of columns | similar to variance - high standard deviation indicates that the data is spread out aka not close to the mean
.sum() - Compute sum of columns
.agg() - Can apply multiple (custom) functions to columns
.cumsum() - Compute cumulative sum of columns
.cummax() - Compute cumulative maximum of columns

.agg example: unemp_fuel_stats = sales.groupby("type")[["unemployment","fuel_price_usd_per_l"]].agg([np.min,np.max,np.mean,np.median])
"""

# # Print the first five rows of the DataFrame
# print(netflix_df.head())

# # Subset the DataFrame for type "Movie"
# netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# # Filter the to keep only movies released in the 1990s
# # Start by filtering out movies that were released before 1990
# subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# # And then do the same to filter out movies released on or after 2000
# movies_1990s = subset[(subset["release_year"] < 2000)]

# # Another way to do this step is to use the & operator which allows you to do this type of filtering in one step
# # movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# # Visualize the duration column of your filtered data to see the distribution of movie durations
# # See which bar is the highest and save the duration value, this doesn't need to be exact!
# plt.hist(movies_1990s["duration"])
# plt.title('Distribution of Movie Durations in the 1990s')
# plt.xlabel('Duration (minutes)')
# plt.ylabel('Number of Movies')
# plt.show()

# duration = 100

# # Filter the data again to keep only the Action movies
# action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# # Use a for loop and a counter to count how many short action movies there were in the 1990s

# # Start the counter
# short_movie_count = 0

# # Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
# for label, row in action_movies_1990s.iterrows() :
#     if row["duration"] < 90 :
#         short_movie_count = short_movie_count + 1
#     else:
#         short_movie_count = short_movie_count

# print(short_movie_count)

# # A quicker way of counting values in a column is to use .sum() on the desired column
# # (action_movies_1990s["duration"] < 90).sum()