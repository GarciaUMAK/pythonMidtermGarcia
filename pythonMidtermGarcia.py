def calculation(q, ppu):
    totalAmmount = q * ppu

    file = open(sales_log.txt, "a")
    file.write(f"Item Name: {itemName}, total Ammount: {totalAmmount}, Price Per Unit: {ppu}")


def exitNa():
    exit()
itemName = ""
quantitySold = ""
pricePerUnit = ""

lop = True

while lop:

    print("========================================")
    print("SALES RECORD MANAGEMENT SYSTEM")
    print("========================================")
    u = input("Select an option (1-4): ")

    if u == "1":
        try:
            itemName = input("Item name: ")
            quantitySold = input("Quantity sold: ")
            quantitySold = int(quantitySold)
            pricePerUnit = input("Price per unit: ")
            pricePerUnit = float(pricePerUnit)
            calculation(quantitySold, pricePerUnit)

        except ValueError:
            print("Error! Please input proper value.")


    if u == "4":
        print("Thank you for using the Sales Record Management System.")
        exitNa()