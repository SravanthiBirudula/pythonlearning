#nested loops are loops inside another loop. The inner loop will be executed one time for each iteration of the outer loop.
#example of nested loops
for i in range(1, 6):
    for j in range(1, 6):
        print(f"i: {i}, j: {j}")
        for k in range(1, 6):
            print(f"i: {i}, j: {j}, k: {k}")

for x in range(3):
    for y in range(3):
        for z in range(3):
            print(f"({x}, {y}, {z})")

#use cases
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(f"Color: {color} - Size: {size}")

years=[2020, 2021, 2022]
months=["Jan", "Feb", "Mar"]
days=range(1, 29)
for year in years:
    for month in months:
        for day in days:
            print(f"report_{year}_{month}_{day}.csv")

#tables , columns , rows : select count(*) from customers where id is null
tables = ["customers", "orders", "products"]
columns = ["id", "created_date"]

for t in tables:
    for c in columns:
        print(f"select count(*) from {t} where {c} IS NULL;")

