import sys
import math
import json
import os.path
from operator import itemgetter

class GreatCircleCalculator:
    def __init__(self, lat, long):
        self.origin = { "latitude": lat, "longitude": long }
    
    #using the Haversine formula
    def getDistanceFromOrigin(self, lat2, long2):
        lat1 = self.origin['latitude']
        long1 = self.origin['longitude']
    
        R = 6371;
        phi1 = math.radians(lat2);
        phi2 = math.radians(lat1);
        phi = math.radians(lat2-lat1);
        lmda = math.radians(long2-long1);

        a = math.sin(phi/2) * math.sin(phi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(lmda/2) * math.sin(lmda/2);
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
        return R * c;
        
# return only the customers within (limit)km, sorted by ascending user_id        
def getInvitees(limit, customers):
    invitees = []
    for customer in sorted(customers, key=itemgetter('user_id')):
        if customer['distance'] < limit:
            print str(customer['user_id']) + ' ' + customer['name']
            invitees.append(customer)
    return invitees
        
def main():
    gcCalc = GreatCircleCalculator(53.339428, -6.257664)
    customers = []
    with open('customers.json', 'r+') as f:
        print f
        for line in iter(f):
            customer = json.loads(line)
            lat = float(customer['latitude'])
            long = float(customer['longitude'])
            
            customer['distance'] = gcCalc.getDistanceFromOrigin(lat, long)
            customers.append(customer)
    
    invitees = getInvitees(100, customers)
            
if __name__ == '__main__':
    main()
    