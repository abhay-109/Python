# 14. Build a dictionary where the keys are product names and the values are their prices.
# Implement options to:
# a. Add a new product
# b. Update price of an existing product

# c. Find products within a given price range
d={}

def add_product():
    key=input('enter the product name : ')
    d[key]=int(input('enter the price : '))
    print(f"The product was added ")


def updata_price():
    key=input('enter the product name : ')
    print(f"The current price of the {key} : {d[key]}")
    if key in d:
        d[key]=d[key]=int(input('enter the new price : '))


def Price_range():
    mi=int(input('Enter the minimum price : '))
    ma=int(input('Enter the max price : '))
    range_of_products=[]
    for key in d:
        if d[key]>mi and d[key]<ma:
            range_of_products.append(f'{key} : {d[key]}')
    print(range_of_products)


while True:

    chose=int(input('Enter the choices \n 1.add prduct \n 2.updata_price \n 3.Prices_range \n 4.exit \n'))
    if chose==1:
        add_product()
    elif chose==2:
        updata_price()
    elif chose==3:
        Price_range()
    elif chose==4:
        break
    else:
        print('please the enter the valide number ')
 
