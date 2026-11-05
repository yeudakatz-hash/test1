from shop.printer import menu
from shop.manager import *


choose = None

while True:


    if choose == "1":
        create_order()

    elif choose == "2":
        show_all_orders()

    elif choose == "3":
        find_order_by_id()

    elif choose == "4":
        close_order()

    elif choose == "5":
        Show_sales_report()

    elif choose == "0":
        break

    choose = menu()



