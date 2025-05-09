inventory = []

def add_product():
    product = input("Ingrese nombre del producto: ")
    price = input ("Ingrese el valor del producto: ")
    product_q = input("Ingrese la cantidad del producto: ")
    product_dict = { "name" : product, "price" : price, "product_q" : product_q
    }
    inventory.append(product_dict)
    # print (inventory)

    
def search_product ():
    user_search = input("¿Que producto desea buscar y/o consultar?:")
    for x in inventory: 
        if x ["name"] == user_search.lower():
            print ("Producto encontrado!")
            print ("Producto", x["name"])
            print ("Precio", x["price"])
            print ("Cantidad", x["product_q"])
            break
    else:
        print("Producto no encontrado.")


def deleted():
    inventory.remove = input("Que producto se desea eliminar: ")


def menu ():
    while True:
        user_options = input("""Bienvenido seleccione una de las siguientes opciones 
                             1.Añadir producto
                             2.Consultar producto     
                             3.Editar y/o actualizar producto
                             4.Eliminar producto
                             5.Consultar valor total del inventario 
                             6.Salir
                             """)
        if user_options == "1":
            add_product()
        elif user_options == "2":
            search_product()
        elif user_options == "3":
            pass
        elif user_options == "4":
            pass
        elif user_options == "5":
            pass
        elif user_options == "6":
            break
        else:
            print("Ingrese solo valores validos")



menu()



