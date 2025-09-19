import tkinter as tk
from tkinter import messagebox

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Productos")
        self.root.geometry("500x400")

       
        self.productos = []

       
        self.lbl_nombre = tk.Label(root, text="Nombre del producto:")
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.lbl_cantidad = tk.Label(root, text="Cantidad:")
        self.lbl_cantidad.pack()
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack()

        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_producto)
        self.btn_agregar.pack(pady=5)

        self.btn_actualizar = tk.Button(root, text="Actualizar", command=self.actualizar_producto)
        self.btn_actualizar.pack(pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_producto)
        self.btn_eliminar.pack(pady=5)

        self.lista = tk.Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

        self.lista.bind("<<ListboxSelect>>", self.seleccionar_producto)

    def agregar_producto(self):
        try:
            nombre = self.entry_nombre.get()
            cantidad = int(self.entry_cantidad.get())
            if nombre:
                self.productos.append({"nombre": nombre, "cantidad": cantidad})
                self.mostrar_productos()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Advertencia", "El nombre no puede estar vacío.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    def mostrar_productos(self):
        self.lista.delete(0, tk.END)
        for i, producto in enumerate(self.productos):
            self.lista.insert(tk.END, f"{i+1}. {producto['nombre']} - Cantidad: {producto['cantidad']}")

    def seleccionar_producto(self, event):
        try:
            index = self.lista.curselection()[0]
            producto = self.productos[index]
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, producto["nombre"])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, producto["cantidad"])
        except IndexError:
            pass

    def actualizar_producto(self):
        try:
            index = self.lista.curselection()[0]
            nombre = self.entry_nombre.get()
            cantidad = int(self.entry_cantidad.get())
            self.productos[index] = {"nombre": nombre, "cantidad": cantidad}
            self.mostrar_productos()
            self.limpiar_campos()
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Selecciona un producto y asegúrate que la cantidad es un número.")

    def eliminar_producto(self):
        try:
            index = self.lista.curselection()[0]
            del self.productos[index]
            self.mostrar_productos()
            self.limpiar_campos()
        except IndexError:
            messagebox.showerror("Error", "Selecciona un producto para eliminar.")

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
