# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import warnings
from utn_fra.pygame_widgets.game_sound import GameSound


'''
################# INTRODUCCION #################
#? Se nos ha solicitado desarrollar una aplicación para llevar registro de las 
#? entradas vendidas en el Parque de la Ciudad, para el concierto de Linkin Park. 
#? Para ello, se solicitará al usuario la siguiente información al momento de 
#? comprar cada entrada:
'''
NOMBRE = 'Facu' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberas programar el boton "Cargar Ventas" para poder cargar 10 ventas.
Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 18)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Vip)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General:           $9000
        * Campo delantero:   $180000
        * Vip:               $230000

Las entradas adquiridas con tarjeta de crédito tendrán un 10% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 20%. 


#!################ ACLARACION IMPORTANTE #################
Del punto B SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
B) INFORMES
    #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
    #! 1) - Cantidad de entradas vendidas para cada tipo.
    #! 2) - Promedio de edad de las personas que compraron ubicación VIP.
    #! 3) - Nombre de la persona de mayor edad que compró una entrada VIP.
    #! 4) - Porcentaje de entradas vendidas de tipo "General"
    #! 5) - Porcentaje de entradas vendidas de tipo "Campo delantero"
    #! 6) - Nombre de la/s persona/s de mayor edad, de género Femenino que compro una 
    #!       entrada VIP.
    #! 7) - Nombre de la/s persona/s de menor edad, de género Masculino que compro una 
    #!       entrada general.
    #! 8) - Tipo de entradas más vendidas.
    #! 9) - Tipo de entradas menos vendidas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Punto de Venta {NOMBRE} [From Zero World Tour]")
        self.minsize(320, 250)

        # self.audio_path = './linkin_park/linkin_park.ogg'
        # self.audio_manager = GameSound()
        # self.audio_manager.play_music(self.audio_path, volume = 0.4)
        
        self.label_title = customtkinter.CTkLabel(master=self, text=f"Punto de Venta {NOMBRE} [From Zero World Tour]", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./linkin_park/UTN_PuntoVenta_LP_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Ventas", command=self.btn_cargar_ventas_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_ventas_on_click(self):
        # Desarrollá la lógica debajo
        
        limite_entradas_a_vender = 4
        cantidad_compradores = 0
        suma_edades_vip = 0
        cantidad_personas_vip = 0
        
        nombre_masculino_general = None
        edad_masculino_general = None
        
        cantidad_entradas_general = 0
        
        total_recaudacion = 0
        
        while cantidad_compradores < limite_entradas_a_vender:
            
            """
            * Nombre del comprador
            * Edad (no menor a 18)
            * Género (Masculino, Femenino, Otro)
            * Tipo de entrada (General, Campo delantero, Vip)
            * Medio de pago (Crédito, Efectivo, Débito) 
            * Precio de la entrada (Se debe calcular)
            """
        
            # Validacion
            nombre = None
            while nombre == None or not nombre.isalpha():
                nombre = input(f'Ingrese el nombre del {cantidad_compradores + 1}° cliente: ')
            
            edad = 0
            while edad == 0 or not edad.isdigit() or (int(edad) < 18):
                edad = input(f'Ingrese la edad del {cantidad_compradores + 1}° cliente [Solo mayores de 18 años]: ')
            edad_int = int(edad)
            
            genero = None
            while genero == None or not genero.isalpha() or\
                (genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro'):
                genero = input(f'Ingrese el genero del {cantidad_compradores + 1}° cliente [Masculino,Femenino,Otro]: ').capitalize()
            
            tipo = None
            while tipo == None or not tipo.isalpha() or\
                (tipo != 'General' and tipo != 'Campo delantero' and tipo != 'Vip'):
                tipo = input(f'Ingrese el tipo de entrada elegido del {cantidad_compradores + 1}° cliente [General,Campo delantero,Vip]: ').capitalize()
            
            pago = None
            while pago == None or not pago.isalpha() or\
                (pago != 'Credito' and pago != 'Debito' and pago != 'Efectivo'):
                pago = input(f'Ingrese el medio de pago elegido del {cantidad_compradores + 1}° cliente [Credito,Debito,Efectivo]: ').capitalize()
            
            
            cantidad_compradores += 1
            
            # Procesar datos
            """
            * Lista de precios: 
            * General:           $90000
            * Campo delantero:   $180000
            * Vip:               $230000

            Las entradas adquiridas con tarjeta de crédito tendrán un 10% de descuento sobre el 
            precio de la entrada, mientras que las adquiridas con tarjeta de débito un 20%. 
            """
            
            match tipo:
                case 'General':
                    if pago == 'Efectivo':
                        entrada = 90000
                    elif pago == 'Credito':
                        entrada = 90000 * 0.9
                    else: # Debito
                        entrada = 90000 * 0.8
                    
                    if genero == 'Masculino' and (edad_masculino_general == None or edad_masculino_general > edad_int):
                        nombre_masculino_general = nombre
                        edad_masculino_general = edad_int
                    
                    cantidad_entradas_general += 1
                    
                case 'Campo delantero':
                    if pago == 'Efectivo':
                        entrada = 180000
                    elif pago == 'Credito':
                        entrada = 180000 * 0.9
                    else: # Debito
                        entrada = 180000 * 0.8
                case 'Vip':
                    if pago == 'Efectivo':
                        entrada = 230000
                    elif pago == 'Credito':
                        entrada = 230000 * 0.9
                    else: # Debito
                        entrada = 230000 * 0.8
                    
                    cantidad_personas_vip += 1
                    suma_edades_vip += edad_int
            
            #! 0) - Cantidad total de dinero recaudado por las ventas de entradas.
            total_recaudacion += entrada
            
            #! 2) - Promedio de edad de las personas que compraron ubicación VIP.
            
            #! 4) - Porcentaje de entradas vendidas de tipo "General"
            
            
            # 7) - Nombre de la/s persona/s de menor edad, de género Masculino que compro una 
            #!       entrada general.
            
            
        # Armar informes
        
        # Aca vas a armar tu variable con el texto del informe a entregar
        porcentaje_entradas_gral = (cantidad_entradas_general * 100 / cantidad_compradores)
        
        # cantidad_personas_vip == 0 -> Me dará un error
        promedio_edad_vip = suma_edades_vip / cantidad_personas_vip
        
        data_informe =\
            f"""
            0° - Cantidad total de dinero recaudado por las ventas de entradas $ {total_recaudacion}
            2° - El promedio de edad de las personas que compraron VIP es: {promedio_edad_vip} años.
            4° - Porcentaje de entradas vendidas de tipo "General": {porcentaje_entradas_gral}%
            7° - Nombre de la/s persona/s de menor edad, de género Masculino que compro una entrada general es: {nombre_masculino_general} | {edad_masculino_general}
            """
        alert('Informe', message=data_informe)

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
