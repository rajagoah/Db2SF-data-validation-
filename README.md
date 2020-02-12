# DataValidation_Db2SF
Validate the data between db2 and sf. both the data will be loaded as a csv file

1. On a daily basis, I am required to reconcile the count between the source (db2) and target (salesforce) systems.
2. The counts never match, with Salesforce always showing more records that what came in the from the source.
3. This module that I'm writing will perform the following functions:
  1. Read the data from a csv file and store in a data frame
  2. Leverage functions within the pandas package to wrangle the data
  3. Create 6 major subsets (3 each for source and target). the subsets will be filtered on PROGRAM_TYPE=MP,CPO,ESC
  4. Program types in nothing but the type of contracts that are sold to customers.
  
  
  <No confidential data will be made available>
