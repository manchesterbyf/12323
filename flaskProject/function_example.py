def hello(**kwargs):
    print(kwargs)

def outer(**kwargs):
    hello(**kwargs)

outer(a = 1,b = 2)