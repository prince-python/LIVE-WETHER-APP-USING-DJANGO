from django.shortcuts import render,HttpResponse
import requests




def index(request):
    city='Indore'
    url=f"https://api.weatherapi.com/v1/current.json?key=1a117971724c4a94932100112230704&q={city}"
    data=requests.get(url).json()
    temp=data['current']['temp_c']
    ico=data['current']['condition']['icon']
    icon=f"http:{ico}"
    text=data['current']['condition']['text']
    location=data['location']['name']
    region=data['location']['region']
    country=data['location']['country']
    lastupdate=data['current']['last_updated']
    return render(request,'index.html',{'location':location,'temp':temp,'region':region,'country':country,'lastupdate':lastupdate,'icon':icon,'text':text})

def get(request):
    city=request.POST['city']
    try:
        url=f"https://api.weatherapi.com/v1/current.json?key=1a117971724c4a94932100112230704&q={city}"
        data=requests.get(url).json()
        temp=data['current']['temp_c']
        ico=data['current']['condition']['icon']
        icon=f"http:{ico}"
        text=data['current']['condition']['text']
        location=data['location']['name']
        region=data['location']['region']
        country=data['location']['country']
        lastupdate=data['current']['last_updated']
        return render(request,'index.html',{ 'text':text,'location':location,'temp':temp,'region':region,'country':country,'lastupdate':lastupdate,'icon':icon})

    except:
        return HttpResponse("<center><h1>city not found go back and try check again</h1></center>")
