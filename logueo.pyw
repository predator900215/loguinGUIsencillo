from tkinter import Tk, Button, Label, Entry, Frame, StringVar, messagebox
import conexionmysql


class raiz:
    def __init__(self):
        self.ventana = Tk()
        self.frame = None
        self.boton_ventana = None
        self.boton_frame = None
        self.entrada_frame = None
        self.label_frame = None
        self.boton_frame = None
        self.lista_ventanas = []
        self.lista_de_frames = []
        self.lista_botones_ventana = []
        self.lista_botones_frame = []
        self.lista_entradas_frame = []
        self.lista_labels_frame = []
        self.mostrar_frame = True
        self.texto_boton = StringVar(value='registro')
        self.contador_de_frames = 0
        self.contador_de_ventanas = 0
        self.contador_botones_ventana = 0
        self.contador_botones_frame = 0
        self.contador_entradas_frame = 0
        self.contador_label_frame = 0
        self.contenido_entrada = ''

    def ventana_crear(self, titulo, color_fondo):
        ventana = self.ventana
        self.lista_ventanas.append(ventana)
        self.contador_de_ventanas += 1
        ventana.title('{}'.format(titulo))
        ventana.config(bg='{}'.format(color_fondo))

    def ventana_tamaño_personalizado(self, indice_ventana, ancho, alto):
        ventana = self.lista_ventanas[indice_ventana]
        ventana.geometry('{}x{}'.format(ancho, alto))

    def ventana_tamaño_pantalla_completa(self, indice_ventana):
        ventana = self.lista_ventanas[indice_ventana]
        ventana.state('zoomed')

    def ventana_posicionar_boton(self, indice_botones_ventana, x, y, width, height):
        boton_de_ventana = self.lista_botones_ventana[indice_botones_ventana]
        boton_de_ventana.place(x=x, y=y, width=width, height=height)

    def ventana_asignarfuncion_boton(self, indice_botones_ventana, funcion_boton_ventana):
        boton_de_ventana = self.lista_botones_ventana[indice_botones_ventana]
        boton_de_ventana.config(command=funcion_boton_ventana)

    def ventana_ejecutar_programa(self):
        self.ventana.mainloop()

    def frame_crear(self, color_fondo):
        self.frame = Frame(self.ventana)
        frame = self.frame
        self.lista_de_frames.append(frame)
        self.contador_de_frames += 1
        frame.config(bg='{}'.format(color_fondo))

    def frame_posicion_tamaño_personalizado(self, indice_frame, x, y, width, height):
        frame = self.lista_de_frames[indice_frame]
        frame.place(x=x, y=y, width=width, height=height)

    def frame_posicion_tamaño_raiz(self, indice_frame):
        frame = self.lista_de_frames[indice_frame]
        frame.place(x=0, y=0, relwidth=1, relheight=1)
        frame.configure(padx=10, pady=10)

    def frame_crear_boton(self, x, y, width, height, nombre_boton=None):
        self.boton_frame = Button(self.frame, text=nombre_boton)
        boton_frame = self.boton_frame
        self.lista_botones_frame.append(boton_frame)
        self.contador_botones_frame += 1
        boton_frame.place(x=x, y=y, width=width, height=height)
        boton_frame.config(font='Arial 12 bold')

    def frame_asignarfuncionboton(self, indice_boton, funcion_boton):
        boton_frame = self.lista_botones_frame[indice_boton]
        boton_frame.config(command=funcion_boton)

    def frame_crear_entrada(self, x, y, width, height, show=None):
        entrada = Entry(self.frame)
        entrada.place(x=x, y=y, width=width, height=height)
        entrada.config(justify='center')
        self.lista_entradas_frame.append(entrada)
        self.contador_entradas_frame += 1
        entrada.config(bd=3)
        entrada.config(font='Arial 12 bold')
        entrada.config(show=show)

    def frame_crear_label(self, texto, x, y, width, height, colorfondo=None, colorletra=None):
        self.label_frame = Label(self.frame, text=texto)
        label_frame = self.label_frame
        self.lista_labels_frame.append(label_frame)
        self.contador_label_frame += 1
        label_frame.place(x=x, y=y, width=width, height=height)
        label_frame.config(bg=colorfondo)
        label_frame.config(fg=colorletra)
        label_frame.config(font='Arial 12 bold')

    def frame_ocultar(self, indice_frame):
        frame = self.lista_de_frames[indice_frame]
        frame.place_forget()

    def registro_db(self):
        entrada1 = self.lista_entradas_frame[0]
        contenido1 = entrada1.get()
        palabra_deseada = "@gmail.com"
        if palabra_deseada in contenido1:
            entrada2 = self.lista_entradas_frame[1]
            contenido2 = entrada2.get()
            conexion = conexionmysql.Connection()
            resultados = conexion.consulta_usuario(contenido1, contenido2)
            if resultados:
                messagebox.showinfo("Error", "El usuario ya esta registrado, presiona ingresar")
            else:
                conexion.inserta_usuario(contenido1, contenido2)
                messagebox.showinfo("Felicidades", "Registro exitoso, presiona ingresar")
        else:
            messagebox.showinfo("Atencion", "Registrate con tu cuenta de Gmail")

    def borrar_usuario(self):
        entrada1 = self.lista_entradas_frame[0]
        contenido1 = entrada1.get()
        entrada2 = self.lista_entradas_frame[1]
        contenido2 = entrada2.get()
        conexion = conexionmysql.Connection()
        resultados = conexion.consulta_usuario(contenido1, contenido2)
        if resultados:
            respuesta = messagebox.askyesno('Confirmacion', 'Deseas continuar con la eliminacion de la cuenta ?')
            if respuesta:
                conexion.borrar_usuario(contenido1, contenido2)
                messagebox.showinfo("Atencion", "Usuario eliminado con exito")
            else:
                messagebox.showinfo("Atencion", "La cuenta se conserva")
        else:
            messagebox.showinfo("Atencion", "Usuario o contraseña incorrectos")

    def ingresar(self):
        entrada1 = self.lista_entradas_frame[0]
        contenido1 = entrada1.get()
        entrada2 = self.lista_entradas_frame[1]
        contenido2 = entrada2.get()
        conexion = conexionmysql.Connection()
        resultados = conexion.consulta_usuario(contenido1, contenido2)
        if resultados:
            ventana1.ventana.title('Campo de trabajo')
            ventana1.ventana_tamaño_pantalla_completa(0)
            ventana1.frame_ocultar(0)
            ventana1.frame_posicion_tamaño_raiz(1)
        else:
            messagebox.showinfo("Atencion", "Usuario o contraseña incorrectos")

    def mostrar_datos_programa(self):
        print('se han creado: ', self.contador_de_ventanas, ' ventanas')
        print('se han creado: ', self.contador_de_frames, ' frames')
        print('se han creado: ', self.contador_botones_ventana, ' botones en la ventana')
        print('se han creado: ', self.contador_botones_frame, ' botones en el frame')
        print('se han creado: ', self.contador_label_frame, ' labels en en el frame')
        print('se han creado: ', self.contador_entradas_frame, ' entradas en el frame')


