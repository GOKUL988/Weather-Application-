from django.shortcuts import render 
from django.shortcuts import redirect
import requests
# Create your views here.
def home(request): 
    search_city = request.GET.get("search") 
    search_bar = True
    if search_city: 
        return redirect('main.html',search_city= search_city)
    return render(request, "home.html", {'search_but' : search_bar}) 

def main(request,search_city):
    notif= False
    search_bar = True
    if search_city: 
        key = 'f4676baa4de740c2a93125752252607' 
        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={search_city}"   
        days = 7 
        url_2 = f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={search_city}&days={days}"
        outdata = requests.get(url).json() 
        out_data = requests.get(url_2).json()   
        if 'location' not in outdata: 
            notif= True  
            search_bar= False
            return render(request, 'home.html', {'notif': notif, 'search_bar': search_bar}) 
    else: 
        return redirect("home") 
        notif= True    
    
    context = {
        'city' : outdata['location']['name'], 
        'date' : outdata['location']['localtime'],
        'region' : outdata['location']['region'], 
        'country' : outdata['location']['country'] ,
        'id': outdata['location'] ['tz_id'], 
        'temp_cel' : outdata['current']['temp_c'], 
        'temp_fa': outdata['current']['temp_f'],  
        'condition_text' : outdata['current']['condition']['text'], 
        'condition_icon':outdata['current']['condition']['icon'], 
        'wind_kph' : outdata['current']['wind_kph'] ,
        'humidity' : outdata['current']['humidity'], 
        'cloud':outdata['current']['cloud'], 
        'uv' : outdata['current']['uv'], 
        'vis_km' : outdata['current']['vis_km'],  
        'notif': notif,      
        'forecast' : out_data,            
    }

    return render(request, "main.html", context)  