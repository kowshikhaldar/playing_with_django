def imilab(*args):
    for arg in args:
        print(arg)


imilab("asssssssam",1,98,True,'ki koros vai ',[9,8,7])

#same output
# mogo=("asssssssam",1,98,True,'kisu kor ',[9,10,7])

# imilab(*mogo) 


def kw32(**args):
    for arg in args:
        print(f"key: {arg} ,Value : {args[arg]}")




kw32( john="zimas",mon="limbs",con="32")


z=dict( john=98, leisun="limbs",con=True)
kw32(**z)

# print(z)