import mysql.connector
import pandas as pd 
PhonePe_Database=mysql.connector.connect(host='localhost',
                        database='phonepe_database',
                        user='root',
                        password='Focus24h')
mycursor = PhonePe_Database.cursor()

# TABLES
# Data_Aggregated_Transaction_Table
# Data_Aggregated_User_Summary_Table
# Data_Aggregated_User_Table
# Data_Map_Districts_Longitude_Latitude
# Data_Map_Transaction_Table

#------1------CREATE-----------INSERT---------------------Data_Aggregated_Transaction_Table
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Aggregated_Transaction_Table (MyIndex INT NOT NULL AUTO_INCREMENT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,Quarter INT,Year INT,State INT,PRIMARY KEY (MyIndex))"
mycursor.execute(sql)
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_Transaction_Table.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Aggregated_Transaction_Table(Payment_Mode,Total_Transactions_count,Total_Amount,Quarter,Year,State) values(%s,%s,%s,%s,%s,%S)"
     mycursor.execute(quer,(row.Payment_Mode,row.Total_Transactions_count,row.Total_Amount,row.Quarter,row.Year,row.State))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

#------2------CREATE-----------INSERT---------------------Data_Aggregated_User_Summary_Table
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Aggregated_User_Summary_Table (MyIndex INT NOT NULL AUTO_INCREMENT,State VARCHAR(50),Year INT,Quarter INT,Registered_Users BIGINT,AppOpenings BIGINT,PRIMARY KEY (MyIndex))"
mycursor.execute(sql) 
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_User_Summary_Table.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Aggregated_User_Summary_Table(State,Year,Quarter,Registered_Users,AppOpenings) values(%s,%s,%s,%s,%s)"
     mycursor.execute(quer,(row.State,row.Year,row.Quarter,row.Registered_Users,row.AppOpenings))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

#------3------CREATE-----------INSERT------------------------Data_Aggregated_User_Table
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Aggregated_User_Table (MyIndex INT NOT NULL AUTO_INCREMENT,Brand_Name VARCHAR(50),Registered_Users_Count BIGINT,Percentage_Share_of_Brand FLOAT,Quarter INT,Year INT,State INT,PRIMARY KEY (MyIndex))"
mycursor.execute(sql)
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_User_Table.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Aggregated_User_Table(Brand_Name,Registered_Users_Count,Percentage_Share_of_Brand,Quarter,Year,State) values(%s,%s,%s,%s,%s,%S)"
     mycursor.execute(quer,(row.Brand_Name,row.Registered_Users_Count,row.Percentage_Share_of_Brand,row.Quarter,row.Year,row.State))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

#------4------CREATE-----------INSERT--------------------------Data_Map_Districts_Longitude_Latitude
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Map_Districts_Longitude_Latitude ( MyIndex INT NOT NULL AUTO_INCREMENT,State VARCHAR(50),District VARCHAR(50),Latitude VARCHAR(50),Longitude VARCHAR(50), PRIMARY KEY (MyIndex))"
mycursor.execute(sql)
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_Districts_Longitude_Latitude.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Map_Districts_Longitude_Latitude(State,District,Latitude,Longitude) values(%s,%s,%s,%s)"
     mycursor.execute(quer,( row.State, row.District, row.Latitude, row.Longitude))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

#------5------CREATE-----------INSERT-----------------------------Data_Map_IndiaStates_TU
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Map_IndiaStates_TU (MyIndex INT NOT NULL AUTO_INCREMENT,state VARCHAR(50),Registered_Users BIGINT,PRIMARY KEY (MyIndex))"
mycursor.execute(sql)
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_IndiaStates_TU.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Map_IndiaStates_TU(state,Registered_Users) values(%s,%s)"
     mycursor.execute(quer,(row.state,row.Registered_Users))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

#------6------CREATE-----------INSERT---------------------------------Data_Map_Transaction_Table
#CREATE TABLE & INSERT DATAFRAME INTO DATABASE
sql= "CREATE TABLE Data_Map_Transaction_Table (MyId INT NOT NULL AUTO_INCREMENT,Place_Name VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,Quarter INT,Year INT,State INT,MyIndex INT,PRIMARY KEY (MyId))"
mycursor.execute(sql)
print('Table created successfully.')
PhonePe_Database.commit()
df=pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_Transaction_Table.csv')
for index, row in df.iterrows():
     quer="INSERT INTO PhonePe_Database.Data_Map_Transaction_Table(Place_Name,Total_Transactions_count,Total_Amount,Quarter,Year,State,MyIndex) values(%s,%s,%s,%s,%s,%s,%s)"
     mycursor.execute(quer,(row.Place_Name,row.Total_Transactions_count,row.Total_Amount,row.Quarter,row.Year,row.State,row.MyIndex))
print('DataFrame Inserted successfully.')
PhonePe_Database.commit()
mycursor.close()

