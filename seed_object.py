from seed import Seed
from data2 import Data_v2
data=Data_v2()
new_data=data.seed_grains_database
seed_object_list=[]
for x in new_data:
    seed=Seed(x,new_data[x][1],new_data[x][2],new_data[x][3],new_data[x][4],new_data[x][0],0)
    seed_object_list.append(seed)
    print("Seed name : ",seed.seed_name)
    print("pod_per_square : ",seed.pods_per_square)
    print("grains_per_pod :",seed.grains_per_pod)
    print("weight :",seed.weight)
    print("cost",seed.cost)
    print("sale_value",seed.sale_value)
    print("amout_of_seeds_produced",seed.amount_of_seeds_produced)
#print(seed_object_list)
   


