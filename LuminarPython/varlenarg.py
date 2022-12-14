# variable length argument  *args - non keyword argument

# def var_length(*arg):
#     print(type(arg))
#     for i in arg:
#         print(i)
#
# var_length(10,20)
# var_length(1,2,3)


# **kargs - keyword argument

def fun(**karg):
    print(type(karg))
    for k,v in karg.items():
        print(k,":",v)

fun(Name='Anu',cls='BCA')
