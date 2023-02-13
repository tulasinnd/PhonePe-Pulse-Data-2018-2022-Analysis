import pandas as pd 
import plotly.express as px
import streamlit as st 
import plotly.graph_objects as go

# Data_Aggregated_Transaction_df= pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_Transaction_Table.csv')
# Data_Aggregated_User_Summary_df= pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_User_Summary_Table.csv')
# Data_Aggregated_User_df= pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Aggregated_User_Table.csv')
# Scatter_Geo_Dataset =  pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_Districts_Longitude_Latitude.csv')
# Coropleth_Dataset =  pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_IndiaStates_TU.csv')
# Data_Map_Transaction_df = pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Data_Map_Transaction_Table.csv')
# Indian_States= pd.read_csv(r'C:\Users\91939\OneDrive\Desktop\PhonePe_P2\data\Longitude_Latitude_State_Table.csv')

Data_Aggregated_Transaction_df= pd.read_csv(r'data/Data_Aggregated_Transaction_Table.csv')
Data_Aggregated_User_Summary_df= pd.read_csv(r'data/Data_Aggregated_User_Summary_Table.csv')
Data_Aggregated_User_df= pd.read_csv(r'data/Data_Aggregated_User_Table.csv')
Scatter_Geo_Dataset =  pd.read_csv(r'data/Data_Map_Districts_Longitude_Latitude.csv')
Coropleth_Dataset =  pd.read_csv(r'data/Data_Map_IndiaStates_TU.csv')
Data_Map_Transaction_df = pd.read_csv(r'data/Data_Map_Transaction_Table.csv')
Indian_States= pd.read_csv(r'data/Longitude_Latitude_State_Table.csv')

st.title(':blue[PhonePe Pulse Data(2018-2022):signal_strength:]')
st.write("### **:blue[PhonePe India]**")
Year = st.selectbox(
    'Please select the Year',
    ('2018', '2019', '2020','2021','2022'))
Quarter = st.selectbox(
    'Please select the Quarter',
    ('1', '2', '3','4'))
year=int(Year)
quarter=int(Quarter)
Transaction_scatter_districts=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year ) & (Data_Map_Transaction_df['Quarter']==quarter) ].copy()
Transaction_Coropleth_States=Transaction_scatter_districts[Transaction_scatter_districts["State"] == "india"]
Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(Transaction_scatter_districts["State"] == "india")],axis=0,inplace=True)
# Dynamic Scattergeo Data Generation
Transaction_scatter_districts = Transaction_scatter_districts.sort_values(by=['Place_Name'], ascending=False)
Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by=['District'], ascending=False) 
Total_Amount=[]
for i in Transaction_scatter_districts['Total_Amount']:
    Total_Amount.append(i)
Scatter_Geo_Dataset['Total_Amount']=Total_Amount
Total_Transaction=[]
for i in Transaction_scatter_districts['Total_Transactions_count']:
    Total_Transaction.append(i)
Scatter_Geo_Dataset['Total_Transactions']=Total_Transaction
Scatter_Geo_Dataset['Year_Quarter']=str(year)+'-Q'+str(quarter)
# Dynamic Coropleth
Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['state'], ascending=False)
Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by=['Place_Name'], ascending=False)
Total_Amount=[]
for i in Transaction_Coropleth_States['Total_Amount']:
    Total_Amount.append(i)
Coropleth_Dataset['Total_Amount']=Total_Amount
Total_Transaction=[]
for i in Transaction_Coropleth_States['Total_Transactions_count']:
    Total_Transaction.append(i)
Coropleth_Dataset['Total_Transactions']=Total_Transaction
# -------------------------------------FIGURE1 MAP------------------------------------------------------------------
#scatter plotting the states codes 
Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
Indian_States['Registered_Users']=Coropleth_Dataset['Registered_Users']
Indian_States['Total_Amount']=Coropleth_Dataset['Total_Amount']
Indian_States['Total_Transactions']=Coropleth_Dataset['Total_Transactions']
Indian_States['Year_Quarter']=str(year)+'-Q'+str(quarter)
fig=px.scatter_geo(Indian_States,
                   lon=Indian_States['Longitude'],
                   lat=Indian_States['Latitude'],                                
                   text = Indian_States['code'], #It will display district names on map
                   hover_name="state", 
                   hover_data=["Registered_Users",'Total_Amount',"Total_Transactions","Year_Quarter"],
                   )
fig.update_traces(marker=dict(color="white" ,size=0.3))
fig.update_geos(fitbounds="locations", visible=False,)
# scatter plotting districts
Scatter_Geo_Dataset['col']=Scatter_Geo_Dataset['Total_Transactions']
fig1=px.scatter_geo(Scatter_Geo_Dataset,
                   lon=Scatter_Geo_Dataset['Longitude'],
                   lat=Scatter_Geo_Dataset['Latitude'],
                   color=Scatter_Geo_Dataset['col'],
                   size=Scatter_Geo_Dataset['Total_Transactions'],     
                   #text = Scatter_Geo_Dataset['District'], #It will display district names on map
                   hover_name="District", 
                   hover_data=["State", "Total_Amount","Total_Transactions","Year_Quarter"],
                   title='District',
                   size_max=22,)