ventana1 = raiz()
ventana1.ventana_crear('Login', '#000000')
ventana1.ventana_tamaño_personalizado(0, 510, 200)
ventana1.frame_crear('#000000')
ventana1.frame_posicion_tamaño_raiz(0)
ventana1.frame_crear_label('Usuario', 20, 30, 100, 30, '#000000', '#FBFFDC')
ventana1.frame_crear_label('Contraseña', 20, 70, 100, 30, '#000000', '#FBFFDC')
ventana1.frame_crear_entrada(130, 20, 350, 30)
ventana1.frame_crear_entrada(130, 60, 350, 30, '*')
ventana1.frame_crear_boton(130, 110, 120, 30, 'crear usuario')
ventana1.frame_crear_boton(250, 110, 120, 30, 'borrar usuario')
ventana1.frame_crear_boton(370, 110, 110, 30, 'ingresar')
ventana1.frame_asignarfuncionboton(0, ventana1.registro_db)
ventana1.frame_asignarfuncionboton(1, ventana1.borrar_usuario)
ventana1.frame_asignarfuncionboton(2, ventana1.ingresar)
ventana1.frame_crear('#000000')
ventana1.frame_ocultar(1)
ventana1.frame_crear_label('Aqui ya estas dentro del programa', 30, 30, 300, 30, '#000000', '#FBFFDC')
ventana1.mostrar_datos_programa()
ventana1.ventana_ejecutar_programa()
