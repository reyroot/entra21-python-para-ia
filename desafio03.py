sells = [850, 1200, 980, 1560, 720, 1100, 890, 1340, 630, 1450,
         970, 1280, 810, 1620, 750, 1050, 920, 1380, 660, 1490]

total = 0
better_day = 0
more_1000 = 0
peak_1500 = 0

for day , sell_day in enumerate(sells):
  total += sell_day
  if sell_day > better_day:
    better_day  = sell_day
  if sell_day >= 1000:
    more_1000 +=1
  if sell_day >= 1500 and peak_1500 == 0:
    peak_1500 = day + 1


print("Daily media: ", total / len(sells), " $")
print("Better day: ", better_day, " $")
print("Peak day: ", peak_1500)
print("More than 1000: ", more_1000)
