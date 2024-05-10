#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""

a = float(input("Please enter in the price of item #1: "))
b = float(input("Please enter in the price of item #2: "))
c = float(input("Please enter in the price of item #3: "))
d = float(input("Please enter in the price of item #4: "))
e = float(input("Please enter in the price of item #5: "))

subtotal = a + b + c + d + e
subtotal = round(subtotal, 2)

gst = subtotal * 0.05
gst = round(gst, 2)

pst = subtotal * 0.07
pst = round(pst, 2)

total = subtotal + gst + pst 
total = round(total, 2)

print('Your subtotal is',subtotal)
print('Your GST is',gst)
print('Your PST is',pst)
print('Your total is',total)

#done