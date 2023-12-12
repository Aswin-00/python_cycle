'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
27) You are tasked with implementing an Inventory Management System for a store that sells different types of products, including electronics and clothing. The system should allow adding, updating, and displaying product information, and it should utilize polymorphism to handle different types of products.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Create a base class called `Product` with the following attributes and methods:

Attributes:
1. `product_id` (a unique identifier for the product)
2. `name` (the name of the product)
3. `price` (the price of the product)

Methods:
1. `__init__(self, product_id, name, price)` - a constructor to initialize the attributes.
2. `get_description(self)` - returns a string describing the product.

Create two subclasses: `` and `Clothing`, each representing a specific type of product. Both subclasses should inherit from the `Product` base class and override the `get_description()` method to provide a description specific to their type.

`Electronics` should have an additional attribute called `manufacturer`.

`Clothing` should have an additional attribute called `size`.

Next, create a class called `Inventory` that maintains a list of products. It should have the following methods:

1. `add_product(self, product)` - adds a product to the inventory.
2. `update_product(self, product_id, new_price)` - updates the price of a product with the given product ID.
3. `display_inventory(self)` - displays information for all products in the inventory.

Now, implement a function called `main()` that demonstrates the Inventory Management System:

1. Create instances of different products (both electronics and clothing).
2. Add these products to the inventory.
3. Update the price of some products.
4. Display the inventory, including the description of each product.

Your program should utilize polymorphism to handle different types of products in the inventory.
 

'''
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price

    def update_price(self,value):
        if value >=0:
            self.price=price
        else:
            print('not a valid amount')
            
                
    def get_description(self):
        return(f'product desription\nproduct_id = {self.product_id }\nproduct name = {self.name}\nprice = {self.price}')
    
    def __str__(self):
         return(f'{self.name}')    

class Electronics(Product):
    def __init__(self,product_id,name,price,manfct):
        super().__init__(product_id,name,price)
        self.manufacturer=manfct
           
class Clothing(Product):
    def __init__(self,product_id,name,price,size):
        super().__init__(product_id,name,price)
        self.size=size
