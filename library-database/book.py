class Book():
    def __init__(self, isbn, authorfirstname, authorlastname, pages):
        self.isbn=isbn
        self.authorfirstname=authorfirstname
        self.authorlastname=authorlastname
        self.pages=pages
        self.status='locked'
        self.available=available
        
    def Status(self, status):
        self.status=status

    def getStatus(self):
        return self.status
    
    def getAvailable(self):
        return self.available

    def getIsbn(self):
        return self.isben

    def getAuthorfirstname(self):
        return self.authorfirstname

    def getAuthorlastname(self):
        return self.authorlastname

    def getPages(self):
        return self.pages

    def getSecurityLevel(self):
        return self.securitylevel
