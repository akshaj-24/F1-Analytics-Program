
#Importing the necessary libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot
import fastf1
import fastf1.plotting

#Setting cache folder
fastf1.Cache.enable_cache(r"C:\Users\aksha\Desktop\Grade 12 Python Practical\Project\Cache")

#Asking for year: parameter1
sessionyear= int(input("Enter the year:  "))

#Displaying event calendar so that user can choose race: parameter 2
schedule = fastf1.get_event_schedule(sessionyear)
print(schedule)

#Asking for race and session info: paramter 3 and 4, loading session
sessionchoice = input("Enter the race location you wish to choose:  ")
sessiontype = input("Enter the session type R for race Q for qualifying:  ")
session = fastf1.get_session(sessionyear,sessionchoice,sessiontype)
session.load()

#Printing menu so user can choose data and graph types
print("Menu:\n1. Comparison between two drivers on their fastest laps\n2. Speed vs Distance between drivers on"
      "fastest lap\n3. Lap Times over the race for a driver (Only R)\n4. Lap Times comparison between "
      "two drivers for a race (Only R)\n5. Session results\n6. Show the weather data for the session"
      "\n7. DataFrame operations and attributes")

#Asking for numeric choice
choice = int(input("Choice: "))

#Creating elif statement for each menu option

# Choice 1: Comparison between two drivers on their fastest laps
if choice==1:
      driver1 = input("Enter the abbreviation of first driver: ")
      color1 = fastf1.plotting.driver_color(driver1)
      fast_driver1 = session.laps.pick_driver(driver1).pick_fastest()
      driver1cardata= fast_driver1.get_car_data()
      driver2 = input("Enter the abbreviation of second driver: ")
      color2 = fastf1.plotting.driver_color(driver2)
      fast_driver2 = session.laps.pick_driver(driver2).pick_fastest()
      driver2cardata = fast_driver2.get_car_data()
      print(driver1cardata.columns)
      x = input("What do you want on the X axis: ")
      y = input("What do you want on the Y axis: ")
      d1x = driver1cardata[x]
      d1y = driver1cardata[y]
      d2x = driver2cardata[x]
      d2y = driver2cardata[y]
      pyplot.plot(d1x,d1y,color=color1,label=driver1)
      pyplot.plot(d2x,d2y,color=color2,label=driver2)
      pyplot.xlabel(x)
      pyplot.ylabel(y)
      pyplot.title([driver1,"and",driver2,' ',y,"v/s",x])
      pyplot.legend()
      pyplot.show()

#Choice 2: Speed vs Distance between drivers on fastest lap
elif choice==2:
      driver1=input("Enter abbreviation for Driver 1: ")
      driver2=input("Enter abbreviation for Driver 2: ")
      color1 = fastf1.plotting.driver_color(driver1)
      color2 = fastf1.plotting.driver_color(driver2)
      d1lap = session.laps.pick_driver(driver1).pick_fastest()
      d2lap = session.laps.pick_driver(driver2).pick_fastest()
      d1tel = d1lap.get_car_data().add_distance()
      d2tel = d2lap.get_car_data().add_distance()
      pyplot.plot(d1tel['Distance'],d1tel['Speed'],color=color1,label=driver1)
      pyplot.plot(d2tel['Distance'], d2tel['Speed'], color=color2, label=driver2)
      pyplot.xlabel("Distance in m")
      pyplot.ylabel("Speed in km/h")
      pyplot.legend()
      pyplot.show()

#Choice 3: Lap Times over the race for a driver (Only R)
elif choice==3:
      driver1 = input("Enter driver 1 abbreviation: ")
      color1 = fastf1.plotting.driver_color(driver1)
      laps = session.load_laps()
      laps['Time_seconds'] = laps['LapTime'].dt.total_seconds()
      driverlaps = laps.pick_driver(driver1)
      pyplot.plot(driverlaps['LapNumber'], driverlaps['Time_seconds'], color=color1, label=[driver1, " Race pace"])
      pyplot.legend()
      pyplot.xlabel("Lap Number")
      pyplot.ylabel("Lap Time in seconds")
      pyplot.show()

#Choice 4:
elif choice==4:
      driver1 = input("Enter driver 1 abbreviation: ")
      driver2= input("Enter driver 2 abbreviation: ")
      color1 = fastf1.plotting.driver_color(driver1)
      color2 = fastf1.plotting.driver_color(driver2)
      laps = session.load_laps()
      laps['Time_seconds'] = laps['LapTime'].dt.total_seconds()
      driver1laps = laps.pick_driver(driver1)
      driver2laps = laps.pick_driver(driver2)
      pyplot.plot(driver1laps['LapNumber'], driver1laps['Time_seconds'], color=color1, label=[driver1, " Race pace"])
      pyplot.plot(driver2laps['LapNumber'], driver2laps['Time_seconds'], color=color2, label=[driver2," Race pace"])
      pyplot.legend()
      pyplot.xlabel("Lap Number")
      pyplot.ylabel("Lap Time in seconds")
      pyplot.show()

elif choice==5:
     if sessiontype=="R":
           print(session.results.iloc[0:20].loc[:, ['FullName', 'Position', 'Points','Status']])
     elif sessiontype=="Q":
           print("What session Q1/Q2/Q3?")
           choice = int(input("Enter choice: "))
           if choice == 1:
                 print(session.results.iloc[0:20].loc[:, ['FullName', 'Position', 'Q1']])
           elif choice == 2:
                 print(session.results.iloc[0:15].loc[:, ['FullName', 'Position', 'Q2']])
           elif choice == 3:
                 print(session.results.iloc[0:10].loc[:, ['FullName', 'Position', 'Q3']])

# Wind data
elif choice==6:
      weather_data = session.laps.get_weather_data()
      print(weather_data.columns)
      print(weather_data.loc[:, ['Time', 'WindSpeed']])
      x = input("What do you want on x axis: ")
      y = input("What do you want on y axis: ")
      pyplot.plot(weather_data.iloc[0:20].loc[:, [x]], weather_data.iloc[0:20].loc[:,[y]],color="Blue")
      pyplot.xlabel(x)
      pyplot.ylabel(y)
      pyplot.show()

# Data Frame attributes and properties
elif choice==7:
      laps = session.load_laps()
      print(laps.index)
      print(laps.columns)
      print(laps.dtypes)
      print(laps.values)
      print(laps.shape)
      print(laps.size)
      print(laps.T)
      laps.to_csv(r'C:\Users\aksha\Desktop\Grade 12 Python Practical\Project\To CSV\sessioncsv.csv',
                  sep='@', header=False, index=False)
