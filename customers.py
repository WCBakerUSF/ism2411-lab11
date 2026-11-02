print("---Exercise 1---")

customer = {
"Name": "Not-Alice",
"email": "alice@example.com",
"tier":"platinum",
"ytd_spend": 12400
}

print(customer)


print("---Exercise 2---")

customer.update("phone": "iphone")




print("---Exercise 3---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

for key, value

for key in customer:
    print(key, customer[key])

print()
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