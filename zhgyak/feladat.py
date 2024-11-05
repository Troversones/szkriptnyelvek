class Product: 
    def __init__(self, name, price, weight = 1):
        self.name = name
        self.price = price
        self.weight = weight

    def apply_discount(self, learazas):
        return self.price * (1 - learazas / 100)
    
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg"
    
    def __eq__(self, other):
        if not isinstance(other, Product) or not isinstance(self, Product):
            return False
         
        return (self.name == other.name and
                self.price == other.price and
                self.weight == other.weight)
    
    def __iadd__(self, other):
        if not isinstance(other, Product) or not isinstance(self, Product):
            return self
        
        if self.name == other.name:
            self.weight += other.weight
            if self.price < other.price:
                self.price = other.price

        return self
        
        

p1 = Product("nev",120,5)
p2 = Product("nev",130,5)

p1 += p2

print(p1.apply_discount(15))

