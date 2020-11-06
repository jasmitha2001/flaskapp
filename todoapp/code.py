import requests
def weather_report(cityname):
    cityname=cityname.strip();
    try:
        response=requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cityname+"&units=metric&appid=0941ecd2acfb0f26b09f7b3ddbb438cf")
        data=response.json()
    except:
        data={'message':"City not found"}
    return data

def corona_updates(countryname):
    countryname=countryname.strip();
    try:
        response=requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+countryname)
        data=response.json()
    except:
        data={'message':"Country not found"}
    return data

def evaluate_expression(expr):
    try: 
        data=eval(expr)
    except Exception as e:
        data="wrong"
    return data