import mysql.connector

try:
    cnx = mysql.connector.connect(
        user ='token_a0a8',
        password = 'oAOrFaz4iBpc1rET',
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

    # add total cost and name in print

    def catalog():
        cursor.execute("SELECT * FROM Item")
        for sku, name, qty, price in cursor:
            print(name, price)

    def addToCart(usrId):
        cartId = ''
        cursor.execute("SELECT * FROM Item")
        for sku, name, qty, price in cursor:
            print(sku, name, price)
        
        add = input("Enter the SKU of the item you would like to add: ")
        qty = input("Enter the quantity you wish to add to the cart: ")



        query = f"SELECT FROM Cart WHERE customer_id = %s"
        cursor.execute(query, (usrId, ))
        x = []
        for id, date, customer_id, shipped, ordered in cursor:
            s = id, date, customer_id, shipped, ordered
            x.append(s)

        if x == []
            query = f"""INSERT INTO CART (customer_id) values(%s)"""
            cursor.execute(query, (usrId, ))
            cnx.commit()

            query = f"SELECT * FROM Cart WHERE customer_id = {userId}"
            cursor.execute(query)
            for id, date, customer_id, shipped, ordered in cursor:
                cartID = id
            
            query = f"INSERT INTO CartItem (cart_id, sku, qty) values(%s, %s, %s)"\
            cursor.execute(query, (cartID, add, qty, ))

        else 
            # if there is already an existing cart 

    def deleteFromCart(usrId):
        viewCart(usrId)
        sku = input("Enter the SKU of the item you would like to remove: ")

    #def clearCart(usrId):

    def updateUser(usrId):
        query = f"Select * FROM Customer WHERE id = %s"
        cursor.execute(query,(usrId, ))

        for id, fname, lname, email, address, zip in cursor:
            print('Your current info')
            print(fname+ " " + lname, email, address, sep="\n")
            
        print("\n"
            "What information would you like to change \n"
            "1. First Name\n"
            "2. Last Name\n"
            "3. Email\n"
            "4. Address\n"
            "5. Back to menu")
        
        c = input("enter number: ")
        
        if c== '1':
            f = input("enter your new first name: ")

            query = (f"UPDATE Customer SET fname= %s WHERE id = %s")
            cursor.execute(query,(f, usrId, ))
            cnx.commit()

            print("First name updated")
        
        if c == '2':
            l = input("enter your new last name: ")

            query = (f"UPDATE Customer SET lname= %s WHERE id = %s")
            cursor.execute(query,(l, usrId, ))
            cnx.commit()

            print("Last name updated")

        if c == '3':
            e = input("enter your new email: ")

            query = (f"UPDATE Customer SET email = %s WHERE id = %s")
            cursor.execute(query,(e, usrId, ))
            cnx.commit()

            print("Email updated")

        if c == '4':
            a = input("enter your new address: ")

            query = (f"UPDATE Customer SET address= %s WHERE id = %s")
            cursor.execute(query,(a, usrId, ))
            cnx.commit()

            print("address updated")

        if c == '5':
            print('Main Menu')

    

    usrId = startup()
    while usrId == "":
        print("This User ID is not a valid input")
        usrId = startup()


    print("Successful User ID")
    # add hello first name 

    while(running):
        print("\n"
            "What action would you like to perform?\n"
            "1. View cart\n"
            "2. View catalog\n"
            "3. Add to cart\n"
            "4. Remove item from cart\n"
            "5. Clear your cart\n"
            "6. Update your info\n"
            "7. Exit")

        action = input("Insert action: ")

        if action == '1':
            print("Your current cart items:")
            viewCart(usrId)

        if action == '2':
            print("Items currently avaliable for sale: ")
            catalog()

        if action == '3':
            addToCart(usrId)

        if action == '6':
            updateUser(usrId)
       
        if action=='7':
            running = False
            print('Goodbye')

except mysql.connector.Error as err:
    print(err)
else:
    cnx.close