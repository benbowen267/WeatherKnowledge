import streamlit as st
import datetime
import urllib.request as urllib2
#from bs4 import BeautifulSoup
import pandas as pd
import lxml
import matplotlib as plot
from PIL import Image
import subprocess
from subprocess import check_output
import pytz


def app():
    def get_todays_date():
        tz = pytz.timezone('Australia/Sydney')
        now = datetime.datetime.now(tz)
        
        today = str(now)
        today = today[0:16]
       
        ReturnString_1 = "Date and time is " + today
        return (ReturnString_1)

    col1, col2 = st.beta_columns([2.5,10])

    with col1:
        st.image('unnamed.png')

    with col2:
        st.title("SHARED PATH ABORIGINAL AND TORRES STRAIT ISLANDER CORPORATION")

    st.title('Welcome to the Indigenous Weather Knowledges App')
    st.write('Yaama, minya gaba nginda?')
    st.write('Here at the Indigenous Weather Knowledges App we celebrate the traditional knowledges and lore that is the product of tens of thousands of years of scientific observations and custodianship')
    date = get_todays_date()

    st.write(date)

    def Weather_Now():
        df0 = pd.read_html('https://www.weatherzone.com.au/nsw/sydney/sydney', header=0)
        df0[1].pop("Unnamed: 1") #remove unused coloumns
        df0[1].pop("Unnamed: 3") #remove unused coloumns
        df0[2].pop("Unnamed: 1")
    #layer two of data
        df1 = pd.read_html('https://www.weatherzone.com.au/nsw/sydney/sydney',header=1)
        df1[1].pop("Unnamed: 1") #remove unused coloumns
        df1[1].pop("Unnamed: 3") #remove unused coloumns
        df1[2].pop("Unnamed: 1")
    #layer three of data
    
    
        return df0[1].columns.values.tolist()+df1[1].columns.values.tolist()+ df0[0].columns.values.tolist()+ df1[0].columns.values.tolist()+ df0[0].columns.values.tolist()+ df1[0].columns.values.tolist()
    def Weather_Now1():
    #data= []
        dfs = pd.read_html('https://www.weatherzone.com.au/nsw/sydney/sydney',header=1)
    #for df in dfs:
   
        output_2= dfs[1] #table of details
        output_2.pop('Unnamed: 1')
        output_2.pop('Unnamed: 3')
        new_header = output_2.iloc[0] #grab the first row for the header
        df = output_2[1:] #take the data less the header row
        df.columns = new_header
        return df


    weatherNow1= Weather_Now1()
    weatherNow= Weather_Now()


    daytemp= (weatherNow[1])
    daytemp= float(daytemp[:-2])
    nighttemp = (weatherNow[3])
    nighttemp= float(nighttemp[:-2])
    nowtemp= (weatherNow[5])
    nowtemp= nowtemp.strip('°C')
    nowtemp=float(nowtemp)
    dewpoint= (weatherNow[7])
    dewpoint= dewpoint.strip('°C')
    dewpoint=float(dewpoint)
    sunrise= (weatherNow[9])
    sunrise=sunrise.strip('EDT')
#sunrise= float(sunrise)
    sunset= (weatherNow[11])
    sunset=sunset.strip('EDT')
#sunset=float(sunset)
#daylighthrs= (sunset-sunrise)

    FeelsLike= str(weatherNow1[0:1])
    FeelsLike= FeelsLike[20:23]
    FeelsLike= float(FeelsLike)
    Humidity= str(weatherNow1[0:1])
    Humidity= Humidity[52:-1]
    #Humidity=float(Humidity)
    WindDir= str(weatherNow1[1:2])
    WindDir=WindDir[-9:-4]
    WindSpd= str(weatherNow1[1:2])
    WindSpd=WindSpd[-6:-4]
#WindSpd= float(WindSpd)
    WindGst= str(weatherNow1[2:3]) 
    WindGst= WindGst[-6:-4]    
#WindGst= float(WindGst)
    Pressure= str(weatherNow1[3:4])  
    Pressure=Pressure[-10:-3]
#Pressure=float(Pressure)  
    FireDanger= str(weatherNow1[4:5])  
    FireDanger=FireDanger[-4:]
    FireDanger= float(FireDanger)       
    Rainsince9am= str(weatherNow1[5:6])
    Rainsince9am=Rainsince9am[-10:-6]


    para = ['Day Temp C','Night Temp C','Now Temp C','Feels Like C', 'Humidity %','Pressure hPa', 'Fire Danger', "Rain Since 9am"]
    values=[daytemp, nighttemp, nowtemp, FeelsLike, Humidity, Pressure, FireDanger, Rainsince9am]
    my_series = pd.Series(values, para)

    df1 = my_series.to_frame()
    df1= pd.DataFrame(df1)
    df1.columns = ["Value"]

    st.write("Today we are looking at Sydney's forecast through the lens of the Dharrawal 6 seasons")
    #st.write(df1)

    col1, col2 = st.beta_columns([10,10])

    with col1:
        st.write(df1)
        #season predictor
        today = datetime.datetime.now()
        month = str(today.month)
        if month == "6" or "7":
            st.title("We are in the Burrugin Season")
            st.write("This is the time when the male Burrugin form lines of up to ten as they follow the female through the woodlands in an effort to wear her down and mate with her. It is also the time when the Burringoa starts to produce flowers, indicating that it is time to collect the nectar of certain plants for the ceremonies. It is also a warning not to eat shellfish.")

        elif month == "7" or "8":
            st.write('Wiritjiribin Cold and Windy')
        elif month == "9" or "10":
            st.write('Ngoonungi Cool Becoming Warm'
        elif month == "11" or "12":
            st.write("Parra'dowee Warm and Wet")
        elif month == "1" or "2" or "3":
            st.write('Burran Hot and Dry')
        elif month == "4" or "5" or "6":
            st.write("Marrai'gang Wet Becoming Cool')
        
    with col2:
        st.image('Seasons.JPG')
   
    def WeatherForecasting():
        content = pd.read_html('https://www.weatherzone.com.au/nsw/sydney/sydney/detailed-forecast', header=0)
        DF= content[0]
        DF.pop("Weather")
        DF.pop("Wind")
        DF.columns = ["Time of Day", "Weather Conditions", "Temperature", "Chance of Rain", "Cloud Cover", "Wind Direction & Speed", "Dew Point", "Humidity"]
        DF= DF.set_index('Time of Day')
        DF= DF.iloc[:9,:]
        return(DF)
        
     
    Forecastdata = WeatherForecasting()
    st.write(Forecastdata)
    Forecastdata.pop("Weather Conditions")
    Forecastdata.pop("Chance of Rain")
    Forecastdata.pop("Wind Direction & Speed")
    Forecastdata.pop("Humidity")
    Forecastdata.pop("Cloud Cover")
    st.line_chart(Forecastdata[1:4])
    
   

    
 



#WRITE A FILE AND STORE DATA NOT CALLING FUNCTION AT THE MOMENT
    def log_day_data(date, df1):
        filename= open('.vscode\datafileSYD.txt', 'a')
        filename.write('-------------------------------------- \n')
        filename.write(str(date))
        filename.write("\n")
    

        filename.write(str(df1))
        filename.write("\n")
        filename.close()
        filename= open('.vscode\datafileSYD.txt', 'r')
        Logdata= filename.readlines()[-20:]
    #logdataframe = pd.DataFrame(Logdata)
    
        filename.close()
        return(Logdata)
    #print ('Data logged')

#log_data=log_day_data(date, df1)
