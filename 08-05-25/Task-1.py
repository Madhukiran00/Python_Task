rows = 5 

for i in range(1, 2 * rows):  
    res = ""
    space = i - 1 if i <= rows else 2 * rows - i - 1
    cols = rows - i + 1 if i <= rows else i - rows + 1

    for sp in range(1, space + 1):
        res += " "

    for j in range(1, cols + 1):
        res += "* "

    print(res)
