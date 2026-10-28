input_char='bananaKing'
first_char=''

for char in input_char:
    if input_char.count(char)==1:
        print('first char is',char)
        break
