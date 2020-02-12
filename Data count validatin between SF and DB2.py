import pandas as pd

#storing the db2 data in to a variable
db2 = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Python projects/CON data set/DB2 data set 02-12-20.csv')
sf = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Python projects/CON data set/SF data set 02-12-20.csv')

#printing out the top 5 records as a sample.
#print(db2.head())
#print(sf.head())

#converting the entire data frame to string and removing it of trailing and leading spaces
#db2_df = db2.columns.str.strip()
#sf_df = sf.columns.str.strip()
db2['PROGRAM_TYPE'] = db2['PROGRAM_TYPE'][1:].str.strip()
db2['PROG_ID'] = db2['PROG_ID'][1:].map(str).str.strip()
db2['CONTRACT_STATUS'] = db2['CONTRACT_STATUS'][1:].str.strip()

#coverting the index class to a data frame
db2_df = pd.DataFrame(db2)
sf_df = pd.DataFrame(sf)


#outputing info to console
#print(type(db2_df))
#print(db2_df.shape)
#print(sf_df.shape)

#Db2 cocnatenating the values of the PK fields to create a unique string field
db2['Unique_string']=db2['PROGRAM_TYPE'].map(str).str.strip()\
                     +db2['LINE_MAKE'].map(str).str.strip()\
                     +db2['PROG_ID'].map(str).str.strip()\
                     +db2['MODEL_CODE'].map(str).str.strip()\
                     +db2['MODEL_YEAR'].map(str).str.strip()\
                     +db2['CHASSIS_NBR'].map(str).str.strip()

#SF cocnatenating the values of the PK fields to create a unique string field
sf['Unique_string']=sf['VCS2_Program_Type__c'].map(str).str.strip()\
                     +sf['VCS2_Line_Make__c'].map(str).str.strip()\
                     +sf['VCS2_Program_Id__c'].map(str).str.strip()\
                     +sf['VCS2_Model_Code__c'].map(str).str.strip()\
                     +sf['VCS2_Model_Year__c'].map(str).str.strip()\
                     +sf['VCS2_Chassis_Number__c'].map(str).str.strip()


#printing a sample unique string
print('number of rows in db2-->', len(db2_df))
print('number of rows in sf-->', len(sf_df))

#filtering a subset to hold only MP contracts using chaining
db2_mp = db2_df.query('PROGRAM_TYPE == "MP" and PROG_ID != "300" and PROG_ID != "168" and PROG_ID != "149"')
print('number of rows in db2_mp -->', len(db2_mp))

sf_mp = sf_df.query('VCS2_Program_Type__c == "MP"')
print('number of rows in sf_mp -->', len(sf_mp))

#now branching out into various contract statuses
db2_mp_act = db2_mp.query('CONTRACT_STATUS == "A"')
print('number of rows in db2_mp_act -->', len(db2_mp_act))

sf_mp_act = sf_mp.query('VCS2_Contract_Status__c == "Active"')
print('number of rows in sf_mp_act -->', len(sf_mp_act))
#iterating through the dataframe to identify which unique string in sf doesn't exist in db2
#declaring a counter variable to be used in the else part of the if statement.
#This counter variable is being used to identify how many records do not exist in the db2 data frame
#j=0
#for i in range(len(sf[0:])):
# if sf['Unique_string'][i] in list(db2['Unique_string']):
  #      continue
   # else:
        #print(sf[:i]['VCS2_Program_Type__c','VCS2_Line_Make__c','VCS2_Program_Id__c','VCS2_Model_Code__c','VCS2_Model_Year__c','VCS2_Chassis_Number__c'])
    #    print(sf.iloc[i])
     #    j = j + 1
