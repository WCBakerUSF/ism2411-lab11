print("---Exercise 1---")

customer = {
"Name": "Not-Alice",
"email": "alice@example.com",
"tier":"platinum",
"ytd_spend": 12400
}

print(customer)


print("---Exercise 2---")





print("---Exercise 3---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

for key in customer:
    print(key, customer[key])


