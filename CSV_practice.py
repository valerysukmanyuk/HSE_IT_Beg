import csv

with open("employees.csv", "r") as csvfile:
    data = csv.reader(csvfile, delimiter= ",")
    
    for row in data: 
        print(", ".join(row))
