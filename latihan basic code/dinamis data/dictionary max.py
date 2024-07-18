#harga max tiap dari beberapa buah
harga_buah={"apel":11000,"pisang":7500,"pepaya":6000,"manggis":5000,"peer":3000,"melon":5560,"leci":2000}


def max_buah(x):
    max=0
    for i in x.values():
        if i > max:
            max=i
    return max

print(max_buah(harga_buah))