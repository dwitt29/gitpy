class StatsList(list):
    @property
    def mean(self):
        return sum(self)/len(self)
        
    @property
    def stdev(self):
        n=len(self)
        return math.sqrt( n*sum(x**2 for x in self)-sum(self)**2)/n
        