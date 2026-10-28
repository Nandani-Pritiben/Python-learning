def func_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
func_kwargs(name='neha',Roll_no=12)