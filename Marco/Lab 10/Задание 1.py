import re


def search(k):
    with open("pi.txt") as f:
        count = 1
        st = f.read(len(k) + 1)
        while st[1:] != k:
            st = st[1:] + f.read(1)
            count += 1
            if count == 10000000:
                print("В этом файле нет")
                break

    return count


print(search('999999'))
print(search('888888'))
print(search('000000'))
print(search('123456'))
print(search('9083011'))
