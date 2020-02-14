#importing module
import pandas as pd
import numpy as np

def SfDb2MPCounts(db2_path, sf_path):

    #setting ipythons max row and column display
    pd.set_option('display.max_row',1000)
    pd.set_option('display.max_column',60)

    #storing the db2 data in to a variable
    db2 = pd.read_csv(db2_path)
    sf = pd.read_csv(sf_path)

    #printing out the top 5 records as a sample.
    print('########## DB2 SHAPE ##########')
    print(db2.shape)

    print('########## DB2 UNIQUE CONTRACT STATUS FIELD ##########')
    print(db2['CONTRACT_STATUS'].unique())

    print('########## SF SHAPE ##########')
    print(sf.shape)

    #converting the entire data frame to string and removing trailing and leading spaces
    #db2_df = db2.columns.str.strip()
    #sf_df = sf.columns.str.strip()
    db2['PROGRAM_TYPE'] = db2['PROGRAM_TYPE'][1:].str.strip()
    db2['PROG_ID'] = db2['PROG_ID'][1:].map(str).str.strip()
    db2['CONTRACT_STATUS'] = db2['CONTRACT_STATUS'][1:].str.strip()

    #determining the type of object
    print('########## DB2 TYPE ##########')
    print(type(db2))

    print('########## SF TYPE ##########')
    print(type(sf))

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

    #filtering a subset to hold only MP Active / pending / expired / Cancelled contracts using chaining
    ############################## DB2 ##############################
    db2_mp_act = db2.query('CONTRACT_STATUS == "Active"')
    print('number of rows in db2_mp -->', len(db2_mp_act))

    db2_mp_pen = db2.query('CONTRACT_STATUS == "Pending"')
    print('number of rows in db2_mp -->', len(db2_mp_pen))

    db2_mp_exp = db2.query('CONTRACT_STATUS == "Expired"')
    print('number of rows in db2_mp -->', len(db2_mp_exp))

    db2_mp_can = db2.query('CONTRACT_STATUS == "Cancelled"')
    print('number of rows in db2_mp -->', len(db2_mp_can))

    ############################## SF ##############################
    sf_mp_act = sf.query('VCS2_Contract_Status__c == "Active"')
    print('number of rows in sf_mp -->', len(sf_mp_act))

    sf_mp_pen = sf.query('VCS2_Contract_Status__c == "Pending"')
    print('number of rows in sf_mp -->', len(sf_mp_pen))

    sf_mp_exp = sf.query('VCS2_Contract_Status__c == "Expired"')
    print('number of rows in sf_mp -->', len(sf_mp_exp))

    sf_mp_can = sf.query('VCS2_Contract_Status__c == "Cancelled"')
    print('number of rows in sf_mp -->', len(sf_mp_can))

    ############################## Calculating the difference in lengths of the ab ove data frames ##############################
    print('difference in count of rows for active records -->', len(sf_mp_act) - len(db2_mp_act))
    print('difference in count of rows for pending records -->', len(sf_mp_pen) - len(db2_mp_pen))
    print('difference in count of rows for expired records -->', len(sf_mp_exp) - len(db2_mp_exp))
    print('difference in count of rows for cancelled records -->', len(sf_mp_can) - len(db2_mp_can))

    #Creating a third list to store the excess records. Making use of setdiff1d function in numpy module to find out
    # values present in sf_mp_act but not in db2_mp_act
    recs_not_present_active = np.setdiff1d(sf_mp_act['Unique_string'], db2_mp_act['Unique_string'], assume_unique=False)

    # values present in sf_mp_pen but not in db2_mp_pen
    recs_not_present_pending = np.setdiff1d(sf_mp_pen['Unique_string'], db2_mp_pen['Unique_string'], assume_unique=False)

    # values present in sf_mp_pen but not in db2_mp_exp
    recs_not_present_expired = np.setdiff1d(sf_mp_exp['Unique_string'], db2_mp_exp['Unique_string'], assume_unique=False)

    # values present in sf_mp_pen but not in db2_mp_can
    recs_not_present_cancelled = np.setdiff1d(sf_mp_can['Unique_string'], db2_mp_can['Unique_string'], assume_unique=False)


    print('########## Number of active present in Sales force but not present in db2 are ##########')
    print(len(recs_not_present_active))

    print('########## Number of pending contracts present in Sales force but not present in db2 are ##########')
    print(len(recs_not_present_pending))

    print('########## Number of expired contracts present in Sales force but not present in db2 are ##########')
    print(len(recs_not_present_expired))

    print('########## Number of cancelled contracts present in Sales force but not present in db2 are ##########')
    print(len(recs_not_present_cancelled))

    return recs_not_present_active, recs_not_present_pending, recs_not_present_expired, recs_not_present_cancelled

if __name__=="__main__":

    #taking input from user and directly passing value to the SfDb2MPCounts() module
    #db2 = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/CON data set/CON-MP-All statuses 3-13 db2.csv'
    #sf = '/Users/aakarsh.rajagopalan/Personal documents/Python projects/CON data set/CON-MP-All statuses 2-13 sf.csv'

    #adding a try except block to handle FileNotFoundError and the NameError
    try:
        recs_not_present_active, recs_not_present_pending, recs_not_present_expired, recs_not_present_cancelled = SfDb2MPCounts(input('Enter the db2 file path -- '), input('Enter the sf file path -- '))
        print('########## The values active are ##########')
        print(recs_not_present_active)

        print('########## The values pending are ##########')
        print(recs_not_present_pending)

        print('########## The values expired are ##########')
        print(recs_not_present_expired)

        print('########## The values cancelled are ##########')
        print(recs_not_present_cancelled)

    except FileNotFoundError:
        print('********** ERROR MESSAGE *************\n'+
              ' File not found. please rerun the program and re enter the file name with path')
    except NameError:
        print('********** ERROR MESSAGE*************\n'+
        'Name of the file is incorrect as the system was unable to find it. Please rerun the program and re etner the file name with path')


