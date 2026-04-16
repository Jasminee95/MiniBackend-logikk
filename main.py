# ##                          Ordre-system ---- Regner ut total bruk per person

# orders = [
#     ["anna", 250],
#     ["per", 300],
#     ["anna", 150],
#     ["maria", 400],
#     ["per", 200],
#     ["anna", 100]
# ]
#
# totalSum = {}
#
# for name, amount in orders:
#     if name in totalSum:
#         totalSum[name] += amount
#     else:
#         totalSum[name] = amount
#
# sorted_orders = sorted(totalSum.items(), key=lambda x: x[1], reverse=True)
#
# for name, amount in sorted_orders:
#     print(f"{name}: {amount}")




# ##            Finn lengste streak

# days = [1, 2, 3, 5, 6, 10, 11, 12, 13]
# days = [100, 4, 200, 1, 3, 2]
# days = sorted(days)
#
# current_streak = 1
# longest_streak = 1
#
# for i in range(1, len(days)):
#     if days[i] == days[i - 1] + 1:
#         current_streak += 1
#     else:
#         current_streak = 1
#     if current_streak > longest_streak:
#         longest_streak = current_streak
#
# print(longest_streak)

#  ##               Raskere sortering O(n)


days = [100, 4, 200, 1, 3, 2]

day_set = set(days)
longest_streak = 0

for day in day_set:
    if (day - 1) not in day_set:
        curr_day = day
        current_streak = 1

        while (curr_day + 1) in day_set:
            curr_day += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

print(longest_streak)


