# Program E10x8.py
# isinstance method 

class Sup:
      
    def subt(self, a, b):
        print('The difference of Two numbers = ', a - b)
  
class Der(Sup):
  
    def subt(self, a, b):
        print('The difference now = ', a - 2*b )
         
     
def main():
    obj1 = Sup()
    obj2 = Der()
    if isinstance(obj1, Sup):
        obj1.subt(300, 100)
    elif isinstance(obj2, Der):
        obj2.subt(300, 100)
      
main()
