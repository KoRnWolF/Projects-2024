def add(*args):
    totals = int()
    for n in args:
        totals = totals + n
    return totals

total = add(3, 4, 9, 10, 23, 100)
print(total)