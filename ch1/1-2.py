print(" *** Wind classification ***")
wind_speed = float(input("Enter wind speed (km/h) : "))
if wind_speed < 52:
    print("Wind classification is Breeze.")
elif wind_speed < 56:
    print("Wind classification is Depression.")
elif wind_speed < 102:
    print("Wind classification is Tropical Storm.")
elif wind_speed < 209:
    print("Wind classification is Typhoon.")
else:
    print("Wind classification is Super Typhoon.")
