# PhonePe-Pulse-Data-2018-2022-Analysis
I have created a dashboard to visualize Phonepe pulse Github repository data(https://github.com/PhonePe/pulse) using Streamlit and Plotly in Python 

Link for web app is : https://tulasinnd-phonepe-pulse-data-2018-2022-phonepe-dashboard-2drsrt.streamlit.app/

THE MAIN COMPONENTS OF DASHBOARD ARE

    1 GEO-VISUALIZATION
    
    2 TRANSACTIONS ANALYSIS
    
    3 USERS ANALYSIS
    
    4 TOP STATES DATA
    
1 Geo-Visualization:
    The India map shows the Total Transactions of PhonePe in both state wide and District wide.It comes with zoom 
    option and on hover displays the content related to that particular state or district.The main 
    functions I have used to create this map are (User can give year and quarter input to show how the data changed over time)
    
    1 Plotlys scatter_geo for plotting districts along with the conent    
    
    2 Plotlys coropleth for drawing the states in India map    
    
2 Transactions Analysis:
    The Transactions data mainly contains the total Transactions count and total amount  in each state and 
district, I have used different graphs available in plotly to represent this data

    1 State-wise study
    The above bar graph shows the increasing order of PhonePe Transactions according to the states of India, 
    Here we can observe the top states with the highest Transaction by looking at graph
    
    2 District-wise study
    User can observe how transactions are happening in districts of a selected state.We can observe the 
    leading distric in a state
    
    3 Year-wise study   
    We can observe the states with total transactions in particular mode in the selected year
    
    4 Overall Analysis
    To show how the transactions drastically increased with time

3 User Data Analysis: 
    The Users data mainly contains the Registered Users count and App openings via different 
    mobile brands in each state and  district,I have used different graphs available in plotly 
    to represent this data

    1 State-wise study
    User can observe how the App Openings are growing and how Registered users are growing in a state
    
    2 District-wise study
    User can observe how App Openings are happening in districts of a selected state
    
    3 Year-wise study   
    User can observe the top leading brands in a particular state in given year
    
    4 Overall Analysis
    We can see that the Registered Users and App openings are increasing year by year
    
4 Top States Data:

    1 States with top Registered users
    2 States with top Total Amount Transacted
    3 States with highest Trabsactions count
    4 States with top app openings

