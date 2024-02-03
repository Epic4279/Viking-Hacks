from Climate_Data import Climate_data
from Climate_Data import Crop_Climate_Data

city_data = Climate_data()
crop_data = Crop_Climate_Data()

city_avg = city_data.city_data_dict
crop_avg = crop_data.crop_data_dict

print(city_avg,crop_avg)

#python Climate_Check.py