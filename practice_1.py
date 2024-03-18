# linear
# binary

import random
data = []
for i in range(20):
    data.append(random.randint(1, 50))
print(data)

target = int(input("target: "))
l = len(data) - 1
low = 0
i = 0
data.sort()
print(data)
while True:
    middle = (l + low) // 2
    if data[middle] == target:
        print(f"bu son {middle} indexda joylashgan")
        i += 1
        break

    elif data[middle] < target:
        low = middle + 1

    elif data[middle] > target:
        l = middle - 1

    i += 1

print(f"Qadamlar soni {i}")


"""print("uzunligi", len(data))
target = int(input("target: "))
step_by = 0
for i in data:
    if i == target:
        print(i)
        print(step_by)
        break
    else:
        step_by += 1"""
