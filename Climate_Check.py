from meteo import Weather

weather=Weather("4012 Carol Avenue Fremont California")
temperature=weather.temperature()
precepitation=weather.percipatation()
print(temperature)
print(precepitation)
def climate_returns(temperature,rainfall):
    from Climate_Data import Climate_data_spring
    from Climate_Data import Climate_data_summer
    from Climate_Data import Climate_data_winter
    from Climate_Data import Climate_data_fall
    from Climate_Data import Crop_Climate_Data
    working = []
    flag = False
    cntr = 0
    fall_city_data = Climate_data_fall()
    summer_city_data = Climate_data_summer()
    winter_city_data = Climate_data_winter()
    spring_city_data = Climate_data_spring()
    crop_data = Crop_Climate_Data()

    fall_avg = fall_city_data.fall_data_dict
    spring_avg = spring_city_data.spring_data_dict
    summer_avg = summer_city_data.summer_data_dict
    winter_avg = winter_city_data.winter_data_dict
    crop_avg = crop_data.crop_data_dict


    
    #a = input("What is the upcoming season? Spring, Fall, Winter, or Summer?")
    #b = input("Which of the following cities are you closest to? Fremont, San Jose, Los Altos, Palo Alto, or Oakland")
    #print(a)

    #if a == "Fall":
        #rainfall = fall_avg[b]["Average Autumn Rainfall (inches)"]
        #temp = fall_avg[b]["Average Autumn Temperature (Fahrenheit)"]
    for i in crop_avg:
        flag = False
        #print(i)
        #crop_rain = [i]["Necessary Rainfall (inches)"]
        #print(i,"i")
        #print(len(crop_avg),"hahaahiahifehifheif",cntr)
        crop_rain = crop_avg[i]["Necessary Rainfall (inches)"]
        crop_temp = crop_avg[i]["Necessary Average Temperature (Fahrenheit)"]
        #print(crop_rain,crop_temp,temp,rainfall)
        if abs(crop_temp - temperature) < 15:
            flag = True
            print(flag)
        if flag == True:
            if abs(crop_rain - rainfall) < 8:
                working.append(i)
        cntr += 1
    return working
            
'''  
#if a == "Spring":
#rainfall = spring_avg[b]["Average Spring Rainfall (inches)"]
#temp = spring_avg[b]["Average Spring Temperature (Fahrenheit)"]
#for i in crop_avg:
#flag = False
#print(i)
#crop_rain = [i]["Necessary Rainfall (inches)"]
            #print(i,"i")
            #print(len(crop_avg),"hahaahiahifehifheif",cntr)
            #crop_rain = crop_avg[i]["Necessary Rainfall (inches)"]
            #crop_temp = crop_avg[i]["Necessary Average Temperature (Fahrenheit)"]
            #print(crop_rain,crop_temp,temp,rainfall)
           #if abs(crop_temp - temp) < 10:
               # flag = True
            #if flag == True:
                #if abs(crop_rain - rainfall) < 5:
                    #working.append(i)
            #cntr += 1

    #if a == "Summer":
        #rainfall = summer_avg[b]["Average Summer Rainfall (inches)"]
        #temp = summer_avg[b]["Average Summer Temperature (Fahrenheit)"]
        #for i in crop_avg:
            #flag = False
            #print(i)
            #crop_rain = [i]["Necessary Rainfall (inches)"]
            #print(i,"i")
            #print(len(crop_avg),"hahaahiahifehifheif",cntr)
            #crop_rain = crop_avg[i]["Necessary Rainfall (inches)"]
            #crop_temp = crop_avg[i]["Necessary Average Temperature (Fahrenheit)"]
            #print(crop_rain,crop_temp,temp,rainfall)
            #if abs(crop_temp - temp) < 10:
                #flag = True
            #if flag == True:
                #if abs(crop_rain - rainfall) < 5:
                    #working.append(i)
            #cntr += 1
   
    if a == "Winter":
        rainfall = winter_avg[b]["Average Winter Rainfall (inches)"]
        temp = winter_avg[b]["Average Winter Temperature (Fahrenheit)"]
        for i in crop_avg:
            flag = False
            #print(i)
            #crop_rain = [i]["Necessary Rainfall (inches)"]
            #print(i,"i")
            #print(len(crop_avg),"hahaahiahifehifheif",cntr)
            crop_rain = crop_avg[i]["Necessary Rainfall (inches)"]
            crop_temp = crop_avg[i]["Necessary Average Temperature (Fahrenheit)"]
            print(crop_rain,crop_temp,temp,rainfall)
            if abs(crop_temp - temp) < 10:
                flag = True
            if flag == True:
                if abs(crop_rain - rainfall) < 5:
                    working.append(i)
            cntr += 1
            
    return working
#python Climate_Check.py'''

availble=climate_returns(temperature,precepitation)
print(availble)