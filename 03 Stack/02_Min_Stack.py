class MinStack:

    def __init__(self):
        self.l = []
        self.mins = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.mins == [] or val <= self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        if self.l[-1] == self.mins[-1]:
            self.mins = self.mins[0:-1]
        self.l = self.l[0:-1]
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        if self.mins == []:
            return None
        else:
            return self.mins[-1]

        
