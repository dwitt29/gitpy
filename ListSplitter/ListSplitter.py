class ListSplitter():
    '''
    split a list of numbers and determine if they can be split where the sublist sums equal
    Eg.    11222 -> True
           12112224 -> False
    '''
    def __init__(self,listitems):
        if len(listitems) < 2: 
            raise Exception('List too short')
        self.listitems=listitems
        self.left=0
        self.right=len(self.listitems)-1
        self.ltot=int(self.listitems[self.left])
        self.rtot=int(self.listitems[self.right])
  
    def doSplit(self):
        while True:
            print '{}:{}  {}:{}'.format(self.left,self.right,self.ltot,self.rtot)
            if (self.right - self.left) <= 1:
                if self.ltot == self.rtot:
                    return True
                else:
                    return False
            else:
                if self.rtot < self.ltot:
                    self.right-=1
                    self.rtot+=int(self.listitems[self.right])
                elif self.ltot < self.rtot: 
                    self.left+=1
                    self.ltot+=int(self.listitems[self.left])
                else:
                    self.left+=1
                    self.ltot+=int(self.listitems[self.left])
