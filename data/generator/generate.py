class Person(object):
    
    '''
    This class creates a Person object having incapsulated data
    structure( ID,age,country,home address etc.)
    '''
    
    def __init__(self):
        
        self.ID = str()
        self.age = int()
        self.current_country = dict()
        self.nepal_address = dict()
        self.profession = dict()
        
    '''
    This function generates a random ID of 10 letters.
    '''   
    def set_ID():
        letters = ["A", "B", "C", "D","E",\
               "F", "G", "H", "I", "J",\
               "K", "L", "M", "N", "O",\
               "P", "Q", "R", "S", "T",\
               "U", "V", "W", "X", "Y", "Z"]
        numbers = [str(i) for i in range(9)]
        
        for k in range(N):
            t = random.choice([0,1])
        if t == 0: self.ID = self.ID + random.choice(letters)
        else: self.ID = self.ID + random.choice(numbers)
    
        
    '''
    This function generates a random age uniformly distributed
    '''
    def set_age():
        self.age = random.randint(25,50)
        
    '''
    This function selected current country data dictionary from the provided list
    '''
    def set_current_country(self,Countries):
        self.current_country = random.choice(Countries)
        
        
    def set_home_address(self, Nepal):
        
    
        
        
        
    