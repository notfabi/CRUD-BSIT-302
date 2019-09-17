from tkinter import *

class Product:
    def __init__(self, merchandise, price, amount):
        self.merchandise = merchandise
        self.price = price
        self.amount = amount
        
    def getMerchandise(self):
        return self.merchandise

    def getPrice(self):
        return self.price

    def getAmount(self):
        return self.amount

    def updateSelf(self, merchandise, price, amount):
        self.merchandise = merchandise
        self.price = price
        self.amount = amount
        btn1['state'] = DISABLED
        btn2['state'] = NORMAL
        viewProducts()


def addProduct():
    global products
    product = Product(e1.get(), e2.get(), e3.get())
    products.append(product)
    viewProducts()

def deleteProduct(product):
    global products
    products.remove(product)
    viewProducts()

def updateProduct(product):
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e1.insert(0,product.getMerchandise())
    e2.insert(0,product.getPrice())
    e3.insert(0,product.getAmount())
    btn1['state'] = NORMAL
    btn2['state'] = DISABLED
    
    btn1.configure(command=lambda: product.updateSelf(e1.get(), e2.get(), e3.get()))
    

def viewProducts():
    global products
    
    row = 1
    list = separator.grid_slaves()
    for l in list:
        l.destroy()
        
    addHeaders()
    for product in products:
        Label(separator, text=product.getMerchandise(), background=color, width=10).grid(row=row, column=0, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product.getPrice(), background=color, width=10).grid(row=row, column=1, sticky=W+E+N+S , padx=10, pady=5)
        Label(separator, text=product.getAmount(),background=color, width=10).grid(row=row, column=2, sticky=W+E+N+S , padx=10, pady=5)

        btn_a1 = Button(separator, text="Change", width=7, command=lambda prod=product: updateProduct(prod))
        btn_a2 = Button(separator, text="Remove", width=7, command=lambda prod=product: deleteProduct(prod))

        btn_a1.grid(row=row, column=3, sticky=W, padx=5, pady=5)
        btn_a2.grid(row=row, column=4, sticky=E, padx=5, pady=5)
        row += 1

    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

def addHeaders():    
    separator.grid(row=5, column=0, columnspan=5, pady=5, sticky=W+E+N+S)
    Label(separator, text="Name", background=color, width=10).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(separator, text="Price", background=color, width=10).grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(separator, text="Quantity",background=color, width=10).grid(row=0, column=2, sticky=W, padx=10, pady=5)
    

products = []
color = "#d9d7d7"

root = Tk()
root.title("Merchandise Inventory System")
root.geometry("450x400") 
root.resizable(0, 0) 

Label(root, text="Merchandise Information").grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Merchandise Name: ").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Merchandise Price: ").grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Merchandise Quantity: ").grid(row=3, column=0, sticky=W, padx=10, pady=5)

e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root, width=40)

e1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)

btn1 = Button(root, text="Update List", width=15, state=DISABLED)
btn2 = Button(root, text="Add Merchandise", width=15, state=NORMAL, command=addProduct)

btn1.grid(row=4, column=1, sticky=W, padx=10, pady=5)
btn2.grid(row=4, column=2, sticky=E, padx=10, pady=5)

separator = Canvas(root, height=100, width=420, background=color, relief=SUNKEN)
addHeaders()
root.mainloop()
