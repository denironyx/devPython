## Restuarant class
class Restuarant:
    """Restuarant class that stores cuisine type and name"""
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def describe(self):
        """Describing the restuarant"""
        print(f"{self.type} is a type cuisine serve at {self.name} restuarant.")
        
    def open(self):
        """A message that indicate that the restuarant is open"""
        print(f"Welcome! {self.name} restuarant is open for services.")
        
my_res =  Restuarant('Only Grill', 'Picanha')
print(f"I have been to {my_res.name}.")
print(f"I do like {my_res.type} cuisine")

## 

my_res.describe()
my_res.open()