from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import sklearn
import joblib
import pandas as pd
from pathlib import Path
import os


def home(request):
    # Get the project root directory (parent of flightprice package)
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODEL_PATH = BASE_DIR / "f_model.sav"
    
    try:
        final_model = joblib.load(MODEL_PATH)
    except Exception as e:
        return render(request, "index.html", {"error": f"Model loading failed: {str(e)}"})

    if request.method == "POST":
        try:
            # Date_of_Journey
            date_dep = request.POST.get("Dep_Time")
            travel_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
            travel_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

            # Departure
            dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
            dep_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

            # Arrival
            date_arr = request.POST.get("Arrival_Time")
            arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
            arrival_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

            # Duration
            duration_hours = abs(arrival_hour - dep_hour)
            duration_minute = abs(arrival_minute - dep_minute)

            # Total Stops
            Stops = int(request.POST.get("stops"))

            # Airline mapping
            airline = request.POST.get('airline')
            airlines = ['Ryanair', 'Lufthansa', 'easyJet', 'Vueling', 'KLM', 'LOT', 
                       'British_Airways', 'Iberia', 'Norwegian', 'SWISS', 'Austrian_Airlines',
                       'Wizz_Air', 'Eurowings', 'Air_France', 'ITA_Airways', 'Finnair',
                       'Transavia_France', 'Multiple_Airlines', 'Smartwings', 'Air_Europa']
            
            airline_dict = {a: (1 if a == airline else 0) for a in airlines}

            # Source mapping
            Source = request.POST.get("Source")
            sources = ['Warsaw', 'Oslo', 'Prague', 'Berlin', 'Rome', 'Amsterdam', 'Paris', 'Barcelona', 'London']
            source_dict = {f's_{s}': (1 if s == Source else 0) for s in sources}

            # Destination mapping
            Destination = request.POST.get("Destination")
            dest_dict = {f'd_{s}': (1 if s == Destination else 0) for s in sources}

            # Build prediction input
            prediction = final_model.predict([[
                Stops,
                travel_day,
                travel_month,
                dep_hour,
                dep_minute,
                arrival_hour,
                arrival_minute,
                duration_hours,
                duration_minute,
                airline_dict['Ryanair'],
                airline_dict['Lufthansa'],
                airline_dict['easyJet'],
                airline_dict['Vueling'],
                airline_dict['KLM'],
                airline_dict['LOT'],    
                airline_dict['British_Airways'],
                airline_dict['Iberia'],
                airline_dict['Norwegian'],
                airline_dict['SWISS'],
                airline_dict['Austrian_Airlines'],
                airline_dict['Wizz_Air'],
                airline_dict['Eurowings'],             
                airline_dict['Air_France'],           
                airline_dict['ITA_Airways'],          
                airline_dict['Finnair'],             
                airline_dict['Transavia_France'],       
                airline_dict['Multiple_Airlines'],     
                airline_dict['Smartwings'],        
                airline_dict['Air_Europa'],
                source_dict['s_Warsaw'],
                source_dict['s_Oslo'],
                source_dict['s_Prague'],
                source_dict['s_Berlin'],
                source_dict['s_Rome'],
                source_dict['s_Amsterdam'],
                source_dict['s_Paris'],
                source_dict['s_Barcelona'],
                source_dict['s_London'],
                dest_dict['d_Warsaw'],
                dest_dict['d_Oslo'],
                dest_dict['d_Prague'],
                dest_dict['d_Berlin'],
                dest_dict['d_Rome'],
                dest_dict['d_Amsterdam'],
                dest_dict['d_Paris'],
                dest_dict['d_Barcelona'],
                dest_dict['d_London'],
            ]])

            output = round(prediction[0], 2)
            prediction_text = "Your Ticket Price is $ {}".format(output)
            
            return render(request, "index.html", {"price": prediction_text})
        
        except Exception as e:
            return render(request, "index.html", {"error": f"Prediction failed: {str(e)}"})

    return render(request, "index.html")

