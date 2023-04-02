def give_change(amount):

    change = [0, 0, 0, 0, 0, 0]

    if amount // 100 > 0:
        change[5] = amount // 100
        amount = amount % 100

    if amount // 50 > 0:
        change[4] = amount // 50
        amount = amount % 50

    if amount // 20 > 0:
        change[3] = amount // 20
        amount = amount % 20

    if amount // 10 > 0:
        change[2] = amount // 10
        amount = amount % 10

    if amount // 5 > 0:
        change[1] = amount // 5
        amount = amount % 5

    change[0] = amount

    return tuple(change)
