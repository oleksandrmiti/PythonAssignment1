# PythonAssignment1
## My first Assignment using Python at Cork College of Commerce.
# PROGRAM SPECIFICATION:

Walled Town Ale has three products: Butchers’ Pale Ale, Farriers’ IPA and Gatehouse Brown Ale. An invoice is issued for each order received.<br>
<br>A discount applies based on the number of barrels of each product purchased.<br><br>
To ensure that each delivery journey is cost effective for the brewery a surcharge is applied if the
delivery truck rack(s) used for that order are not full. Each rack has space for up to 15 barrels. <br><br>
### Basic Price per barrel:
• Butchers’ Pale Ale  €125.50<br>
• Farriers’ IPA       €105.90<br>
• Gatehouse Brown Ale €132.35<br>
### Discounts:<br>
• €10 for each 10 barrels of Butchers’ Pale<br>
• €8.40 for each 12 barrels of Farriers’ IPA.<br>
• €11.65 for each 9 barrels of Gatehouse Brown Ale.<br><br>
### Surcharge:
• €2.00 for each empty rack space.<br><br> The application works as follows:<br>
The user enters the name and address (3 separate lines) of the client company and its phone number (minimum 10 characters, digits only, no spaces). The number of barrels of each product is also entered. An invoice is produced as seen below.
### Notes:
1. The invoice number is 8 characters in length and is generated from the client company name and phone number as follows:
<br>  a. First 3 characters: all invoices begin with the initials of Walled Town Ale – i.e. WTA
<br>  b. Next 2 characters: the first 2 digits of the phone number (excluding leading zeros)
<br>  c. Next 2 characters: the final 2 digits of the phone number
<br>  d. The second last character of the purchasing company’s name (upper-case)
<br> e.g. phone number: 0214882499, company name Bob’s Brewhouse’. Invoice no: WTA2199S
2. Lines marked 1 in the invoice are only to be included if a surcharge applies
3. Lines marked 2 in the invoice are only to be included if a discount applies. A line should not be
included for any individual item that is not discounted.
4. The border around the receipt is for illustration only, and does not need to be coded.
Ale.
    
5. You can prompt the user to enter a date manually, or you can use import "datetime" to your program.
6. Input and output are to conform to industry standards (prompts should be clear and consistent).
7. Currency is to be suitably formatted, with two digits for the cent amount, i.e., €36.50. Use commas as appropriate, i.e., €10,412.60.
8. Numeric values should be right aligned.
<br><img width="540" alt="image" src="https://github.com/oleksandrmiti/PythonAssignment1/assets/114529427/b337ecde-0f7d-40ae-8b8a-25c124ecc5cf">
<br>
You are required to design, code, and test a program that will read in the details of each customer along with the number of barrels of each product ordered. You should then print out an invoice (to screen) that will mirror the invoice shown above.
