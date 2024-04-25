#Sep 2023

import streamlit as  st
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import altair as alt
#from PIL import Image


#Read data from for laptop
#athlete_df=pd.read_csv(r'C:\Users\HP\Desktop\streamlit\Project-1\athlete_events.csv')
#noc_df=pd.read_csv(r'C:\Users\HP\Desktop\streamlit\Project-1\noc_regions.csv')
athlete_df=pd.read_csv(r'athlete_events1.csv')
noc_df=pd.read_csv('noc_regions.csv')

#---------------------------------For Data Cleaning---------------------------------#
athlete_df.isna().any()

athlete_df['Age'].isnull().value_counts()

a1= athlete_df[athlete_df['Age'].isnull()]

athlete_df['Age'].describe()
athlete_df['Height'].describe()
athlete_df['Weight'].describe()

avg = athlete_df['Age'].mean()
athlete_df['Age'].fillna(avg, inplace = True)
athlete_df['Age'].isnull().value_counts()

avg1 = athlete_df['Height'].mean()
athlete_df['Height'].fillna(avg1, inplace = True)
athlete_df['Height'].isnull().value_counts()

avg2 = athlete_df['Weight'].mean()
athlete_df['Weight'].fillna(avg2, inplace = True)
athlete_df['Weight'].isnull().value_counts()

athlete_df['Medal'].fillna("No Medal", inplace = True)
athlete_df['Medal'].isnull().value_counts()

athlete_df.isnull().any()
#Our athlete data has not any null value now
athlete_df.duplicated().value_counts()
athlete_df.drop_duplicates(inplace = True)
athlete_df.duplicated().value_counts()
#Our athlete data has been clean now

noc_df.isna().any()
noc_df['region'].fillna("N.A",inplace = True)
noc_df['notes'].fillna("N.A",inplace = True)
noc_df.duplicated().any()
#False

#Now we are merging both dataframes
df1 = pd.DataFrame(athlete_df)
df2 = pd.DataFrame(noc_df)

newdf = df1.merge(df2, how="left")
newdf.isna().any()
newdf['region'].fillna("N.A",inplace = True)
newdf['notes'].fillna("N.A",inplace = True)
newdf.isna().any()
newdf.duplicated().any()
#False

#---------------------------------Data Cleaning END---------------------------------#

#----------------------------Basic EDA related to athlete---------------------------#
# Q1- Some most famous sports name in olymics?
athlete_df['Sport'].value_counts().head(10)
#Athletics               38624
#Gymnastics              26707
#Swimming                23195
#Shooting                11448
#Cycling                 10827
#Fencing                 10735
#Rowing                  10595
#Cross Country Skiing     9133
#Alpine Skiing            8829
#Wrestling                7154
#Name: Sport, dtype: int64

# Q2- Name of the Olympic sports
athlete_df['Sport'].unique()
#array(['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Speed Skating',
#       'Cross Country Skiing', 'Athletics', 'Ice Hockey', 'Swimming',
#       'Badminton', 'Sailing', 'Biathlon', 'Gymnastics',
#       'Art Competitions', 'Alpine Skiing', 'Handball', 'Weightlifting',
#       'Wrestling', 'Luge', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh',
#       'Fencing', 'Equestrianism', 'Shooting', 'Boxing', 'Taekwondo',
#       'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Modern Pentathlon',
#       'Figure Skating', 'Golf', 'Softball', 'Archery', 'Volleyball',
#       'Synchronized Swimming', 'Table Tennis', 'Nordic Combined',
#       'Baseball', 'Rhythmic Gymnastics', 'Freestyle Skiing',
#       'Rugby Sevens', 'Trampolining', 'Beach Volleyball', 'Triathlon',
#       'Ski Jumping', 'Curling', 'Snowboarding', 'Rugby',
#       'Short Track Speed Skating', 'Skeleton', 'Lacrosse', 'Polo',
#       'Cricket', 'Racquets', 'Motorboating', 'Military Ski Patrol',
#       'Croquet', 'Jeu De Paume', 'Roque', 'Alpinism', 'Basque Pelota',
#      'Aeronautics'], dtype=object)

# Q3- Which team participates the most?
athlete_df['Team'].value_counts()

a2= athlete_df[athlete_df['Team']=="United States"]
#United States    17598
#France           11817
#Great Britain    11264
#Italy            10213
#Germany           9230
#                 ...  
#Souriceau-38         1
#Carabinier-5         1
#Ducky-4              1
#Ducky-16             1
#Digby                1
#Name: Team, Length: 1184, dtype: int64
#17598 rows × 15 columns

#Q4- Which gender participates more, male or female?
athlete_df['Sex'].value_counts()
X= athlete_df['Sex'].value_counts()

round((X/athlete_df['Sex'].count()) * 100,2)
#M    195353
#F     74378
#Name: Sex, dtype: int64 

#data in term of %
#      Name
#Sex       
#M    72.89
#F    27.63 %

