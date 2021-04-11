import pyowm

owm = pyowm.OWM('344de8c4672c7f8cd7e99ba15e327956', language="ita")

name = input("Select your country: ")

observation = owm.weather_at_place(name)
w = observation.get_weather()
print(w)