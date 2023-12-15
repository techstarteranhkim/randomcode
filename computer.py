class Computer:
    def __init__(self, hwprice, swprice,cpu,gpu,ram,motherboard,psu,case,ssd):
        self.hwprice=hwprice
        self.swprice=swprice
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram
        self.motherboard=motherboard
        self.psu=psu
        self.case=case
        self.ssd=ssd
    
    def info_parts(self):
        print("Der PC besteht aus folgenden Teilen: ")
        print(f"CPU: {self.cpu}")
        print(f"GPU: {self.gpu}")
        print(f"RAM: {self.ram}")
        print(f"Motherboard: {self.motherboard}")
        print(f"PSU: {self.psu}")
        print(f"Case: {self.case}")
        print(f"SSD: {self.ssd}")
    
    def info_price(self):
        print(f"Der ganze PC kostet {self.hwprice}€ und {self.swprice}€, also ingesamt {int(self.swprice)+int(self.hwprice)}€")