r= """GROCERY STORE
   \tCustomer Receipt"""

book1_title = "python Basics"
book2_title = "Data Science Intro"

book1_price = 450
book2_price = 600

a= "Booktitle: {} - ₹{}".format(book1_title,book1_price)
b = "Booktitle: {} - ₹{}".format(book2_title,book2_price)

total_price = book1_price + book2_price

c = "total price : ₹{}\n".format(total_price)

thank_you = "\nThank you for shopping!"

receipt = r + "\n"+ a + "\n" + b + "\n" + c + thank_you

print(receipt.upper())