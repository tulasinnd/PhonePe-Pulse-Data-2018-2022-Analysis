# PhonePe-Pulse-Data-2018-2022-Analysis
I have created a dashboard to visualize Phonepe pulse Github repository data(https://github.com/PhonePe/pulse) using Streamlit and Plotly in Python 

Link for web app is : https://tulasinnd-phonepe-pulse-data-2018-2-phonepe-dashboard-df-sochbu.streamlit.app/

Geo-Visualization:
The India map shows the Total Transactions of PhonePe in both state wide and District wide. 
It comes with zoom option and on hover displays the content related to that particular state or district
The main functions I have used to create this map are 
Plotlys scatter_geo for plotting districts along with the conent
Plotlys coropleth for drawing the states in India map
User can give year and quarter input to show how the data changed over time

Transactions Analysis:
The Transactions data mainly contains the total Transactions count and total amount  in each state and  district, I have used different graphs available in plotly to represent this data
1 State and Total Transactions BAR CHAT (User Input: Year, Quarter)
The above bar graph shows the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with the highest      Transaction by looking at graph
2 State & PaymentMode BAR CHAT (User Input: Payment Mode, State)
The above bar graph shows how each payment mode is performed statewide
3 PaymentMode and Year  (User Input: Payment Mode, Year)
The above bar graph shows the total number of transactions that happened in a particular payment mode in all states
4 PIE CHAT
To show how the transactions drastically increased with time

User Data Analysis:
The Users data mainly contains the Registered Users count and App openings via different mobile brands  in each state and  district, I have used different graphs available in plotly to represent this data
1 Brand Share DONUT  &  BAR CHAT   (User Input: State, Year)
The above donut chat shows  how the users are registered through different brans in india. We can also see which brand has more users and the brand with less users
2  State & Userbase MULTI-BAR CHAT (State)
This Multi-bar graph tells how the user base is created in particular state with respect to app openings and Registered users

Top 5 States Data:
1 DataFrame (User Input:  Year, Quarter, Appopening)
Top 5 States With Highest PhonePeApp Openings in given year and Quarter
2 DataFrame (User Input:  Year, Quarter, Registered Users)
Top 5 States With Highest Registered Users in given year and Quarter

