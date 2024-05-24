st = str(input("Твои мысли..."))
st_ = st.replace(' ', '')
big = 0
small = 0
for i in st_:
    if i.isupper():
        big += 1
    else:
        small += 1
if big > small:
    print(st.upper())
elif small > big:
    print(st.lower())
else:
    print(st)
