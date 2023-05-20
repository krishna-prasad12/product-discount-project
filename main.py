from classes import *


def main():
    p_list=[]
    products={        #products and price
    "ProductA":20,
    "Product B":40,
    "Product C":50
    }
    cart=Cart()
    for name,price in products.items():
        qty=int(input(f"enter the quantity of {name} :"))
        gift_wrap=input("Should the product be gift wraped (y/n)")
        item=Items(qty,gift_wrap,name,price)                     #object of class items
        cart.add_items(item)
        item_tot=item.cal_tot()
        p_list.append([name,qty,item_tot])
 
#printing all the details of the products
    print("\n"*2)
    print(f"****************Invoice Details*****************")
    for item in p_list:
        product_det=f"product:{item[0]}\nordered quantity:{item[1]}15\n total amount:${item[2]}"
        print(product_det)
    sub=cart.sub_tot()
    print(f"subtotal:{sub}")
    disc_name,disc_amt=cart.discount_applied()
    print(f"discount applied:{disc_name}  discount amount:${disc_amt}")
    gift_fee,ship_fee=cart.gift_ship_cost()
    print(f"Shipping fee:{ship_fee} gift fee:{gift_fee}")
    disc_applied=cart.apply_discount(disc_amt)
    total=disc_applied+ship_fee
    print(f"Total:${total}")
    
main()

