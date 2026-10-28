
# 1
for i in range(1, 6):
    # Multiply the string '*' by the current row number 'i'
    print(f"{'*' * (2*(6-i)-1):^10}")

# 2
for i in range(1, 6):
    # Multiply the string '*' by the current row number 'i'
    # if i==1:
    #      continue
    print(f"{'*' * (2*i-1):^10}")

# 1
for i in range(1, 6):
     x="*"
     x=x*i
     print(f'{x:>5}')

for i in range(1, 6):
     x="*"
     x=x*i
     print(f'{x}')

for i in range(1, 6):
     x="*"
     x=x*(6-i)
     print(f'{x:>5}')

for i in range(1, 6):
     x="*"
     x=x*(6-i)
     print(f'{x}')