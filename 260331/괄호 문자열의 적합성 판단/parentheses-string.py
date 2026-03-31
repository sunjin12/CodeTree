str = input()
st = []

for p in str:
    if p == '(':
        st.append('(')
    else:
        if not st:
            st.append("E")
            break
        st.pop()
    
if st:
    print("No")
else:
    print("Yes")