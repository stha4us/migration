

class Node(object):
    "Generic tree node."
    def __init__(self, name):
        self.name = name
        self.child = {}

        
        
        
class HomeAddressTree(object):
    '''
    This class creates a address tree form
    the provided address dictionary
    A random walk on tree provides => country.province.district.VRD.ward
    '''
    def __init__(self,country,ID):
        self.root = Node(country,ID)
        
    def set_province(self,province,PID):
        self.root.child.update({province:Node(province,PID)})
            
    def set_district(self,province,district,DID):
        self.root.child[province].child.update({district:Node(district,DID)})
        
    def set_VRD(self,province,district,VRD,VID):
        self.root.child[province].child[district].child.update({VRD:Node(VRD,VID)})
        
    def set_ward(self,province,district,VRD,ward,WID):
         self.root.child[province].child[district].child[VRD].child.update({ward:Node(ward,WID)})
            
    


class Person(object):
    
    '''
    This class creates a Person object having incapsulated data
    structure( ID,age,country,home address etc.)
    '''
    
    def __init__(self):
        
        self.ID = str()
        self.age = int()
        self.foreign_address = dict()
        self.home_address = dict()
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
        
    
        
    