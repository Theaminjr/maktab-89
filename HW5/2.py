
class Product:
    num = 0
    def __call__(self, a):
        self.num += a
        return self
    
    def __repr__(self):
        result = self.num
        self.num = 0
        return f"{result}"
  

Add = Product()
print(Add(3))
print(Add(3)(5))