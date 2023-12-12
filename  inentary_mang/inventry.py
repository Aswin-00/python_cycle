'''

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

from product import Product as pd
  

class Inventory:
    def __init__(self):
        self.Inventory_list=[]
        
    def add_product(self, product):
        self.Inventory_list.append(product)

    def show_all(self):
        return self.Inventory_list

    def search(self,name):

        x=any(i.name==name for i in self.Inventory_list)
        if x==False:
            print('prodoct not in inventory soory')
            return
        print('product found ')
        
        for i in self.Inventory_list:
            if i.name==name:
                print('-'*45)
                print(i.get_description())
    def remove(self,name):
        for i in self.Inventory_list:
            if i.product_id==name:
                print(i.get_description())
                self.Inventory_list.remove(i)
                
        

                      
in01=Inventory()

def main():
    in01.add_product(pd('E01','baja',600))
    in01.add_product(pd('E02','scoter',60000))
    in01.add_product(pd('E03','fan',60000))
    in01.add_product(pd('E04','fan',60000))

    
    in01.search('df')
    in01.remove('E01')
    print(in01.show_all())
    

if __name__=='__main__':
    main()
