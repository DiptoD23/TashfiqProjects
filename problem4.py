products = []
prices = []
quantities = []

n = int(input("Enter the number of products: "))

for i in range(n):
    print(f"\nEnter details for Product {i + 1}")
    name = input("Product Name: ")
    price = float(input("Unit Price: "))
    quantity = int(input("Quantity: "))

    products.append(name)
    prices.append(price)
    quantities.append(quantity)

subtotal = sum(price * qty for price, qty in zip(prices, quantities))

if subtotal >= 500: discount_rate = 0.15
elif subtotal >= 200: discount_rate = 0.10
else: discount_rate = 0.0

discount_amount = subtotal * discount_rate
final_bill = subtotal - discount_amount

max_price_index = prices.index(max(prices))
max_qty_index = quantities.index(max(quantities))

print()
for name, price, qty in zip(products, prices, quantities):
    print(f"{name:<10} | {qty:>3} x taka {price:>6.2f} = taka {price * qty:>7.2f}")

print("_" * 60)
print(f"{'Subtotal:':<28}  taka {subtotal:>8.2f}")
print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<28} -taka {discount_amount:>8.2f}")
print(f"{'Final Bill:':<28}  taka {final_bill:>8.2f}")
print("_" * 60)

print(f"Most Expensive Product: {products[max_price_index]} (taka {prices[max_price_index]:.2f})")
print(f"Highest Quantity Product: {products[max_qty_index]} ({quantities[max_qty_index]} units)")