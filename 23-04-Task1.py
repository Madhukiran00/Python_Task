

class Laptop:
    
    def __init__(self,brand,model ,processor ,ram,storage):
        self.brand=brand
        self.model=model
        self.processor=processor
        self.ram=ram
        self.storage=storage
      
    def about(self):
        
        return f"Brand:{self.brand}, Model:{self.model},Processor:{self.processor},Ram:{self.ram},Storage:{self.storage}"
    
    
laptop1=Laptop("HP","OMEN 16","Intel Core i7","16GB DDR5","1TB SSD")
laptop2=Laptop("HP", "OMEN","AMD Rtzen","16GB","1TB")
laptop3=Laptop("Lenovo","IdeaPad","Intel Core Ultra 9","16GB","1TB")
laptop4=Laptop("Asus","Zen Book 14 OLED","Intel Core Ultra 7","16GB","1TB")
laptop5=Laptop("Dell","Inspiron 14","Intel core i5","*GB","512")
laptop6=Laptop("Lenovo","ThinkPad","Intel core i3","8GB","512 GB ")
laptop7=Laptop("Microsoft","Surface Laptop","Intel core i7","8GB","512 GB")
laptop8=Laptop("Aces","Aspire 5","Ryzen 5","8GB","512GB")

print(laptop1.about())
print(laptop2.about())
print(laptop3.about())
print(laptop4.about())
print(laptop5.about())
print(laptop6.about())
print(laptop7.about())
print(laptop8.about())


