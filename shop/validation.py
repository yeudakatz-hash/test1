from .shopping_cart import *
import json


def str_to_int(string):
    try:
        return int(string)
    except:
        return None



def check_num(num):
    if str_to_int(num) > 0:
        return False
    return True



def is_id_exist(p_id):
    for i in products:
        if i["id"] == str_to_int(p_id):
            return False
    return True



def total_price(id_product, quantities_product):
    for i in products:
        if i["id"] == str_to_int(id_product):
            return str_to_int(quantities_product) * i["price"]


def discount(total_price):
    if total_price < 300:
        return 0
    elif total_price < 700:
        return  5
    elif total_price < 1500:
        return  10
    else:
        return 15





