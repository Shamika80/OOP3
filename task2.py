class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):        
        print("-" * 20)
        print("Product Information:")
        print(f"  ID: {self.product_id}")
        print(f"  Name: {self.name}")
        print(f"  Price: ${self.price:.2f}")

class Clothing(Product):
    
    def __init__(self, product_id: str, name: str, price: float, size: str):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
    
        super().display_info() 
        print(f"  Size: {self.size}")

class Book(Product):    
    def __init__(self, product_id: str, name: str, price: float, author: str):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):    
        super().display_info() 
        print(f"  Author: {self.author}")

    

class Electronic(Product):
    def __init__(self, product_id: str, name: str, price: float, specs: str):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):        
        super().display_info() 
        print(f"  Specifications: {self.specs}")


    

class Clothing(Product):
    
    def __init__(self, product_id: str, name: str, price: float, size: str):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        
        super().display_info() 
        print(f"  Size: {self.size}")


book = Book("B001", "The Hitchhiker's Guide to the Galaxy", 12.99, "Douglas Adams")
electronic = Electronic("E002", "iPhone 15", 999.99, "6.1-inch display, A17 Bionic chip")
clothing = Clothing("C003", "Levi's Jeans", 59.99, "32W x 32L")

book.display_info()
print("-" * 20)  
electronic.display_info()
print("-" * 20) 
clothing.display_info()