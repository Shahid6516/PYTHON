device_status = "active"
temprature = 38

if device_status == "active":
    if temprature > 35:
        print("High temprature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")


