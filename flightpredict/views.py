from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import sklearn
import joblib
import pandas as pd



# def home(request):
#     return render(request, "index.html")


def home(request):

    final_model = joblib.load('f_model.sav')
    

    if request.method == "POST":
  
        # Date_of_Journey
        date_dep = request.POST.get("Dep_Time")
        travel_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        travel_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        dep_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.POST.get("Arrival_Time")
        arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        arrival_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        duration_hours = abs(arrival_hour - dep_hour)
        duration_minute = abs(arrival_minute - dep_minute)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Stops = int(request.POST.get("stops"))
        # print(Total_stops)

        # Airline
        airline=request.POST.get('airline')
        if(airline=='Ryanair'):
            Ryanair = 1
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Lufthansa'):
            Ryanair = 0
            Lufthansa = 1
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0         
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='easyJet'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 1
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0
            
        if(airline=='Vueling'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 1
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0
            
        if(airline=='KLM'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 1
            LOT = 0
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0 
            
        if(airline=='LOT'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 1
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='British_Airways'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 1
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Iberia'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0       
            British_Airways = 0
            Iberia = 1
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Norwegian'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0        
            British_Airways = 0
            Iberia = 0
            Norwegian = 1
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='SWISS'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 1
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0
            
        if(airline=='Austrian_Airlines'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0      
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 1
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Wizz_Air'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 1
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0
          
        if(airline=='Eurowings'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            SWISS = 0
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            KLM = 0
            LOT = 0      
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 1            
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0    

        if(airline=='Air_France'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0      
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 1           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='ITA_Airways'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0         
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 1          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0
       
        if(airline=='Finnair'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0           
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 1             
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Transavia_France'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 1       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Multiple_Airlines'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0           
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 1    
            Smartwings = 0            
            Air_Europa = 0

        if(airline=='Smartwings'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0          
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 1            
            Air_Europa = 0

        if(airline=='Air_Europe'):
            Ryanair = 0
            Lufthansa = 0
            easyJet = 0
            Vueling = 0
            KLM = 0
            LOT = 0           
            British_Airways = 0
            Iberia = 0
            Norwegian = 0
            SWISS = 0
            Austrian_Airlines = 0
            Wizz_Air = 0
            Eurowings = 0             
            Air_France = 0           
            ITA_Airways = 0          
            Finnair = 0              
            Transavia_France = 0       
            Multiple_Airlines = 0     
            Smartwings = 0            
            Air_Europa = 1

        # Departure
        Source = request.POST.get("Source")
        if (Source == 'Warsaw'):
            s_Warsaw = 1
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Oslo'):
            s_Warsaw = 0
            s_Oslo = 1
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Prague'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 1
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Berlin'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 1
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Rome'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 1
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Amsterdam'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 1
            s_Paris = 0
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Paris'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 1
            s_Barcelona = 0
            s_London = 0

        if (Source == 'Barcelona'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 1
            s_London = 0                        

        if (Source == 'London'):
            s_Warsaw = 0
            s_Oslo = 0
            s_Prague = 0
            s_Berlin = 0
            s_Rome = 0
            s_Amsterdam = 0
            s_Paris = 0
            s_Barcelona = 0
            s_London = 1

        # Arrival

        Source = request.POST.get("Destination")
        if (Source == 'Warsaw'):
            d_Warsaw = 1
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0
        
        if (Source == 'Oslo'):
            d_Warsaw = 0
            d_Oslo = 1
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Prague'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 1
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Berlin'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 1
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Rome'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 1
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Amsterdam'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 1
            d_Paris = 0
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Paris'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 1
            d_Barcelona = 0
            d_London = 0

        if (Source == 'Barcelona'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 1
            d_London = 0

        if (Source == 'London'):
            d_Warsaw = 0
            d_Oslo = 0
            d_Prague = 0
            d_Berlin = 0
            d_Rome = 0
            d_Amsterdam = 0
            d_Paris = 0
            d_Barcelona = 0
            d_London = 1

    # ['transfer_stops', 'travel_day',
    #    'dep_hour', 'dep_minute', 'arrival_hour', 'arrival_minute',
    #    'duration_hours', 'duration_minute', 'airline_names_Air France',
    #    'airline_names_Austrian Airlines', 'airline_names_British Airways',
    #    'airline_names_Eurowings', 'airline_names_Finnair',
    #    'airline_names_ITA Airways', 'airline_names_Iberia',
    #    'airline_names_KLM', 'airline_names_LOT', 'airline_names_Lufthansa',
    #    'airline_names_Multiple Airlines',
    #    'airline_names_Norwegian', 'airline_names_Ryanair',
    #    'airline_names_SWISS', 'airline_names_Smartwings',
    #    'airline_names_TAP AIR PORTUGAL', 'airline_names_Transavia France',
    #    'airline_names_Volotea', 'airline_names_Vueling',
    #    'airline_names_Wizz Air', 'airline_names_easyJet', 'dep_city_Barcelona',
    #    'dep_city_Berlin', 'dep_city_London', 'dep_city_Oslo', 'dep_city_Paris',
    #    'dep_city_Prague', 'dep_city_Rome', 'dep_city_Warsaw',
    #    'arrival_city_Barcelona', 'arrival_city_Berlin', 'arrival_city_London',
    #    'arrival_city_Oslo', 'arrival_city_Paris', 'arrival_city_Prague',
    #    'arrival_city_Rome', 'arrival_city_Warsaw']]    


        prediction=final_model.predict([[
            Stops,
            travel_day,
            travel_month,
            dep_hour,
            dep_minute,
            arrival_hour,
            arrival_minute,
            duration_hours,
            duration_minute,
            Ryanair,
            Lufthansa,
            easyJet,
            Vueling,
            KLM,
            LOT,    
            British_Airways,
            Iberia,
            Norwegian,
            SWISS,
            Austrian_Airlines,
            Wizz_Air,
            Eurowings,             
            Air_France,           
            ITA_Airways,          
            Finnair,             
            Transavia_France,       
            Multiple_Airlines,     
            Smartwings,        
            Air_Europa,
            s_Warsaw,
            s_Oslo,
            s_Prague,
            s_Berlin,
            s_Rome,
            s_Amsterdam,
            s_Paris,
            s_Barcelona,
            s_London,
            d_Warsaw,
            d_Oslo,
            d_Prague,
            d_Berlin,
            d_Rome,
            d_Amsterdam,
            d_Paris,
            d_Barcelona,
            d_London,
        ]])

        output=round(prediction[0],2)
        prediction_text="Your Ticket Price is $ {}".format(output)
        
        return render(request, "index.html", {"price":prediction_text})

    return render(request, "index.html")
   
   