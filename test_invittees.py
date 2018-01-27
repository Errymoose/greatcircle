from greatcircle import *


data = [
    {'latitude': 53.339428, 'longitude': -6.257664, 'distance': 0.00, "user_id": 4, "name": "John Doe" },
    {'latitude' : 53.3397964, 'longitude': -6.2576875, 'distance': 0.04099, "user_id": 2, "name": "Bob User" },
    {'latitude' : 53.267505901, 'longitude': -6.4552688633, 'distance': 15.374125, "user_id": 3, "name": "Jane Doe" },
    {'latitude': 45.8257438, 'longitude': -0.1206294, 'distance': 944.58169,"user_id": 1, "name": "Sarah"}
    ]
def test_answer():
    invitees = getInvitees(10, data)
    assert invitees == [ 
            {'latitude' : 53.3397964, 'longitude': -6.2576875, 'distance': 0.04099, "user_id": 2, "name": "Bob User" },
            {'latitude': 53.339428, 'longitude': -6.257664, 'distance': 0.00, "user_id": 4, "name": "John Doe" },
        ]
        
    invitees = getInvitees(100, data)
    assert invitees == [ 
            {'latitude' : 53.3397964, 'longitude': -6.2576875, 'distance': 0.04099, "user_id": 2, "name": "Bob User" },
            {'latitude' : 53.267505901, 'longitude': -6.4552688633, 'distance': 15.374125, "user_id": 3, "name": "Jane Doe" },
            {'latitude': 53.339428, 'longitude': -6.257664, 'distance': 0.00, "user_id": 4, "name": "John Doe" },
        ]
    