str = input()
st = []

for p in str:
    if p == '(':
        st.append('(')
    else:
        if not st:
            print("No")
        st.pop()
    
    if st:
        print("No")
    else:
        print(Y)