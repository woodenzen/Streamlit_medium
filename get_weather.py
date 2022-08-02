from urllib.request import urlopen
import json

api_key = '6ea23923b64d0a887f767d1e271567e9'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "moscow"
state_id = "id"
country_code = "us"
complete_url = base_url + "&q=" + city_name + "," + state_id + "," + country_code + "&appid=" + api_key + "&units=imperial" + "&city.sun.rise" + "&city.sun.set"
url = complete_url
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
print(data_json)
x = data_json

#GLOBALS

y = x["main"]
print(y)
current_temp = round((y["temp"]))
max_temp = round((y["temp_max"]))
min_temp = round(y["temp_min"])
humidity = y["humidity"]
pressure = y["pressure"]
feels = round((y["feels_like"]))
previous_temp = 23

def temp_difference():
    global previous_temp
    #Getting percentage of difference between old and new temp
    change_percent = ((float(current_temp) - max_temp) / max_temp) * 100
    #To int instead of float
    change_percent = int(change_percent)
    print(change_percent)

    if previous_temp > current_temp:
        return str(change_percent)


    # if its an increase we add a + symbol.
    if previous_temp < current_temp:
        return "+" + str(change_percent)


    if change_percent == 0:
        return "0"




def get_temp():
    return(str(current_temp)+" °F")


def get_temp_min():
    return(str(min_temp)+" °F")


def get_temp_max():
    return(str(max_temp)+" °F")

def get_humidity():
    return(str(humidity))

def get_pressure():
    return(str(pressure))

def get_feel():
    return(str(feels)+"°F")