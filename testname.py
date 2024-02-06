from data2 import Data_v2

data2=Data_v2()
x=data2.seed_grains_database
for i in x:
    list = [data2.seed_grains_database[i][0], data2.seed_grains_database[i][1], data2.seed_grains_database[i][2]]
    print(list)
#python testname.py