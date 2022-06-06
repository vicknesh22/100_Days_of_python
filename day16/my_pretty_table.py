from prettytable import PrettyTable

# create object name table

table = PrettyTable()
# add column
table.add_column("Mobile Name", ["Mi", "Samsung", "oneplus"])
table.add_column("Type", ["cheap", "competitive", "creative"])
table.add_column("Price-Point", ["low", "high", "Medium"])
# add row
table.add_row(["Apple", "Premium", "High"])
# change align
table.align = "l"

print(table)
