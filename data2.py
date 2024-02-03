class Data_v2:
    def __init__ (self):
        self.seed_grains_database = {
            'Wheat': [600, 1000, 150, 30, 3],
            'Barley': [550, 800, 120, 20, 2.5],
            'Oats': [500, 700, 100, 15, 2],
            'Rye': [650, 900, 130, 25, 2.7],
            'Maize': [700, 1200, 180, 16, 3.5],
            'Rice': [900, 1500, 200, 30, 1.8],
            'Sorghum': [700, 1000, 160, 18, 3],
            'Millet': [750, 1100, 170, 22, 2.2],
            'Quinoa': [850, 1300, 190, 25, 2.8],
            'Amaranth': [600, 1000, 150, 20, 2.5],
            'Teff': [650, 900, 140, 18, 2.3],
            'Spelt': [800, 1200, 180, 25, 2.5],
            'Einkorn': [850, 1300, 200, 30, 2.7],
            'Emmer': [750, 1100, 160, 22, 2],
            'Khorasan': [900, 1500, 220, 28, 3.2],
            'Buckwheat': [800, 1200, 180, 20, 2.5],
            'Millet': [750, 1100, 170, 22, 2.2],
            'Soybeans': [700, 1000, 150, 15, 4],
            'Lentils': [650, 900, 130, 18, 1.8],
            'Chickpeas': [850, 1300, 190, 25, 2.2],
            'Black-eyed Peas': [750, 1100, 160, 20, 2],
            'Kidney Beans': [900, 1500, 200, 30, 2.5],
            'Pinto Beans': [700, 1000, 150, 15, 3],
            'Adzuki Beans': [650, 900, 140, 18, 2.8],
            'Lima Beans': [800, 1200, 180, 25, 3],
            'Garbanzo Beans': [850, 1300, 220, 28, 2.5],
            'Fava Beans': [750, 1100, 160, 22, 2],
            'Sunflower Seeds': [700, 1000, 150, 15, 1],
            'Pumpkin Seeds': [650, 900, 130, 18, 0.8],
            'Flaxseeds': [850, 1300, 190, 25, 0.5],
            'Chia Seeds': [750, 1100, 170, 22, 1],
            'Hemp Seeds': [900, 1500, 200, 30, 0.2],
            'Poppy Seeds': [700, 1000, 150, 15, 0.1],
            'Sesame Seeds': [650, 900, 140, 18, 0.2],
            'Mustard Seeds': [800, 1200, 180, 25, 0.5],
            'Cumin Seeds': [850, 1300, 220, 28, 0.3],
            'Coriander Seeds': [750, 1100, 160, 22, 0.4],
            'Fennel Seeds': [900, 1500, 200, 30, 0.3],
            'Caraway Seeds': [700, 1000, 150, 15, 0.2],
            'Anise Seeds': [650, 900, 130, 18, 0.3],
            'Safflower Seeds': [800, 1200, 180, 25, 0.4],
            'Agricultural Hemp': [850, 1300, 190, 25, 0.2],
            'Canola': [750, 1100, 160, 22, 0.4],
            'Cotton Seeds': [900, 1500, 200, 30, 0.5],
            'Peanuts': [700, 1000, 150, 15, 1.5],
            'Walnuts': [650, 900, 130, 18, 2],
            'Almonds': [800, 1200, 180, 25, 1.5],
            'Cashews': [850, 1300, 220, 28, 2],
            'Pistachios': [750, 1100, 160, 22, 1.7],
            'Hazelnuts': [900, 1500, 200, 30, 1.8],
            'Pecans': [700, 1000, 150, 15, 1.8],
            'Brazil Nuts': [650, 900, 140, 18, 2.5],
            'Macadamia Nuts': [800, 1200, 180, 25, 1.2],
            'Chestnuts': [850, 1300, 190, 25, 3],
            'Cocoa Beans': [750, 1100, 160, 22, 0.6],
            'Coffee Beans': [900, 1500, 200, 30, 0.2],
            'Flax': [700, 1000, 150, 15, 0.5],
            'Hemp': [650, 900, 130, 18, 0.2],
            'Chia': [800, 1200, 180, 25, 0.3]
            }
        self.cost_per_bushel = {
            'Wheat': 4.5,
            'Barley': 3.8,
            'Oats': 2.7,
            'Rye': 4.2,
            'Maize': 3.9,
            'Rice': 5.6,
            'Sorghum': 4.1,
            'Millet': 4.3,
            'Quinoa': 6.2,
            'Amaranth': 4.8,
            'Teff': 5.1,
            'Spelt': 5.3,
            'Einkorn': 6.5,
            'Emmer': 5.8,
            'Khorasan': 7.2,
            'Buckwheat': 5.4,
            'Soybeans': 9.8,
            'Lentils': 3.6,
            'Chickpeas': 7.4,
            'Black-eyed Peas': 6.1,
            'Kidney Beans': 8.2,
            'Pinto Beans': 7.0,
            'Adzuki Beans': 6.5,
            'Lima Beans': 7.6,
            'Garbanzo Beans': 7.8,
            'Fava Beans': 6.9,
            'Sunflower Seeds': 2.5,
            'Pumpkin Seeds': 1.8,
            'Flaxseeds': 2.1,
            'Chia Seeds': 3.2,
            'Hemp Seeds': 0.9,
            'Poppy Seeds': 0.6,
            'Sesame Seeds': 1.2,
            'Mustard Seeds': 1.8,
            'Cumin Seeds': 2.2,
            'Coriander Seeds': 2.0,
            'Fennel Seeds': 2.4,
            'Caraway Seeds': 1.7,
            'Anise Seeds': 1.9,
            'Safflower Seeds': 2.3,
            'Agricultural Hemp': 0.8,
            'Canola': 3.0,
            'Cotton Seeds': 1.5,
            'Peanuts': 4.5,
            'Walnuts': 6.2,
            'Almonds': 5.8,
            'Cashews': 7.0,
            'Pistachios': 6.5,
            'Hazelnuts': 5.4,
            'Pecans': 6.1,
            'Brazil Nuts': 7.5,
            'Macadamia Nuts': 8.2,
            'Chestnuts': 9.0,
            'Cocoa Beans': 2.3,
            'Coffee Beans': 1.8,
            'Flax': 1.9,
            'Hemp': 0.7,
            'Chia': 1.0,
            }
        self.bushels_produced_per_acre = {
            'Wheat': 40,
            'Barley': 35,
            'Oats': 30,
            'Rye': 38,
            'Maize': 45,
            'Rice': 28,
            'Sorghum': 40,
            'Millet': 37,
            'Quinoa': 50,
            'Amaranth': 42,
            'Teff': 43,
            'Spelt': 48,
            'Einkorn': 52,
            'Emmer': 45,
            'Khorasan': 55,
            'Buckwheat': 50,
            'Soybeans': 20,
            'Lentils': 32,
            'Chickpeas': 38,
            'Black-eyed Peas': 35,
            'Kidney Beans': 40,
            'Pinto Beans': 36,
            'Adzuki Beans': 33,
            'Lima Beans': 42,
            'Garbanzo Beans': 45,
            'Fava Beans': 40,
            'Sunflower Seeds': 10,
            'Pumpkin Seeds': 8,
            'Flaxseeds': 12,
            'Chia Seeds': 18,
            'Hemp Seeds': 5,
            'Poppy Seeds': 3,
            'Sesame Seeds': 7,
            'Mustard Seeds': 10,
            'Cumin Seeds': 15,
            'Coriander Seeds': 11,
            'Fennel Seeds': 14,
            'Caraway Seeds': 9,
            'Anise Seeds': 11,
            'Safflower Seeds': 13,
            'Agricultural Hemp': 4,
            'Canola': 16,
            'Cotton Seeds': 8,
            'Peanuts': 22,
            'Walnuts': 28,
            'Almonds': 25,
            'Cashews': 26,
            'Pistachios': 23,
            'Hazelnuts': 24,
            'Pecans': 26,
            'Brazil Nuts': 30,
            'Macadamia Nuts': 32,
            'Chestnuts': 35,
            'Cocoa Beans': 11,
            'Coffee Beans': 9,
            'Flax': 10,
            'Hemp': 4,
            'Chia': 6,
        }