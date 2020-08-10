class Fees():
    def __init__(self, amount, weeklyinterest):
        self.amount=amount
        self.weeklyinterest=weeklyinterest
        self.locked=locked
        self.viewfines=viewfines

    def getAmount(self):
        return self.amount

    def getWeeklyinterest(self):
        return self.weeklyinterest

    def getLocked(self):
        return self.locked

    def getViewfines(self):
        return self.viewfines
    
    