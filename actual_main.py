class run_program:
    def __init__(self):
        pass
    def start_game(self, address):
        from seed_object import Seed_Costs
        from Climate_Check import Climate
        from meteo import Weather
        weather=Weather(address)
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
        sorted_objects = sorted(final_crops, key=lambda x: x.profit, reverse=True)
        return sorted_objects
        for x in sorted_objects:
            print(str(x.seed_name)+": $"+str(round(x.profit,3)))
            



