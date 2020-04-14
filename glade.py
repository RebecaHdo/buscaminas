#!/usr/bin/python
# -*- coding: UTF-8 -*-

#importa tu libreria favorita <3
import gtk


class test():

    def __init__(self):

        #se asignan todas las tablas creadas en glade
        self.glade = gtk.Builder()
        self.glade.add_from_file('Buscaminas.glade')
        self.ventana = self.glade.get_object('window1')
        self.tabla = self.glade.get_object('table2')
        self.tabla2 = self.glade.get_object('hpaned1')
        self.ajuste = self.glade.get_object('table1')
        self.glade.connect_signals(self)

        self.ventana.show()
        return None

    def gtk_true(self, boton):
        #pruebas de pulsar los botones
        print boton.get_label()
        print self.ventana.get_size()

    def on_window1_delete_event(self, widget):
        #cierra el programa
        gtk.main_quit()
        return None

    def on_window1_check_resize(self, ventana):
        #lo importante de esto

        #x e y son el tamaño de la ventana y dif su diferencia
        #para que los botones siempre sean cuadrados perfectos se añade espacio en la tabla exterior
        x, y = ventana.get_size()
        dif = abs(x - y)
        dif = dif / 2
        if x >= y:
            self.ajuste.set_col_spacing(0, dif)
            self.ajuste.set_col_spacing(1, dif)
            self.ajuste.set_row_spacing(0, 0)
            self.ajuste.set_row_spacing(1, 0)
        else:
            self.ajuste.set_row_spacing(0, dif)
            self.ajuste.set_row_spacing(1, dif)
            self.ajuste.set_col_spacing(0, 0)
            self.ajuste.set_col_spacing(1, 0)

            #si algo no te cuadra dimelo por tele

if __name__ == '__main__':
    # Instanciamos la interfaz
    app = test()
    # Lanzamos el bucle de gestión de eventos
    gtk.main()
    print "Termina el programa"
