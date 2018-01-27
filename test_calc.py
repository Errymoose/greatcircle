from greatcircle import *

data = [
    {'latitude': 53.339428, 'longitude': -6.257664, 'distance': 0.00 },
    {'latitude' : 53.3397964, 'longitude': -6.2576875, 'distance': 0.04099 },
    {'latitude' : 53.267505901, 'longitude': -6.4552688633, 'distance': 15.374125 },
    {'latitude': 45.8257438, 'longitude': -0.1206294, 'distance': 944.58169}
    ]

def test_answer():
    gc = GreatCircleCalculator(53.339428, -6.257664)
    for item in data:
        distance = gc.getDistanceFromOrigin(item['latitude'], item['longitude'])
        
        assert abs(item['distance'] - distance) <= 0.001
    
    