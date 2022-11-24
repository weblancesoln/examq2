data = ["1234", "123456", "12345678910", "1234562", "013", "011", "8543210", "12345", "1238974"]

lx = []
ly = []
def item_tuple(arg):
    x = 0
    while x < len(arg):
        if len(arg[x]) <= 4:
            lx.append(arg[x])
        elif len(arg[x]) >= 7:
            ly.append(arg[x])
        x = x+1
        
    y = (lx,ly)
    print(y)
    
item_tuple(data)








