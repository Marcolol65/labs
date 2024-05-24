count, *gg = map(int, input().split())

div_2 = []
div_13 = []
div_26 = []
for arg in gg:
    if arg % 2 == 0:
        if arg % 26 == 0:
            div_26.append(arg)
            continue
        div_2.append(arg)
    elif arg % 13 == 0:
        div_13.append(arg)

print(count, gg)
print(len(div_2) * len(div_13) + len(div_26) * (count - 1))