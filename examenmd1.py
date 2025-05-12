inventory = []

#It works with .lower and .strip to avoid problems with uppercase letters or not adding a name to the product.
def add_product():
    while True:
        product_add = input("Ingrese el producto que desea agregar: ").strip().lower()
        if product_add:
            break
        else:
            print("El nombre del producto no puede estar en blanco.")
    
    while True:
        try:
            price = float(input("Ingrese el precio de este producto: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido para el precio.")
    
    while True:
        try:
            quantity = int(input("Ingrese la cantidad de este producto: "))
            break
        except ValueError:
            print("Ingrese solo valores enteros válidos.")
    
    product_dict = {"name": product_add, "price": price, "quantity": quantity}
    inventory.append(product_dict)
    print(f"Producto '{product_add}' agregado correctamente.")

#Section for searching for the existence of a product by repeating the .strip and .lower
def search_product():
    user_search = input("Ingrese el producto que desea verificar: ").strip().lower()
    for product in inventory:
        if product["name"] == user_search:
            print("Producto encontrado!")
            print(f"Nombre: {product['name']}")
            print(f"Precio: {product['price']}")
            print(f"Cantidad: {product['quantity']}")
            return
    print("Producto no encontrado. Verifique nuevamente.")

#Inventory editing menu with try and except to avoid code corruption when using invalid inputs
def edit_product():
    name = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
    for product in inventory:
        if product["name"] == name:
            print(f"Producto encontrado: {product}")
            print("¿Qué desea editar?")
            print("1. Nombre")
            print("2. Precio")
            print("3. Cantidad")
            
            while True:
                try:
                    choice = int(input("Ingrese el número de la opción: "))
                    if choice == 1:
                        new_name = input("Ingrese el nuevo nombre: ").strip().lower()
                        if new_name:
                            product["name"] = new_name
                            print("Nombre actualizado correctamente.")
                        else:
                            print("El nombre no puede estar vacío.")
                        break
                    elif choice == 2:
                        new_price = float(input("Ingrese el nuevo precio: "))
                        product["price"] = new_price
                        print("Precio actualizado correctamente.")
                        break
                    elif choice == 3:
                        new_quantity = int(input("Ingrese la nueva cantidad: "))
                        product["quantity"] = new_quantity
                        print("Cantidad actualizada correctamente.")
                        break
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Ingrese un valor válido.")
            return
    print(f"Producto '{name}' no encontrado.")

def delete_product():
    product_deleted = input("¿Qué producto desea eliminar?: ").strip().lower()
    for product in inventory:
        if product["name"] == product_deleted:
            inventory.remove(product)
            print(f"Producto '{product_deleted}' eliminado correctamente.")
            return
    print(f"Producto '{product_deleted}' no encontrado.")

#The total inventory is aggregated using the lambda method.
def total_inventory():
    total = sum(map(lambda p: p["price"] * p["quantity"], inventory))
    print(f"Valor total del inventario: {total:.2f}")

def show_inventory():
    if not inventory:
        print("El inventario está vacío.")
        return
    
    print("Inventario completo:")
    print("-" * 40)
    print(f"{'Nombre'} | {'Precio'} | {'Cantidad'}")
    print("-" * 40)
    for product in inventory:
        print(f"{product['name']} | ${product['price']} | {product['quantity']}")
    print("-" * 40)

def menu():
    while True:
        print("-" * 60)
        print("Bienvenido seleccione la opcion que desea realizar")
        print("1. Agregar producto")
        print("2. Verificar existencia")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Ver valor total del inventario")
        print("6. Mostrar todo el inventario")
        print("7. Salir")
        print("-" * 60)
        choice = input("Seleccione una opción: ")
       
        if choice == "1":
            add_product()
        elif choice == "2":
            search_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            total_inventory()
        elif choice == "6":
            show_inventory()
        elif choice == "7":
            print("Espero hayas disfrutado tu tiempo en nuestro sistema :D hasta luego")
            break
        else:
            print("Opción inválida.")
            
#Before executing the menu function, the user is asked to select whether they want to start by adding several items or if they want to advance to the main menu.
while True:
    print("-" * 60)
    user_choice = input("""Bienvenido antes de comenzar debes seleccionar una opcion:
    1).Agregar productos que desee de entrada
    2).Continuar con el programa
    3).Cierre total del programa
    """)
    print("-" * 60)
    if user_choice == "1":
        while True:
            try:
                total_items = int(input("cuantos items desea añadir: "))
                if int (total_items) >0:
                    for i in range(total_items):
                        add_product()
                    break
                else:
                    print("solo numeros validos")
            except ValueError:
                print("Solo entradas validas.")
   
    elif user_choice == "2":
        menu()
    elif user_choice =="3":
        break    
    else:
        print("Solo entradas validas")