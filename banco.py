import tkinter as tk

class Cliente:
    # Definición del método o función constructora
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, domicilio):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.domicilio = domicilio  # Cambio: 'domicilio' en lugar de 'direccion'

class Cuenta:
    def __init__(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = 1000.0

    def abonar(self, cantidad):
        self.saldo += cantidad

    def cargar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        else:
            return False

class Movimiento:
    def __init__(self, fecha_movimiento, descripcion, cargo, abono, saldo):
        self.fecha_movimiento = fecha_movimiento
        self.descripcion = descripcion
        self.cargo = cargo
        self.abono = abono
        self.saldo = saldo

class EstadoCuenta:
    def __init__(self, cliente: Cliente, cuenta: Cuenta, fecha_ingreso, movimiento: Movimiento):
        self.cliente = cliente
        self.cuenta = cuenta
        self.fecha_ingreso = fecha_ingreso
        self.movimiento = movimiento

# Se realiza la instancia del la clase cliente, 'datos' es un objeto de tipo Cliente
datos = Cliente("abril", "sanchez", "tovar", "29 de Abril", "CBTiS 75")

# Crear la ventana principal de la interfaz gráfica
root = tk.Tk()
root.title("Datos del Cliente")
root.geometry("400x300")

# Crear etiquetas (Labels) para mostrar la información del cliente
label_nombre = tk.Label(root, text=f"Nombre: {datos.nombre}")
label_nombre.pack(pady=5)

label_apellido_paterno = tk.Label(root, text=f"Apellido Paterno: {datos.apellido_paterno}")
label_apellido_paterno.pack(pady=5)

label_apellido_materno = tk.Label(root, text=f"Apellido Materno: {datos.apellido_materno}")
label_apellido_materno.pack(pady=5)

label_fecha_nacimiento = tk.Label(root, text=f"Fecha de Nacimiento: {datos.fecha_nacimiento}")
label_fecha_nacimiento.pack(pady=5)

label_domicilio = tk.Label(root, text=f"Domicilio: {datos.domicilio}")
label_domicilio.pack(pady=5)

# Iniciar el ciclo principal de la interfaz gráfica
root.mainloop()
