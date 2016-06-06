expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)
print(type(expenses))
for item, cost in (expenses):
    print(item, cost)
