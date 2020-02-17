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

#grouping by state_po and extracting the count of countys in each state
print(data.groupby('state')['county'].count())

#outputing only for newjersey
data_nj = data.query('state == "New Jersey"')

print('***************************** NJ ONLY FILTER COMPLETE *****************************')

#grouping by county, year and party to extract count of candidate votes
data_nj_countByParty = data_nj.groupby(['state','county','year','party','candidate']).agg(
        CountByParty=pd.NamedAgg(column='candidatevotes',aggfunc=sum))

print(data_nj_countByParty.head())

#logic for deciding winner
print(data_nj_countByParty.groupby(['state','county','year'])['CountByParty'].max())