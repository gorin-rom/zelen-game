class Price:
    def __init__(self, Т=0, М=0, К=0, Б=0, З=0):
        if all(0 <= vegs <= 5 for vegs in [Т, М, К, Б, З]):
            
            self.Т = Т
            self.М = М
            self.К = К
            self.Б = Б
            self.З = З
        else:
            raise ValueError

    def __repr__(self):
        return f'{self.Т}{self.М}{self.К}{self.Б}{self.З}'

    def save(self):
        return repr(self)



