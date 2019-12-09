import mysql.connector

try:
    cnx = mysql.connector.connect(
        user ='mk0918',
        password = '3560Hemsedal',
        host ='127.0.0.1',
        database='acm1123_theWatchStore'
    )
    cursor = cnx.cursor()
    running = True;

    def startup():
        customerId = input("Please insert your customer ID: ")
        query = f"select * from Customer where id = %s;"
        usrId = ""
        cursor.execute(query, (customerId,))
        for id, fname, lname, email, address, zip in cursor:
            usrId = id
            print(usrId)
        return usrId


    def viewCart(userID):
        query = f"select * from Cart inner join CartItem on CartItem.cart_id = Cart.id where Cart.customer_id = %s;"
        cursor.execute(query, (userID,))
        for cartId, date, customer_id, ordered, shipped, cartItemid, item_sku, qty, cost in cursor:
            print(item_sku)

    def catalog():
        cursor.execute("SELECT * FROM Item")
        for sku, name, qty, price in cursor:
            print(name, price)

    usrId = startup()
    while usrId == "":
        print("This User ID is not a valid input")
        usrId = startup()


    print("Successful User ID")

    while(running):
        print("\n"
            "What action would you like to perform?\n"
            "1. View cart\n"
            "2. View catalog")

        action = input("Insert action: ")

        if action == '1':
            print("Your current cart items:")
            viewCart(usrId)

        if action == '2':
            print("Items currently avaliable for sale: ")
            catalog()
        running = False


except mysql.connector.Error as err:
    print(err)
else:
    cnx.close



