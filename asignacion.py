import time
import random

# Variables para controlar los octetos de la dirección IP
ultimo_octeto = 1
penultimo_octeto = 0

# Diccionario para almacenar las asignaciones de IP
asignaciones = {}

def generar_direccion_ip():
    global ultimo_octeto, penultimo_octeto

    # Incrementar el penúltimo octeto si se utilizan todas las direcciones IP del último octeto
    if ultimo_octeto > 254:
        penultimo_octeto += 1
        ultimo_octeto = 1

    # Generar la dirección IP
    direccion_ip = f"192.168.{penultimo_octeto}.{ultimo_octeto}"

    # Incrementar el último octeto
    ultimo_octeto += 1

    return direccion_ip

def asignar_ip(direccion_mac):
    if direccion_mac in asignaciones:
        print("¡La dirección MAC ya está asignada!")
        return asignaciones[direccion_mac]
    else:
        direccion_ip = generar_direccion_ip()
        asignaciones[direccion_mac] = direccion_ip
        return direccion_ip

def inhabilitar_asignacion(direccion_mac):
    if direccion_mac in asignaciones:
        del asignaciones[direccion_mac]
        return True
    else:
        return False

def mostrar_asignaciones():
    print("Asignaciones de IP:")
    for direccion_mac, direccion_ip in asignaciones.items():
        estado = "A" if validar_ip(direccion_ip) else "X"
        print(f"Dirección MAC: {direccion_mac}, Dirección IP: {direccion_ip}, Estado: {estado}")

def validar_ip(ip):
    # Implementa aquí tu lógica de validación de IP
    # Puedes utilizar la función socket.inet_aton(ip) o cualquier otra técnica de validación
    return True

# Generar un conjunto de direcciones MAC aleatorias
cantidad_mac = 300
direcciones_mac = set()
while len(direcciones_mac) < cantidad_mac:
    direccion_mac = "%012x" % random.randint(0, 2**48-1)
    direccion_mac = ":".join(direccion_mac[i:i+2] for i in range(0, len(direccion_mac), 2))
    direcciones_mac.add(direccion_mac)

# Asignar las direcciones MAC generadas
for direccion_mac in direcciones_mac:
    direccion_ip = asignar_ip(direccion_mac)
    estado = "A" if validar_ip(direccion_ip) else "X"
    print(f"La dirección IP asignada a la MAC {direccion_mac} es {direccion_ip}. Estado: {estado}")

# Mostrar las asignaciones
mostrar_asignaciones()

# Esperar 15 minutos
time.sleep(5)

# Ejecutar el bucle principal
while True:
    # Solicitar acción al usuario
    accion = input("Ingrese la acción a realizar (A para asignar / I para inhabilitar / Q para salir): ")

    if accion.lower() == "a":
        # Solicitar dirección MAC al usuario
        direccion_mac = input("Ingrese los 12 dígitos de la dirección MAC: ")

        # Agregar los dos puntos (:) cada dos caracteres
        direccion_mac = ":".join(direccion_mac[i:i+2] for i in range(0, len(direccion_mac), 2))

        # Asignar IP y mostrar resultado
        direccion_ip = asignar_ip(direccion_mac)
        if direccion_ip:
            estado = "A" if validar_ip(direccion_ip) else "X"
            print(f"La dirección IP asignada a la MAC {direccion_mac} es {direccion_ip}. Estado: {estado}")

    elif accion.lower() == "i":
        # Solicitar dirección MAC al usuario
        direccion_mac = input("Ingrese los 12 dígitos de la dirección MAC a inhabilitar: ")

        # Agregar los dos puntos (:) cada dos caracteres
        direccion_mac = ":".join(direccion_mac[i:i+2] for i in range(0, len(direccion_mac), 2))

        # Inhabilitar asignación y mostrar resultado
        if inhabilitar_asignacion(direccion_mac):
            print(f"La asignación para la MAC {direccion_mac} ha sido inhabilitada.")

    elif accion.lower() == "q":
        # Salir del programa
        break

    # Mostrar las asignaciones
    mostrar_asignaciones()
