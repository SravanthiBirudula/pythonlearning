#convert the full country names into 2 letter abbrivations 
country = "United States of America"


#achieve it using if else statements
if country == "Canada":
    print("CA")
elif country == "Mexico":
    print("MX")
elif country == "United States of America":
    print("US")
else:
    print("Unknown country")

#using match case statements

match country:
    case "United States of America" | "USA":
        print("US")
    case "Canada":
        print("CA")
    case "Mexico":
        print("MX")
    case _:
        print("Unknown country")
    