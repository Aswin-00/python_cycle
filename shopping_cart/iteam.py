'''
1. Create an `Item` class with  attributes and methods:
   - Attributes: `name`, `price`, `quantity`, `description`, and `manufacturer`.
   - Methods:
     - `__init__(self, name, price, description, manufacturer)` - Initialize the item with a name, 
         price, description, and manufacturer. Quantity should be set to 1 by default.
     - `increase_quantity(self)` - Increase the quantity of the item by 1.
     - `decrease_quantity(self)` - Decrease the quantity of the item by 1.
     - `get_item_details(self)` - Return a string with details of the item.

2. Create a `ShoppingCart` class with the following methods:
   - `__init__(self)` - Initialize an empty list of items.
   - `add_item(self, item)` - Accept an Item object and add it to the cart.
   - `remove_item(self, item)` - Accept an Item object and remove it from the cart.
   - `display_cart(self)` - Display the items in the cart with their details.




Create a menu-driven program for the user to perform the following actions:

- Add an item to the shopping cart.
- Remove an item from the shopping cart.
- Display the contents of the shopping cart.
- Quit the program.


'''

class Iteam:
    def __init__(self,name,price,description,manu):
        self.name=name
        self.price=price
        self.quantity=1
        self.description=description
        self.manaufacturer=manu
        

    def increase_quantity(self):
        self.qunatity+=1
            
    def decrease_quantity(self):
        if self.quantity>0:
               self.quantity-=1
    
    def get_iteam_details(self):
        print(f'''
Name         {self.name}
Price        {self.price}
Quantity     {self.quantity}
Description  {self.description}
Manufactuter {self.manaufacturer}
              ''')
    def __str__(self):
        return(f'''
{self.name}\t{self.quantity}\t{self.price}
''')
        
Laptop=Iteam('Laptop',1200,'High-performance laptop','hp')
phone=Iteam('phone',800,'Latest smartphone model','Apple')




