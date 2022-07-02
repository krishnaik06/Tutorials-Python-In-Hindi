def hello(*args,**kwargs):
    print(args)
    print(kwargs)

#hello("Krish","Naik",age=32,dob=1989)

lst=list(('Krish', 'Naik'))
dict_val={'age': 32, 'dob': 1989}

#hello(*lst,**dict_val)

hello("Krish","NAik","1","2","1989",age=10,dob=1990)