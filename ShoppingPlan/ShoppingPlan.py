class Location(object):

    def __init__(self,x,y,name):
        self.x=x
        self.y=y
        self.name=name

    def GetLoc(self):
        return self.name, (self.x, self.y)

class Store(Location):

    def __init__(self,x,y,name,stock):
        super(Store, self).__init__(x,y,name)
        self.stock=stock

class Map(object):

    def __init__(self):
        self.locations={}
        self.roads={}

    def addLocation(self,loc):
        if loc.name not in [ l for l in self.locations.keys() ]:
            self.locations.update({loc.name:loc})

    def addRoad(self,road):
        if road.label not in [ r for r in self.roads.keys() ]:
            self.roads.update({road.label:road})

    def Display(self):
        print "Map.Display()"
        for roadkey,road in self.roads.items():
            print road.GetRoad()

    def BuildAllRoads(self):
        for i in self.locations.values():
            for j in self.locations.values():
                if i.name != j.name:
                    self.addRoad(Road(i,j,'{} to {}'.format(i.name,j.name)))

    def BuildTwoWayRoad(self, locFrom, locTo):
        for i in locFrom:
            for j in locTo:
                if i.name != j.name:
                    self.addRoad(i,j,'{} to {}'.format(i.name,j.name))
                    self.addRoad(j,i,'{} to {}'.format(i.name,j.name))

    def BuildOneWayRoad(self, locFrom, locTo):
        for i in locFrom:
            for j in locTo:
                if i.name != j.name:
                    self.addRoad(i,j,'{} to {}'.format(i.name,j.name))

class Road(object):
    def __init__(self,loc1,loc2,label):
        self.loc1=loc1  # class Location() or Store()
        self.loc2=loc2  # class Location() or Store()
        self.distance=calcDist(self.loc1, self.loc2)
        self.label=label
    def GetRoad(self):
            return self.label, self.loc1.GetLoc(), self.loc2.GetLoc(), '{0:.2f}'.format(self.distance)

def Shopping(gas, foodlist, stores, home, town):
    import itertools, re

    expt=re.compile('!')

    StoreCombos = itertools.permutations(stores,len(stores)) 
    for StoreCombo in StoreCombos:
        TotalCost=0.0
        WhereAmI=home.get('home').name
        TripStops=[]
        TripStops.append(WhereAmI)
        Perishable=False
        ReturnHome=False
        templist=list(foodlist)
        for i in StoreCombo:
            store=stores[i]
            Cart=[]
            FoundFood=False
            for food in templist:
                Perishable=False
                if expt.search(food):
                    ReturnHome=True
                    food=food.rstrip('!')
                    Perishable=True
                if store.stock.has_key(food):
                   FoundFood=True
                   TotalCost+=float(store.stock[food])
                   print '${0:.2f}'.format(TotalCost), food, store.name
                   Cart.append(food) if not Perishable else Cart.append(food+'!')
            if FoundFood:
               TripStops.append(store.name)
               TotalCost+=gas*town.roads.get('{} to {}'.format(WhereAmI,store.name)).distance
               print '${0:.2f}'.format(TotalCost), '{} to {}'.format(WhereAmI,store.name),town.roads.get('{} to {}'.format(WhereAmI,store.name)).distance
               WhereAmI=store.name
               for food in Cart:
                   templist.pop(templist.index(food))
            if ReturnHome:
               TripStops.append(home.get('home').name)
               TotalCost+=gas*town.roads.get('{} to {}'.format(WhereAmI,home.get('home').name)).distance
               print '${0:.2f}'.format(TotalCost), '{} to {}'.format(WhereAmI,home.get('home').name),town.roads.get('{} to {}'.format(WhereAmI,home.get('home').name)).distance
               WhereAmI=home.get('home').name
               ReturnHome=False
               Perishable=False

        if WhereAmI != home.get('home').name:
            TotalCost+=gas*town.roads.get('{} to {}'.format(WhereAmI,home.get('home').name)).distance
            print '${0:.2f}'.format(TotalCost), '{} to {}'.format(WhereAmI,home.get('home').name),town.roads.get('{} to {}'.format(WhereAmI,home.get('home').name)).distance
            TripStops.append(home.get('home').name)
            WhereAmI=home.get('home').name

        print foodlist,StoreCombo, TripStops, '${0:.2f}'.format(TotalCost)

def calcDist( source, dest ):
    import math
    return math.sqrt((dest.x - source.x)**2 + (dest.y - source.y)**2)
 
def ReadData():
    fh=open('store2.txt', 'r')
    cases=int(fh.readline().rstrip().split(None)[0])

    for case in range(cases):
        num_items,num_stores,gas_price=map(int,fh.readline().rstrip().split(None))

        foodlist=fh.readline().rstrip().split(None)

        stores=dict()
        for store in range(num_stores):
            tmp=fh.readline().rstrip().split(None)
            x,y,store_stock=int(tmp[0]),int(tmp[1]),{ k:v for k,v in (x.split(':') for x in tmp[2:]) }
            stores.update({'store{}'.format(store):Store(x,y,'store{}'.format(store),store_stock)})

    return gas_price,foodlist,stores

def main():
    home=dict(); home.update({'home':Location(0,0,'home')})
    gas,foodlist,stores=ReadData()
    Town=Map()
    locations=dict(home.items()+stores.items())
    for location in locations:
        Town.addLocation(locations[location])
    Town.BuildAllRoads()
    Town.Display()
    Shopping(gas, foodlist, stores, home, Town)

if __name__ == '__main__':
    main()
