
class Product:
    # ... (Base class remains the same) ... 

 class Book("Product"):
    # ... (Book class remains the same) ...

  class Electronic("Product"):
    # ... (Electronic class remains the same) ...

   class Clothing("Product"):
    # ... (Clothing class remains the same) ...

# Instantiate objects
    book1 = "Book"("B001", "The Lord of the Rings", 24.99, "J.R.R. Tolkien", "9780547928227")
laptop1 = "Electronic"("E002", "SuperLaptop", 999.00, "TechGiant", {"Processor": "UltraChip", "RAM": "16GB", "Storage": "1TB SSD"})
jeans1 = "Clothing"("C002", "Denim Jeans", 39.99, "M", "Blue", "Denim")

# Call display methods
print("Book Details:")
book1 = "display_info"()
print("\n---\n")

# Expected Output:
# Book Details:
# Product ID: B001
# Name: The Lord of the Rings
# Price: $ 24.99
# Author: J.R.R. Tolkien
# ISBN: 9780547928227
# ---

print("Laptop Details:")
laptop1.display_info()
print("\n---\n")

# Expected Output:
# Laptop Details:
# Product ID: E002
# Name: SuperLaptop
# Price: $ 999.0
# Brand: TechGiant
# Specifications:
#   Processor: UltraChip
#   RAM: 16GB
#   Storage: 1TB SSD
# ---

print("Jeans Details:")
jeans1.display_info() 

# Expected Output:
# Jeans Details:
# Product ID: C002
# Name: Denim Jeans
# Price: $ 39.99
# Size: M
# Color: Blue
# Material: Denim 