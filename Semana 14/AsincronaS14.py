#Definimos una función para ejecutar el programa

def ejecutar_programa():
    print("¡BIENVENIDO AL PROGRAMA!\n")
    
    # Lista de nombres de los departamentos
    departamentos = ["Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán", "La libertad", "Morazán", "La Paz", "Santa Ana", "San Miguel", "San Salvador", "San Vicente", "Sonsonate", "La Unión", "Usulután"]
    
    # Diccionario que contiene los municipios de cada departamento
    municipios_por_departamento = {
         "Ahuachapán" : ["Ahuachapán", "Apaneca", "Atiquizaya", "Concepción de Ataco", "El Refugio"],
         "Cabañas" : ["Cinquera","Dolores", "Guacotecti", "Ilobasco", "Jutiapa"],
         "Chalatenango" : ["Agua Caliente", "Arcatao", "Azacualpa", "Cancasque", "Citalá", "Comalapa"],
         "Cuscatlán" : ["Cojutepeque", "Candelaria", "El Carmen", "Suchitoto", "San José Guayabal", "San Pedro Perulapán"],
         "La libertad" : ["Antiguo Cuscatlán", "Chiltiupán", "Ciudad Arce", "Colón", "Comasagua", "Huizúcar"],
         "Morazán" : ["Arambala", "Cacaopera", "Chilanga", "Corinto", "Delicias de Concepción", "El Divisadero"],
         "La Paz" : ["Zacatecoluca","Cuyultitán","El Rosario","Jerusalén","Mercedes La Ceiba","Olocuilta"],
         "San Miguel" : ["Carolina", "Chapeltique", "Chinameca", "Chirilagua", "Ciudad Barrios", "Comacarán"],
         "San Salvador" : ["Aguilares", "Apopa", "Ayutuxtepeque", "Cuscatancingo", "Ciudad Delgado", "El Paisnal"],
         "San Vicente" : ["Apastepeque", "Guadalupe", "San Cateyano Istepeque", "San Esteban Catarina", "San Ildefonso", "San Lorenzo"],
         "Sonsonate" : ["Acajutla", "Armenia", "Caluco", "Cuisnahuat", "Izalco", "Juayúa"],
         "La Unión" : ["Anamorós", "Bolívar", "Concepción de Oriente", "Conchagua", "El Carmen", "El Sauce"],
         "Usulután" : ["Alegría", "Berlín", "California", "Concepción Batres", "El Truinfo", "Ereguayquín"]
    }

    # Preguntar al usuario si quiere ejecutar el programa
    respuesta = input("\n¿Desea ejecutar el programa? (Sí/No): ")
    
    while respuesta.lower() == "sí":
        # Mostrar la lista de departamentos
        print("\nLista de departamentos: ")
        for departamento in departamentos:
            print("- " + departamento)
        

        # Solicitar al usuario el nombre del departamento
        departamento_elegido = input("\nIngrese el nombre de un departamento: ")
        
        # Verificar si el departamento ingresado por el usuario existe en la lista
        if departamento_elegido.capitalize() not in departamentos:
            print("\nEl departamento ingresado no es válido.")

        else:
            # Obtener la lista de municipios del departamento elegido
            municipios = municipios_por_departamento[departamento_elegido.capitalize()]
            
            # Mostrar la lista de municipios
            print("\nLista de municipios de " + departamento_elegido.capitalize() + ":")
            for municipio in municipios:
                print("- " + municipio)
             # Preguntamos al usuario si desea consultar otro departamento
            respuesta = input("\n¿Desea consultar los municipios de otro departamento? (S/N): ")
            if respuesta.upper() == "N":
                print("\nGracias por utilizar nuestro programa. ¡Hasta la próxima!")
                return
            # Si la respuesta es sí, pedimos que ingrese nuevamente un departamento
            elif respuesta.upper() == "S":
                ejecutar_programa()
        
ejecutar_programa()