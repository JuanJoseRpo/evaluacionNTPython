
import random

productos = []
zonaA = {'limite': 50, 'unidades': 0}
zonaB = {'limite': 50, 'unidades': 0}
zonaC = {'limite': 50, 'unidades': 0}
zonaD = {'limite': 50, 'unidades': 0}
opcion=None

while opcion !=6:
    
    print('**********************************************')
    print('*******************NVENTARIO******************')
    print('**********************************************')
    print('1. Registrar producto ')
    print('2. Mostrar todos los productos en bodega')
    print('3. Buscar por nombre ')
    print('4. Buscar y modificar el numero de unidades  ')
    print('5. Buscar y eliminar un producto  ')
    print('6. Salir ')
    opcion = int(input('Digita una opcion: '))
    if opcion==1:
        producto={}
        
        listaNumerosGenerados=[]
        numerosAleatorios = random.randint(1,201)
        while numerosAleatorios in listaNumerosGenerados:
            numerosAleatorios = random.randint(1, 201)

        listaNumerosGenerados.append(numerosAleatorios)        
        producto['id'] = listaNumerosGenerados
        producto['Nombre'] = input('Ingresa el nombre del producto: ')
        producto['Precio Unitario'] = int(input('Ingresa el precio unitario del producto: '))
        producto['Ubicacion'] = input('Ingresa la ubicacion en la tienda (A,B,C,D): ').lower()
        producto['Numero de unidades'] = int(input('Ingresa el numero de unidades compradas: '))
        
        
        if producto['Ubicacion'] == 'a':
            if zonaA['unidades'] + producto['Numero de unidades'] <= zonaA['limite']:
                zonaA['unidades'] += producto['Numero de unidades']
            else:
                print('-----------------------------------------------------------------')
                print(f'¡La zona A no puede almacenar más de {zonaA["limite"]} unidades!')
                print('-----------------------------------------------------------------')
                continue
        elif producto['Ubicacion'] == 'b':
            if zonaB['unidades'] + producto['Numero de unidades'] <= zonaB['limite']:
                zonaB['unidades'] += producto['Numero de unidades']
            else:
                print('-----------------------------------------------------------------')
                print(f'¡La zona B no puede almacenar más de {zonaB["limite"]} unidades!')  
                print('-----------------------------------------------------------------') 
                continue   
        elif producto['Ubicacion'] == 'c':
            if zonaC['unidades'] + producto['Numero de unidades'] <= zonaC['limite']:
                zonaC['unidades'] += producto['Numero de unidades']
            else:
                print('-----------------------------------------------------------------')
                print(f'¡La zona C no puede almacenar más de {zonaC["limite"]} unidades!') 
                print('-----------------------------------------------------------------') 
                continue    
        elif producto['Ubicacion'] == 'd':
            if zonaD['unidades'] + producto['Numero de unidades'] <= zonaD['limite']:
                zonaD['unidades'] += producto['Numero de unidades']
            else:
                print('-----------------------------------------------------------------')
                print(f'¡La zona D no puede almacenar más de {zonaD["limite"]} unidades!')   
                print('-----------------------------------------------------------------') 
                continue 
        else:
            print('------------------------------------------')
            print('Ubicación no válida. Inténtalo nuevamente.')
            print('------------------------------------------')
            continue
        producto['Descripcion'] = input ('Ingresa una descripcion del producto: ')
        producto['Casa'] = input ('Ingresa la casa o editorial: ')
        producto['Referencia'] = input('Ingresa su referencia: ')
        producto['Pais'] = input('Ingresa su pais de origen: ')
        producto['Garantia'] = input('Garantia extendida: ')
        
            
        productos.append(producto)
        
      
    elif opcion == 2:
        for productoAuxiliar in productos:
            print(f'Nombre: {productoAuxiliar["Nombre"]} \nPrecio Unitario: {productoAuxiliar["Precio Unitario"]} \nUbicacion: {productoAuxiliar["Ubicacion"]} \nCasa: {productoAuxiliar["Casa"]} \nDescripcion: {productoAuxiliar["Descripcion"]} \nReferencia: {productoAuxiliar["Referencia"]} \nPais: {productoAuxiliar["Pais"]} \nNumero de unidades: {productoAuxiliar["Numero de unidades"]} \nGarantia: {productoAuxiliar["Garantia"]}')
    elif opcion == 3:
        print('******Buscar producto por nombre******')
        nombreIngresado = input('Ingresa el nombre del producto que buscas: ').lower()
        
        if not nombreIngresado.isalpha():
            print('------------------------------------')
            print('Error: Debes introducir solo letras.')
            print('------------------------------------')
        elif nombreIngresado.isalpha() :
            for productoAuxiliar in productos:
                if productoAuxiliar['Nombre'].lower() == nombreIngresado.lower():
                    print(f'id: {productoAuxiliar["id"]}\nNombre: {productoAuxiliar["Nombre"]}\nPrecio Unitario: {productoAuxiliar["Precio Unitario"]}\nDescripcion: {productoAuxiliar["Descripcion"]}')
                    if productoAuxiliar['Garantia'] == 'si'.lower():
                        print(f' si hay garantia mi papa')
                    elif productoAuxiliar['Nombre'].lower() != nombreIngresado.lower():
                        print(f' El nombre -{nombreIngresado}- no se encuentra en la base de datos')
                        
    elif opcion == 4:
        print('******Buscar producto por nombre******')
        nombreIngresado = input('Ingresa el nombre del producto que buscas modificar: ').lower()
        
        if not nombreIngresado.isalpha():
            print('------------------------------------')
            print('Error: Debes introducir solo letras.')
            print('------------------------------------')
        elif nombreIngresado.isalpha() :
            for productoAuxiliar in productos:
                if productoAuxiliar['Nombre'].lower() == nombreIngresado.lower():
                    print(f'Nombre: {productoAuxiliar["Nombre"]}\nNumero de unidades: {productoAuxiliar["Numero de unidades"]}')
                    nuevaCantidad = int(input('Ingresa la nueva cantidad que deseas restar: '))
                    if nuevaCantidad < productoAuxiliar["Numero de unidades"]:
                       cantidadModificada = int(productoAuxiliar["Numero de unidades"]-nuevaCantidad)
                       print(f'ok la nueva cantidad de {productoAuxiliar["Nombre"]} es de {cantidadModificada}')
                    else:
                        print('La cantidad que ingresaste es mayor a la que hay en el inventario. Ingresa una cantidad menor')  
                elif productoAuxiliar['Nombre'].lower() != nombreIngresado.lower():
                    print(f' El nombre -{nombreIngresado}- no se encuentra en la base de datos')
                else:
                    print('Intenta de nuevo')    
    
    elif opcion == 5:
        nombreIngresado = input('Ingresa el nombre del producto que deseas eliminar: ').lower()
        if not nombreIngresado.isalpha():
            print('------------------------------------')
            print('Error: Debes introducir solo letras.')
            print('------------------------------------')
        elif nombreIngresado.isalpha() :
            for i in range(len(productos)):
                if productos[i]['Nombre'].lower() == nombreIngresado.lower():
                    print(f'el producto es: \n{productos[i]["id"]}\nNombre: {productos[i]["Nombre"]}\nPrecio Unitario: {productos[i]["Precio Unitario"]}\nDescripcion: {productos[i]["Descripcion"]}')
                    confirmacionEliminar= input('Este es el producto que seleccionaste.¿Deseas eliminarlo? Escribe "Si" para confirmar  o "No" para cancelar: ')
                    if confirmacionEliminar.lower() == 'si':
                        del productos[i]
                        print('Producto eliminado.')
                    else:
                        print('No se elimino')
                elif productos[i]['Nombre'] != nombreIngresado.lower():
                    print(f' El nombre -{nombreIngresado}- no se encuentra en la base de datos')
                  
       


