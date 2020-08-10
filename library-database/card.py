class Card():
    def __init__(self, cardnumber, title, dateissues, expiration):
        self.cardnumber=cardnumber
        self.title=title
        self.dateissues=datetime.datetime.now()
        self.expiration=datetime.datetime()
        
    def getCardnumber(self):
        return self.cardnumber

    def getTitle(self):
        return self.title

    def getDateissues(self):
        return self.dateissues

    def getExpiration(self):
        return self.expiration

    
    