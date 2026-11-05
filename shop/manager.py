from .validation import *



def get_id():
    prod = input("enter id of product: ")
    while True:
        if str_to_int(prod) is None:
            prod = input("Enter ID number.")
        elif check_num(prod) is True:
            prod = input("Enter positive ID number.")
        elif is_id_exist(prod) is True:
            print("The product does not exist.")
            prod = input("Enter ID number.")
        else:
            break
    return prod



def get_num(action):
    quantity = input(f"enter {action} of product: ")
    while True:
        if str_to_int(quantity) is None:
            quantity = input(f"Enter {action} number.")
        elif check_num(quantity) is True:
            quantity = input(f"Enter positive {action} number.")
        else:
            break
    return quantity




def id_order():
    return len(carts) + 1










def create_order():
    total = 0
    cont = True
    while cont is True:
        id_product = get_id()
        quantities_product = get_num("quantity")
        total += total_price(id_product, quantities_product)
        cont = input("Do you need another product?\n"
              "Enter 0 to exit")
        if cont != 0:
            cont = True
        else:
            break
    discount_percents = discount(total)
    print(f"price {total} , discount{discount_percents}% , after discount {(total * (100 / (100 - discount_percents)))}")
    return  f"id_order{id_order()} , price {total} , discount{discount_percents}% , after discount {(total * (100 / (100 - discount_percents)))}"




def show_all_orders():
    for cart in carts:
        print(cart)



def find_order_by_id():
    search_id = get_num("order_id")
    try:
        for cart in carts:
            if cart["id"] == search_id:
                print(cart)
                return cart
    except:
        print("dont have carts yet")


def close_order():
    close_id = find_order_by_id()
    return f"status: CLOSED {close_id}"



def Show_sales_report():
    pass