from seed_object import Seed_Costs
from Climate_Check import Climate
from meteo import Weather
weather=Weather("4012 Carol Avenue Fremont California")
temperature=weather.temperature()
precepitation=weather.percipatation()
print(temperature)
print(precepitation)
climate_object=Climate()
amount_crops_eligble=climate_object.climate_returns(temperature,precepitation)
print(amount_crops_eligble)
seed_object=Seed_Costs()
z=seed_object.create_seed_object()
#print(z)
final_crops=list()
for x in amount_crops_eligble:
    for y in z:
        if x == y.seed_name:
            final_crops.append(y)

print(len(final_crops))
            



