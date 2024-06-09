def calculate(item_list, item_idx):
    item_price = float(item_list[item_idx + 1])
    item_amount = int(input(f"How many {item_list[item_idx]} do you want: "))
    item_cost = item_price * item_amount
    item = item_list[item_idx] + "(" + str(item_amount) + ")"
    cost = "${:,.2f}".format(item_cost)
    cartitems.append(item)
    print(f"\nItem cost: {item} = {cost}")
    return item_cost


# -------------------------<<<<< Menu Function has area variables >>>>>-------------------------
def menu(area):
    if area == "f":
        menu_list = fruit
        menu_title = "Fruit Section"
        menu_items = ["(A)pples", "a(V)ocado", "(B)anana", "(K)iwifruit", "(O)ranges"]
        menu_pick = ["a", "v", "b", "k", "o"]
        choice = ["apples", "avocado", "banana", "kiwi", "oranges"]

    elif area == "v":
        menu_list = veges
        menu_title = "Vegetable Section"
        menu_items = ["(C)ucumber", "(L)ettuce", "(O)nions", "(P)otatoes", "(S)alad"]
        menu_pick = ["c", "l", "o", "p", "s"]
        choice = ["cucumber", "lettuce", "onions", "potatoes", "salad"]

    else:
        menu_list = deli
        menu_title = "Delicatessan"
        menu_items = ["(H)am", "(M)ussels", "(S)alami", "sa(L)mon", "sa(U)sages"]
        menu_pick = ["h", "m", "s", "l", "u"]
        choice = ["ham", "mussels", "salami", "salmon", "sausages"]

    # -------------------------<<<<< Returns 5 items >>>>>-------------------------
    return menu_list, menu_title, menu_items, menu_pick, choice


# -------------------------<<<<< Lists of Item & Price >>>>>-------------------------
fruit = ["banana", 2.00, "avocado", 1.50, "oranges", 1.50, "apples", 2.00, "kiwi", 1.50]
veges = ["onions", 2.50, "cucumber", 5.25, "potatoes", 3.50, "lettuce", 4.50, "salad", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

# -------------------------<<<<< Globals for Cart price and items >>>>>-------------------------
cartprice = 0
cartitems = []

while True:
    print("\nSelect Area to Shop")
    print("(F)ruit")
    print("(V)egetables")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()

    if len(area) > 1:
        area = area[0]

    area_check = ["f", "v", "d", "x"]

    if area not in area_check:
        print("Selection Error 1")
        continue

    elif area == "x":
        print("Thank you for shopping with us")
        currency = "${:,.2f}".format(cartprice)
        print(f"\nTotal cost = {currency}")
        print(f"The items selected where: {cartitems}")
        break

    else:
        area_list, area_title, area_menu, area_pick, choices = menu(area)

        print(area_title)

        for z in area_menu:
            print(z)

        print("(G)o Back")

        menu_pick = input("Enter Letter: ").lower()

        if len(menu_pick) > 1:
            menu_pick = menu_pick[0]

        if menu_pick == "g":
            continue

        elif menu_pick not in area_pick:
            print("Selection Error 2")
            continue

        else:
            item_idx = 0

            for y in range(0, len(area_pick)):
                if menu_pick == area_pick[y]:
                    item_idx = y

            item_find = area_list.index(choices[item_idx])
            item_cost = calculate(area_list, item_find)
            cartprice += item_cost

        currency = "${:,.2f}".format(cartprice)
        print(f"\nCost so far = {currency}")
        print(f"Cart items = {cartitems}")
