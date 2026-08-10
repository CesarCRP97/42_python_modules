def ft_water_reminder():
    days_since_last_watering = input("Days since last watering: ")
    if int(days_since_last_watering) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_reminder()
