import requests
from datetime import datetime

api_key = '0f06c421d290e8abc5f2ada2d17b1f6c'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %H:%M:%S")
clouds = api_data['clouds']['all']
weather_id = api_data['weather'][0]['id']
pr = api_data ['main']['pressure']

print ("-------------------------------------------------------------")
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<0>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print ("-------------------------------------------------------------")

print ("Weather Stats for - \n                        |  {}  |      \n                 | {}".format(location.upper(), date_time))

print ()

print ("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")
                                                                    
print ()

print ("Current temperature is       : {:.2f} deg C".format(temp_city))
print ("Current weather desc         :",weather_desc)

print ()

if (233> weather_id >=200):
  print ("⚠️⚡ Thunderstorm warning ⚡⚠️")
elif (322> weather_id >=300):
  print ("Take an umbrella with you ")
elif (532> weather_id >=500):
  print ("Dont foget your umbrella!!!")
elif (623 > weather_id >=600):
  print ("Dont fogrt your winter kits its freezing!")
elif (782> weather_id >=701):
  print ("Mind your step !!")
elif (801> weather_id >=800):
  print ("Enjoy the clear sky")
elif (805> weather_id >=801):
  print("Its better not to plan watching stars in night :)")

print()

print ("Current cloudiness           :",clouds,'%' )
print ("Current Humidity             :",hmdt, '%')

print()

if (hmdt < 50 ):
  print ("water vapour in the atmosphere is less than 50% use more water")
else:
  print ("water vapour in the atmosphere is good")

print ()

print ("Current wind speed           :",wind_spd ,'kmph')
print ("Current Atmospheric pressure :",pr,'hPa')

print()
                                                                      
print("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")





txtlist = [temp_city,weather_desc,clouds,hmdt,wind_spd,pr,date_time,weather_id]

with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :     
    f.write("-------------------------------------------------------------\n")
    f.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<0>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    f.write("-------------------------------------------------------------\n")
    
    f.write("\n")
    
    f.write("Weather Stats for - \n                        |  {}  |      \n                 | {}".format(location.upper(), date_time))
    
    f.write("\n")
    
    f.write("\n ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※\n")
    
    f.write("\n")
    
    f.write("Current temperature is       : {:.2f} deg C\n".format(txtlist[0]))
    f.write("{},{} \n".format("Current weather desc         :" ,txtlist[1]))
    
    f.write("\n")

    if (233> txtlist[7] >=200):
       f.write("⚠️⚡ Thunderstorm warning ⚡⚠️")
    elif (322> txtlist[7] >=300):
      f.write("Take an umbrella with you ")
    elif (532> txtlist[7] >=500):
      f.write("Dont foget your umbrella!!!")
    elif (623 > txtlist[7] >=600):
      f.write("Dont fogrt your winter kits its freezing!")
    elif (782> txtlist[7] >=701):
      f.write("Mind your step !!")
    elif (801> txtlist[7] >=800):
      f.write("Enjoy the clear sky")
    elif (805> txtlist[7] >=801):
      f.write("Its better not to plan watching stars in night :)\n")

    f.write("\n")
    
    f.write("{},{},{} \n".format("Current cloudiness           :",txtlist[2],'%' ))
    f.write("{},{},{} \n".format("Current Humidity             :",txtlist[3],"%"))

    f.write("\n")

    if (hmdt < 50 ):
      f.write("water vapour in the atmosphere is less than 50% use more water")
    else:
      f.write("water vapour in the atmosphere is good\n")

    f.write("\n")

    f.write("{},{},{} \n".format("Current wind speed           :",txtlist[4],"kmph"))
    f.write("{},{},{} \n".format("Current Atmospheric pressure :",txtlist[5],"hPa"))

    f.write("\n")

    f.write("※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※")