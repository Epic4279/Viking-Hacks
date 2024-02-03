from data import Data
data=Data()
seed_data=data.grape_seeds_data
working = []
amount_per_acre = 0
x = False
cost = int(input("What is the maximum you are willing to pay per acre per crop?"))
seed_rep = input("Should the crops be able to produce seeds, reply with yes or no")
if seed_rep.lower() == "yes":
    seed_rep = True
elif seed_rep.lower() == "no":
    seed_rep = False
#print(seed_rep, cost,"XXGEIUGWEF")
for i in seed_data:
    x = False
    print(seed_data[i])
    #print(seed_data[i][0])
    if cost < seed_data[i][0]:
        x = True
        #print(cost,seed_data[i][0])
        continue
    if seed_data[i][1] != seed_rep:
        x = True
        #print(seed_rep,seed_data[i][1])
        continue
    if x == False:
        print("hello")
        working.append(i)
print(working)