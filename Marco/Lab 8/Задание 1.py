class alla:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vivodka(self):
        print(self.x)
        print(self.y)

    def izmena(self):
        self.x *= 8
        self.y *= 8
        print(self.x)
        print(self.y)

    def summ(self):
        print(self.x + self.y)

    def maxim(self):
        if self.x > self.y:
            print(self.x)
        else:
            print(self.y)


kuraj = alla(22, 30)
kuraj.vivodka()
kuraj.izmena()
kuraj.summ()
kuraj.maxim()
