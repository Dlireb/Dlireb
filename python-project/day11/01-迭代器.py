class Iter_item:
    def __init__(self,end):
        self.end = end#设置结束值
        self.starte = 0#设置起始值为0

    def __iter__(self):
        return self

    def __next__(self):
        if self.starte < self.end:
            value = self.starte
            self.starte += 1
            return value
        else:
            raise StopIteration

for x in Iter_item(5):
    print(x)