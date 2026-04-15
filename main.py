
orders = [
    ["anna", 250],
    ["per", 300],
    ["anna", 150],
    ["maria", 400],
    ["per", 200],
    ["anna", 100]
]

totalSum = {}

for name, amount in orders:
    if name in totalSum:
        totalSum[name] += amount
    else:
        totalSum[name] = amount

sorted_orders = sorted(totalSum.items(), key=lambda x: x[1], reverse=True)

for name, amount in sorted_orders:
    print(f"{name}: {amount}")


