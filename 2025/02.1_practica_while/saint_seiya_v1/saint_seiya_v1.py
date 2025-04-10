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
#? El presentador del torneo de artes marciales quiere que desarrolles un modelo prototipico 
#? de scouter (un detector basicamente) para ver ciertas metricas de los participantes.
#? de cualquier parte del universo, es por eso que deberas realizar la carga 
#? de 10 participantes.
'''
NOMBRE = '' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
A) Para ello deberas programar el boton "Cargar Guerreros" para poder cargar 10 Caballeros del zodiaco.
Los datos que deberas pedir para los Caballeros del zodiaco son:
    * El nombre del Caballeros del zodiaco.
    * El tipo de armadura (Bronce, Plata, Oro, Divina, Oscura).
    * La cantidad de cosmos del guerrero (entre 25000 y 150000).
    
#!################ ACLARACION IMPORTANTE #################
Del punto B SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido. En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
B) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de guerreros de armadura de Oro.
    #! 1) - Cantidad de guerreros de armadura Divina.
    #! 2) - Nombre, Armadura y Cosmos del guerrero mas fuerte.
    #! 3) - Nombre, Raza y Poder del guerrero mas debil.
    #! 4) - Cantidad de guerreros con mas de 85000 de poder y armadura de Plata.
    #! 5) - Cantidad de guerreros con menos de 50000 de poder y armadura de Bronce.
    #! 6) - Armadura que mas guerreros posea inscriptos.
    #! 7) - Armadura que menos guerreros posea inscriptos.
    #! 8) - el promedio de cosmos de todos los guerreros con armadura Oscura.
    #! 9) - el porcentaje, tipo de armadura y promedio de cosmos de guerreros 
    #!      de cada tipo de armadura, respecto al total de guerreros.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Saint Seiya {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"{NOMBRE} de la constelacion Uteneana", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.audio_path = './saint_seiya_v1/seiya.ogg'
        self.audio_manager = GameSound()
        self.audio_manager.play_music(self.audio_path, volume=0.4)
        
        self.image = tk.PhotoImage(file='./saint_seiya_v1/UTN_SaintSeiya_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Caballeros del Zodíaco", command=self.btn_cargar_participantes_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_cargar_participantes_on_click(self):
        # Desarrollá la lógica debajo
        
        
        
        
        # Aca vas a armar tu variable con el texto del informe a entregar
        data_informe = 'CAMBIAR ESTE TEXTO POR TU INFORME'
        alert('Informe', message=data_informe)

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
