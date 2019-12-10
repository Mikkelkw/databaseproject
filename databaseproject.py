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
        for cartId, date, customer_id, ordered, shipped, cartItemid, cartId, item_sku, qty in cursor:
            print(item_sku)

    # add total cost and name in print

    def catalog():
        cursor.execute("SELECT * FROM Item")
        for sku, name, qty, price in cursor:
            print(name, price)

    def addToCart(usrId):
        cartId = ''
        c = 0
        query = f"SELECT * FROM Item"
        cursor.execute(query)
        for sku, name, qty, price in cursor:
            print(sku, name, price)
        
        add = input("Enter the SKU of the item you would like to add: ")
 
        query = f"SELECT * From Item WHERE sku = %s"
        cursor.execute(query, (add, ))
        for sku, name, qty, price in cursor:
            c+=1

        if c== 0: 
            print('Not a valid SKU. Please try again')
        
        else:
            qty = input("Enter the quantity you wish to add to the cart: ")
            try:
                query = f"SELECT * FROM Cart WHERE customer_id = {usrId}"
                cursor.execute(query)
                for id, date, customer_id, shipped, ordered in cursor:
                    cartId = id
                
                query = f"INSERT INTO CartItem (cart_id, item_sku, qty) values(%s, %s, %s)"
                cursor.execute(query, (cartId, add, qty, ))
                cnx.commit()
                print('added to cart')

            except:
                query = f"INSERT INTO Cart (customer_id) values({usrId})"
                cursor.execute(query)
                cnx.commit()

                query = f"INSERT INTO CartItem (item_sku, qty) values(%s, %s, %s)"
                cursor.execute(query, (add, qty, ))
                cnx.commit()
                print('Cart Created')

    def deleteFromCart(usrId):
        cartId = ''
        viewCart(usrId)
        sku = input("Enter the SKU of the item you would like to remove: ")

        try:
            query = f"SELECT * From Cart Where customer_id = {usrId}"
            cursor.execute(query)
            for id, date, customer_id, ordered, shipped in cursor:
                cartId = id
                print(cartId)

            query = f"DELETE From CartItem Where cart_id = {cartId}"
            print('Cart Deleted!')

        except:
            print(No existing cart)

    def clearCart(usrId):
        query = f"Delete From Cart Where customer_id = {usrId}"

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
        
        if action == '4':
            deleteFromCart(usrId)

        if action == '5':
            clearCart(usrId)

        if action == '6':
            updateUser(usrId)
       
        if action=='7':
            running = False
            print('Goodbye')

except mysql.connector.Error as err:
    print(err)
else:
    cnx.close