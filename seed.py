class Seed():
    # Weight is per 100 grains measured in grams
    # All others measured in meters
    # Cost per acre to plant
    # Sale value is $ per bushel
    def __init__(self, seed_name, amount_of_seeds_produced, pods_per_square, grains_per_pod, weight, cost, sale_value,bushel_produced): 
        self.seed_name = seed_name
        self.pods_per_square = pods_per_square
        self.grains_per_pod = grains_per_pod
        self.weight = weight
        self.cost = cost
        self.sale_value = sale_value
        self.amount_of_seeds_produced=amount_of_seeds_produced
        #self.bushels_produced_per_acre=((float(self.pods_per_square) * float(self.grains_per_pod) * float(self.weight)) / float(10000)) * 36.7437
        self.bushels_produced_per_acre=bushel_produced
        self.profit=(self.bushels_produced_per_acre*self.sale_value)
    
   
