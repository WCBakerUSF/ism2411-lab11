print("---Exercise 1---")

customer = {
"Name": "Not-Alice",
"email": "alice@example.com",
"tier":"platinum",
"ytd_spend": 12400
}

print(customer)


print("---Exercise 2---")
customer['phone'] = '555-5555'
print(customer)






print("---Exercise 3---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

print("---Exercise 4---")
for key, value

for key in customer:
    print(key, customer[key])

print("---Exercise 5---")

tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15
                }

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price}")

print("---Exercise 6---")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}: ${discount:.2f} off a $300 purchase)")


print("---Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")


print()

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},

]