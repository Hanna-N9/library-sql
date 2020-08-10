class Librarian():
    def __init__(self, lastname, firstname, email, position):
        self.lastname=lastname
        self.firstname=firstname
        self.email=email
        self.position=position
        self.checkfine=checkfine
        self.verifymember=verifymember
        self.viewmemberrecord=viewmemberrecord
        self.updatebook=updatebook

    def getLastname(self):
        return self.lastname

    def getFirstname(self):
        return self.firstname

    def getEmail(self):
        return self.email

    def getPosition(self):
        return self.position
    
    def getCheckfine(self):
        return self.checkfine

    def getVerifymember(self):
        return self.verifymember

    def getUpdatebook(self):
        return self.updatebook

    
    
    