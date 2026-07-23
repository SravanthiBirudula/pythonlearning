#search
text = "Maria is a Data Engineer and she is 27 years old"
print("Is 'Maria' in text? ", "Maria" in text)
print("Index of 'Maria' in text: ", text.find("Maria"))

phone  = "+971-50-1234567"
print("Is '+971' in phone? ", phone.startswith("+971"))

email = "birudula.sravanthi@gmail.com"
print("Is 'gmail' in email? ", email.endswith("outlook.com"))
print("Is '@' in email? ", "@" in email)

#----------------------------------------------------------------------------

phone1 = "+971-50-1234567"
phone2 = "00971-50-1234567"
phone3 = "0-50-1234567"

print(phone1[5:])
print(phone2[6:])
print(phone3[2:])

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
#------------------------------------------------------------------------------

#validation--------------------------------------------------------------------
country = "India"
print(country.isalpha())
phone = "971501234567"
Actualphone = "+971501234567"
value = 90.1
val1 = 90
print(phone.isdigit())
print(" ".isspace())
print(Actualphone.isnumeric())
print(val1.is_integer())