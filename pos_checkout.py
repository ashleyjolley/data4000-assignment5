
# Assignment 5 - Exercise 1: POS Checkout System

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

subtotal = 0.0
total_units = 0

while True:
    item_name = input("Item name (or DONE): ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == "":
        print("Item name cannot be blank.")
        continue

    while True:
        try:
            unit_price = float(input("Unit price: "))
            if unit_price <= 0:
                print("Price must be greater than 0.")
                continue
            if unit_price == float("inf") or unit_price != unit_price:
                print("Enter a valid finite price.")
                continue
            break
        except ValueError:
            print("Enter a valid price.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number.")

    subtotal += unit_price * quantity
    total_units += quantity

if total_units >= 10 or subtotal >= 100:
    discount = 10
else:
    discount = 0

total = subtotal * (1 - discount / 100)

if seed % 2 == 1:
    total = max(0, total - 3)
    perk = "YES"
else:
    perk = "NO"

print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount}%")
print(f"Perk applied: {perk}")
print(f"Total: ${total:.2f}")
