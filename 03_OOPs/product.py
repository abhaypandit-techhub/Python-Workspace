class product :
  def __init__(self,product_id,name,price,stock) :
    self.product_id=product_id
    self.name=name
    self.price=price
    self.stock=stock

  def product_info (self) :
    print((f"{self.product_id}|{self.name}|{self.price}|{self.stock}"))

  def check_stock(self):
    if self.stock > 0 :
      print(f"Product {self.name} is available")
    else :
      print(f"Product {self.name} out of stock") 

prod_1=product(554,"mouse",546,0)
prod_1.product_info()
prod_1.check_stock()
prod_2=product(244,"keyboard",999,1)
prod_2.product_info()
prod_2.check_stock()
       