#Q5- Can we have players physical details in terms of height & weight?
athlete_df[['Height','Weight']].describe()
#	    Height	            Weight
#count	269731.000000	269731.000000
#mean	175.338957	    70.701918
#std	9.301313	    12.606697
#min	127.000000	    25.000000
#25%	170.000000	    63.000000
#50%	175.338970	    70.702393
#75%	180.000000	    76.000000
#max	226.000000	    214.000000
#---------------------------------EDA END---------------------------------#

#---------------------------------STREAMLIT APP VISUAL---------------------------------#
st.set_page_config(layout="wide")

with st.container():
    col1,col2= st.columns(spec=[0.5,0.5], gap="small")
    
    with col1:
        st.image("https://cdn.britannica.com/44/190944-131-7D082864/Silhouette-hand-sport-torch-flag-rings-Olympic-February-3-2015.jpg",
            width=600,) # Manually Adjust the width of the image as per requirement)
    
    with col2:
        st.title('HISTORY DASHBOARD FOR OLYMPIC GAMES')        
        st.header('Project Owner: Mr.Saad Ahmed Masood')
        st.subheader('Project Outline:')
        st.write('Using a data collection from Kaggle, this dashboard can be useful for visualising information about the Olympics by a selection of countries.')

overall_Regn = sorted(newdf['region'].unique())
selected_Regn= st.selectbox('Kindly select any country', overall_Regn)
sub_regn= newdf[newdf['region']== selected_Regn]
participants= sub_regn['Name'].nunique()

sub_bronze = newdf[(newdf['region']== selected_Regn) & (newdf['Medal']=='Bronze')]
bronze=sub_bronze['Medal'].count()

sub_silver = newdf[(newdf['region']== selected_Regn) & (newdf['Medal']=='Silver')]
silver=sub_silver['Medal'].count()

sub_gold = newdf[(newdf['region']== selected_Regn) & (newdf['Medal']=='Gold')]
gold=sub_gold['Medal'].count()

medal_got= newdf[(newdf['region']==selected_Regn)&(newdf['Medal']!='No Medal')]

Bar=medal_got.groupby('Name').agg(Total_Medals_Won=('Medal','count')).head(10)
Table=medal_got.groupby('Name')[['Medal']].count().sort_values(by='Medal', ascending= False).head(10)
Hist_var = medal_got['Age'].value_counts()
medal_name= medal_got.groupby('Name')['Name'].count().sort_values(ascending=False).head(10)
season_medal=medal_got.groupby('Season')['Medal'].count().head(10)

col1,col2,col3,col4 = st.columns(4)
col1.metric('Bronze Medals', bronze)
col2.metric('Silver Medals',silver)
col3.metric('Gold Medals', gold)
col4.metric('Total Participants', participants)

with st.container():
    Y,Z= st.columns(spec=[0.4,0.6], gap="small")            # To ADD Line-Graph,Z,Y,X= st.columns(3)   
    gold_var = sub_gold.groupby('Year').agg(Gold=('Medal','count'))
    silver_var =sub_silver.groupby('Year').agg(Silver=('Medal','count'))
    bronze_var =sub_bronze.groupby('Year').agg(Bronze=('Medal','count'))
    
    #line= pd.concat([gold_var, silver_var, bronze_var],1)
    #X.header('Medals earn over time')
    #X.line_chart(line)
    
    fig, ax=plt.subplots(figsize=(10,10))  # values in parathensis can be adjust to resize image
    #color=['teal','cyan','gold','coral','tan','violet','brown','orange','maroon','red']
    ax= plt.barh(medal_name.index, medal_name.values, color=sns.color_palette("Spectral",len(medal_name.index)))
    plt.xlabel('Numbers of Medals')
    Y.header('Leading Ten Medalists')
    Y.pyplot(fig)
    Z.header('Legendary Hall')
    Z.table(Table)
    
with st.container():
    S,T,U = st.columns(3)
    
    fig=plt.figure(figsize=(10,10)) # values in parathensis can be adjust to resize image
    sns.histplot(newdf, x='Age',bins=15,color="teal")
    #sns.barplot(newdf, x='Age',bins=15, color = 'muted')
    S.header('Age & Medal')
    S.pyplot(fig)
    gender= newdf.groupby(['Medal','Sex'])['Sex'].count()
    
    fig1, ax1 = plt.subplots()
    ax1.pie(gender, labels = gender.index, autopct='%1.1f%%',shadow=False, startangle=0) #startangle value can be set to adject image position
    ax1.axis('equal')  # A pie with an equal aspect ratio is drawn as a circle.#
    T.header('Gender-Based Winner')
    T.pyplot(fig1)
    
    figb = plt.figure(figsize=(5,5))
    sns.barplot(x=season_medal.index,y=season_medal.values, alpha=0.7) # graph can be light/dark by change value of alpha min=0, max=1
    U.header('Seasonal Successes')
    U.pyplot(figb)
#------------------------------------------END------------------------------#