fig1.update_traces(marker=dict(color="rebeccapurple" ,line_width=1))    
#coropleth mapping india
fig_ch = px.choropleth(
                Coropleth_Dataset,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',                
                locations='state',
                color="Total_Transactions",                                       
                )
fig_ch.update_geos(fitbounds="locations", visible=False,)
#combining districts states and coropleth
fig_ch.add_trace( fig.data[0])
fig_ch.add_trace(fig1.data[0])
st.plotly_chart(fig_ch)
st.info('**:blue[The above India map shows the Total Transactions of PhonePe in both state wide and District wide. Please zoom in or full screen for more information]**')
# -----------------------------------------------FIGURE2 BAR------------------------------------------------------------------------
st.write("### :blue[State & Transactions]")
Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['Total_Transactions'])
fig = px.bar(Coropleth_Dataset, x='state', y='Total_Transactions',title='Total Transaction in '+str(year)+" Quarter"+str(quarter)+" in increasing order")
st.plotly_chart(fig)
st.info('**:blue[The above bar graph showing the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with highest Transaction by looking at graph]**')
# ------------------------------------------------FIGURE3 BAR--------------------------------------------------------
st.write('# :green[TRANSACTIONS ANALYSIS :currency_exchange:]')
Data_Aggregated_Transaction=Data_Aggregated_Transaction_df.copy()
Data_Aggregated_Transaction.drop(Data_Aggregated_Transaction.index[(Data_Aggregated_Transaction["State"] == "india")],axis=0,inplace=True)
State_PaymentMode=Data_Aggregated_Transaction.copy()
st.write('### :green[State & PaymentMode]')
mode = st.selectbox(
    'Please select the Mode',
    ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services','Others'),key='a')
state = st.selectbox(
    'Please select the State',
    ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
       'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
       'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
       'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
       'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'),key='b')
State= state
Year_List=[2018,2019,2020,2021,2022]
Mode=mode
State_PaymentMode=State_PaymentMode.loc[(State_PaymentMode['State'] == State ) & (State_PaymentMode['Year'].isin(Year_List)) & 
                        (State_PaymentMode['Payment_Mode']==Mode )]
State_PaymentMode = State_PaymentMode.sort_values(by=['Year'])
State_PaymentMode["Quarter"] = "Q"+State_PaymentMode['Quarter'].astype(str)
State_PaymentMode["Year_Quarter"] = State_PaymentMode['Year'].astype(str) +"-"+ State_PaymentMode["Quarter"].astype(str)
import plotly.express as px
fig = px.bar(State_PaymentMode, x='Year_Quarter', y='Total_Transactions_count',color="Total_Transactions_count",
            title='The Transaction pattern of '+Mode+' in '+State, color_continuous_scale="Viridis")
