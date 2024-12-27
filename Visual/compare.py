h1 = 0
h2 = 0
h3 = 0
order = []
for i in range(20):
    if i == 0:
        order.append(0)
    else:
        if h1 <= h2 and h1 <= h3:
            h1 += 1.5
            print(h1)
            order.append(1)
        elif h2 <= h1 and h2 <= h3:
            h2 += 1
            order.append(2)
        else:
            h3 += 0.5
            order.append(3)
print(order)
