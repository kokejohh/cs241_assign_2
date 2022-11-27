class Cat:
    def __init__(self, size, is_move=False):
        self.size = size
        self.is_move = is_move
    def setSize(self, size): self.size = size
    def setIsMove(self, is_move): self.is_move = is_move
    def getSize(self): return self.size
    def getIsMove(self): return self.is_move

class State:
    def __init__(self):
        self.cats = []
    def append(self, cat):
        self.cats.append(cat)
    def correct(self, cats):
        for i in range(0, len(cats), 2):
            if (cats[i].getSize() != cats[i + 1].getSize()): return False
        return True
    def findMinBox(self):
        ans = 0
        cats = self.cats
        setCat = set(cat.getSize() for cat in cats)
        for size in setCat:
            if (self.correct(cats)): return ans
            for cat in cats: if (cat.getSize() <= size): cat.setIsMove(True)
            cats = [Cat(cat.getSize()) for cat in cats if cat.getIsMove() == False]
            ans = size

n = int(input('input n : '))
state = State()
for i in range(n): state.append(Cat(int(input())))
print(state.findMinBox())

