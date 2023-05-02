amount_coin = int(input("Введите количество монет :"))
count_head = 0
count_tail = 0
  for i in range(amount_coin):
  x = int(input())
    if x == 0:
    count_head += 1
    else:
    count_tail += 1
if count_head > count_tail:
print(f"Минимальное количество монет, которые нужно перевернуть -"{count_tail})
else:
print(f"Минимальное количество монет, которые нужно перевернуть -"{count_head})
