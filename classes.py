import math

class Items:
    def __init__(self,qty,gift,name,price):
        self.qty=qty
        self.gift=gift
        self.name=name
        self.price=price
    
    def cal_tot(self):
        item_tot=self.qty*self.price
        if self.gift=='y':
            item_tot=item_tot+(self.qty*1)
        return item_tot

class Cart:
    def __init__(self):
        self.items=[]

    def add_items(self,item):
        self.items.append(item)
        
    def sub_tot(self):
        self.sub_total_amount=0
        for item in self.items:
            self.sub_total_amount=self.sub_total_amount+item.cal_tot()
        
        return self.sub_total_amount
    
    def gift_ship_cost(self):
        ship_fee=5         #per 1 package containing 10 items
        tot_qty=sum(item.qty for item in self.items)
        gift_fee_applied=tot_qty*1
        packages=math.ceil(tot_qty/10)       #round to nextwhole number
        ship_fee_applied=packages*5
        return gift_fee_applied,ship_fee_applied

    
    def discount_applied(self):
        all_discount={}
        total_qty=sum(item.qty for item in self.items)
        self.discount_app=""
        self.discount_price=0
        if self.sub_total_amount>0:
             if self.sub_total_amount>200:
                self.discount_app="flat_10_discount"
                self.discount_price=10
                all_discount[self.discount_app]=self.discount_price
             if  (item.qty>10 for item in self.items):
                self.discount_app="bulk_5_discount"
                for item in self.items:
                    if item.qty>10:
                        self.discount_price=self.sub_tot()*0.05
                all_discount[self.discount_app]=self.discount_price
             if total_qty>20:
                self.discount_app="bulk_10_discount"
                self.discount_price=self.sub_tot()*0.1
                all_discount[self.discount_app]=self.discount_price
             if total_qty>30 and  (item.qty>15 for item in self.items):
                self.discount_app="tiered_50_discount"
                self.discount_price=self.sub_tot()*0.5
                all_discount[self.discount_app]=self.discount_price

        best=max(all_discount,key=all_discount.get)
        print(all_discount)
        disc=best
        disc_amt=all_discount[best]

        return disc,disc_amt
    
    def apply_discount(self,amount):
        self.disc_amt=amount
        disc_applied_amt=self.sub_tot()-self.disc_amt
        return disc_applied_amt





        