#importing required modules
import pandas as pd

#configuring the display limits of the columns and rows
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows',15)

print('***************************** CONFIG COMPLETE *****************************')

#using read_csv file to create a data frame out of the input file
data = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/countypres_2000-2016.csv')

#displaying the data type of the read data
print(type(data))

#displaying the shape of the datafram
print(data.shape)

print('***************************** DATA READ COMPLETE *****************************')

#sampling the data to the console
print(data.head())

#outputing only for newjersey
data_nj = data.query('state == "New Jersey"')
print('***************************** NJ ONLY FILTER COMPLETE *****************************')

#grouping by county, year and party to extract count of candidate votes
print(data_nj.groupby(['state','year','party','candidate']).agg(
        votes_by_party = pd.NamedAgg(column = 'candidatevotes', aggfunc = sum)
).sort_index)

data_nj_sum = pd.DataFrame(data_nj.groupby(['state','year','party','candidate']).agg(
        votes_by_party = pd.NamedAgg(column = 'candidatevotes', aggfunc = sum)
))

print('***************************** FINDING OUT WHO WON IN NJ *****************************')
#finding out who won in nj
print(data_nj.groupby(['state','year']).agg(
        winning_votes = pd.NamedAgg(column ='candidatevotes', aggfunc = max)
).reset_index())

data_nj_winner = data_nj.groupby(['state','year']).agg(
        winning_votes = pd.NamedAgg(column ='candidatevotes', aggfunc = max))


print('***************************** PRINTING THE DATA FRAME FOR NJ *****************************')
print(data_nj_sum)


print('***************************** WRITING TO CSV *****************************')
#using the reset_index() method to allow all the columns to be printed in to the csv
data_nj_sum.reset_index().to_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/data_nj_countByParty.csv',  index = False)

data_nj_winner.reset_index().to_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Winner_in_nj.csv',  index = False)