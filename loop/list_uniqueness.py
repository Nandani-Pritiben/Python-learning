items=['apple','banana','mango','banana','apple','orange']
unique_item=set()
duplicate=set()
count=[]

for i in items:
    if(i in unique_item):
         print('duplicate',i)
         break
    else:
         unique_item.add(i)
    