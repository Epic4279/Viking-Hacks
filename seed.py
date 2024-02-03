class Seed():
    # Weight is per 100 grains measured in grams
    # All others measured in meters
    # Cost per acre to plant
    # Sale value is $ per bushel
    def __init__(self, seed_name, amount_of_seeds_produced, pods_per_square, grains_per_pod, weight, cost, sale_value): 
        self.seed_name = seed_name
        self.pods_per_square = pods_per_square
        self.grains_per_pod = grains_per_pod
        self.weight = weight
        self.cost = cost
        self.sale_value = sale_value
        self.amount_of_seeds_produced=amount_of_seeds_produced
    
    def max_yeild(self):
        # returns bushels per 100 acres
        return ((self.pods_per_square * self.grains_per_pod * self.weight) / 10,000) * 36.7437
    
    #def net_max_profit(self, bushels_yeilded):
        #profit = bushels_yeilded * self.sale_value
        #loss = self.max_yeild() * 