st.plotly_chart(fig)
st.info('**:green[The above bar graph shows how each payment mode performed state wide]**')
# -----------------------------------------FIGURE4 BAR---------------------------------------------------------------------
st.write('### :red[PaymentMode and Year]')
M = st.selectbox(
    'Please select the Mode',
    ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services','Others'),key='D')
Y = st.selectbox(
    'Please select the Year',
    ('2018', '2019', '2020','2021','2022'),key='F')
Year_PaymentMode=Data_Aggregated_Transaction.copy()
Year=int(Y)
Mode=M
Year_PaymentMode=Year_PaymentMode.loc[(Year_PaymentMode['Year']==Year) & 
                        (Year_PaymentMode['Payment_Mode']==Mode )]
States_List=Year_PaymentMode['State'].unique()
State_groupby_YP=Year_PaymentMode.groupby('State')
Year_PaymentMode_Table=State_groupby_YP.sum()
Year_PaymentMode_Table['states']=States_List
del Year_PaymentMode_Table['Quarter']
del Year_PaymentMode_Table['Year']
Year_PaymentMode_Table = Year_PaymentMode_Table.sort_values(by=['Total_Transactions_count'])
fig2= px.bar(Year_PaymentMode_Table, x='states', y='Total_Transactions_count',color="Total_Transactions_count",
            title='In the Year '+str(Year)+' the '+Mode+" pattern in all states ",color_continuous_scale="peach",)
st.plotly_chart(fig2) 
st.info('**:red[The above bar graph shows the total number of transactions happened in a particular payment mode in all states]**')
# -------------------------------------------FIGURE5 PIE------------------------------------------------------------
st.write('### :blue[Drastical Increase in Transactions :rocket:]')
years=Data_Aggregated_Transaction.groupby('Year')
years_List=Data_Aggregated_Transaction['Year'].unique()
years_Table=years.sum()
del years_Table['Quarter']
years_Table['year']=years_List
total_trans=years_Table['Total_Transactions_count'].sum() # this data is used in sidebar
st.markdown(years_Table.style.hide(axis="index").to_html(), unsafe_allow_html=True)
fig1 = px.pie(years_Table, values='Total_Transactions_count', names='year', title='Total Transactions count in different years')
st.plotly_chart(fig1)
st.info('**:blue[The above pie chat shows how the online payments are drastically increased with time.Initially in 2018,2019 the transactions are less but with time the online payments are increased at a high scale via PhonePe. We can clearly see that more than 50% of total Phonepe transactions in india happened are from the year 2022 ]**')


#----------------------------------------FIGURE6 DONUT CHAT----------------------------------
st.write('# :orange[USERS DATA ANALYSIS ]')
st.write('### :orange[Brand Share] ')
state = st.selectbox(
    'Please select the State',
    ('india','andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
       'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
       'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
       'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
       'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'),key='Z')
Y = st.selectbox(
    'Please select the Year',
    ('2018', '2019', '2020','2021','2022'),key='X')
y=int(Y)
s=state
brand=Data_Aggregated_User_df[Data_Aggregated_User_df['Year']==y] 
brand=Data_Aggregated_User_df.loc[(Data_Aggregated_User_df['Year'] == y) & (Data_Aggregated_User_df['State'] ==s)]
myb= brand['Brand_Name'].unique()
x = sorted(myb)
b=brand.groupby('Brand_Name').sum()
b['brand']=x
br=b['Registered_Users_Count'].sum()
labels = b['brand']
values = b['Registered_Users_Count']
fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4,customdata=labels,textinfo='label+percent',texttemplate='%{label}<br>%{percent:1%f}',insidetextorientation='horizontal',textfont=dict(color='#000000'),marker_colors=px.colors.qualitative.Prism)])
st.plotly_chart(fig3)
st.info('**:orange[The above donut chat and below bar graph shows how the users are registered through different brans in india. We can also see which brand has more users and the brand with less users  ]**')
#---------------------------------------------------FIGURE7 BAR-------------------------------------------------------------
b = b.sort_values(by=['Registered_Users_Count'])
fig4= px.bar(b, x='brand', y='Registered_Users_Count',color="Registered_Users_Count",
            title='In '+state+' the Brand Share distribution in '+str(y),
            color_continuous_scale="oranges",)
st.plotly_chart(fig4) 
# --------------------------------------------------FIGURE8 BAR-------------------------------------------
st.write('### :blue[State & Userbase]')
state = st.selectbox(
    'Please select the State',
    ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
       'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
       'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
       'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
       'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'),key='W')
app_opening=Data_Aggregated_User_Summary_df.groupby(['State','Year'])
a_state=app_opening.sum()
la=Data_Aggregated_User_Summary_df['State'] +"-"+ Data_Aggregated_User_Summary_df["Year"].astype(str)
a_state["state_year"] = la.unique()
sta=a_state["state_year"].str[:-5]
a_state["state"] = sta
sout=a_state.loc[(a_state['state'] == state) ]
ta=sout['AppOpenings'].sum()
tr=sout['Registered_Users'].sum()
sout['AppOpenings']=sout['AppOpenings'].mul(100/ta)
sout['Registered_Users']=sout['Registered_Users'].mul(100/tr)
fig = go.Figure(data=[
    go.Bar(name='AppOpenings %', y=sout['AppOpenings'], x=sout['state_year']),
    go.Bar(name='Registered Users %', y=sout['Registered_Users'], x=sout['state_year'])
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(fig)
st.info('**:blue[This bar graph tells how the user base is created in particular state with respect to app openings and Registered users  ]**')
# -----------------------------------------------------SIDEBAR CODE--------------------------------------------------------
with st.sidebar:  
    st.title(':green[Top states contributing to PhonePe]')
    Data_Map_User_df=Data_Aggregated_User_Summary_df.copy() 
    # st.metric(label="TOTAL TRANSACTIONS BY INDIANS TILL NOW", value=total_t)
    year = st.selectbox(
    'Please select the Year',
    ('2022','2021','2020','2019','2018'), key='yb')
    quarter = st.selectbox(
    'Please select the Quarter',
    ('4','3','2','1'),key='qb')
    opt = st.selectbox(
    'Please select any option',
    ('AppOpenings','Registered Users'),key='ob')
    top_states=Data_Map_User_df.loc[(Data_Map_User_df['Year'] == int(year)) & (Data_Map_User_df['Quarter'] ==int(quarter))]
    top_states_r = top_states.sort_values(by=['Registered_Users'], ascending=False)
    top_states_a = top_states.sort_values(by=['AppOpenings'], ascending=False)  
    if opt=='Registered Users':
        rt=top_states_r[1:6]
        st.markdown("# :green[Top 5 States With Highest Registered Users in "+year+" Q"+quarter+" :curly_haired_man::curly_haired_woman:]")
        st.markdown(rt[[ 'State','Registered_Users']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
    if opt=='AppOpenings':
        at=top_states_a[1:6]
        st.markdown("# :orange[Top 5 States With Highest PhonePeApp Openings in "+year+" Q"+quarter+" :iphone:]")
        st.markdown(at[['State','AppOpenings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
   



