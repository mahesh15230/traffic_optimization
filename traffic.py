import math
import copy as cp

class Road:

    road_count = 0

    def __init__(self, tosignalpop, awaysignalpop, signal1, signal2 = None):
        self.tosignalpop = tosignalpop
        self.awaysignalpop = awaysignalpop
        self.roadhead = signal1
        self.roadtail = signal2
        self.id = Road.road_count
        Road.road_count += 1

class Signal:

    signal_count = 0

    def __init__(self, mingreentime, maxgreentime, roadcount, nbhsignal = None): #nbhsignal has to be Signal object
        if nbhsignal == None:     
            self.id = Signal.signal_count
            Signal.signal_count += 1
            self.mingreentime = mingreentime
            self.maxgreentime = maxgreentime
            self.roads = [Road(0,0,self) for i  in range(roadcount)]
            self.roadLightConfig = dict(zip(self.roads,['orange' for i in range(roadcount)]))
        else:
            self.id = Signal.signal_count
            Signal.signal_count += 1
            self.mingreentime = mingreentime
            self.maxgreentime = maxgreentime
            self.roads = [Road(0,0,self) for i  in range(roadcount - 1)]
            self.roadLightConfig = dict(zip(['orange' for i in range(roadcount)],self.roads))
            for road in nbhsignal.roads:
                if road.roadtail == None:
                    road.roadtail = self
                    break

    def optimize(self):
        while True:    
            roadpopsdict = {}
            for road in self.roads:
                roadpopsdict[road] = road.tosignalpop
                
                








def greenlight(popsize):
    if 0 < popsize < 5:
        return 10
    elif 5 < popsize < 15:
        return 20
    elif 15 < popsize < 20:
        return 30
    elif 20 < popsize < 25:
        return 40 
    elif 25 < popsize < 30:
        return 50
    elif 30 < popsize < 40:
        return 70
    elif 40 < popsize :
        return 80