from iteam import Iteam 
class Shoppingcart:
    def __init__(self):
        self.iteams=[]
        
    def add_item(self, item):
        self.iteams.append(item)
        
    def remove_item(seld,item):
        self.iteams.remove(item)

    def display_cart(self):
        print(f'''
Name\tQuantity\tPrice
''')
        for i in range(0,len(self.iteams)):
            print(self.iteams[i])

cart=cart()

def main():
        print('''
Shopping Cart Menu:
1. Add an item to the cart
2. Remove an item from the cart
3. Display the contents of the cart
4. Quit

''')
        choice =input('Enter your choice')
        if choice==1:
            pass
        else :
            pass
            
        


    
if __name__=='__main__':
    main()
