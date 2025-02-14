global_data = []

class badclass:
    def __init__(self,x,y):
        self.data=x
        self._y=y

    def process(self):global_data.append(self.data)

    def get_data(self): return self._y  
