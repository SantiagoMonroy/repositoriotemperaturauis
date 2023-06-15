import requests
import tkinter as tk
from tkinter import messagebox

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def obtener_clima(self, ciudad):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={self.api_key}&lang=es'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data['main']['temp']
            descripcion_clima = data['weather'][0]['description']
            velocidad_viento = data['wind']['speed']
            latitud = data['coord']['lat']
            longitud = data['coord']['lon']
            temperatura_celsius = temperatura - 273.15
            return {
                '☁    Temperatura': f'{temperatura_celsius:.2f} °C',
                '☂    Descripción del clima': descripcion_clima,
                '❄    Velocidad del viento': f'{velocidad_viento} m/s',
                '☈    Latitud': latitud,
                '⇱    Longitud': longitud
            }
        else:
            return None

def obtener_info_clima():
    ciudad = ciudad_entry.get()
    pronostico = api.obtener_clima(ciudad)
    if pronostico is not None:
        weather_info.delete(1.0, tk.END)
        for key, value in pronostico.items():
            weather_info.insert(tk.END, f'{key}: {value}\n')
    else:
        messagebox.showerror('Error', 'Hay un error con la ciudad que ingresaste.')

def cerrar_ventana():
    if messagebox.askokcancel('Salir', '¿Estás seguro de que quieres salir?'):
        window.destroy()

API_KEY = 'e622ac46041338d0859ca1a4da9de8f1'
api = WeatherAPI(API_KEY)

window = tk.Tk()
window.title('𝓟𝓻𝓸𝓷𝓸𝓼𝓽𝓲𝓬𝓸 𝓭𝓮𝓵 𝓽𝓲𝓮𝓶𝓹𝓸')
window.protocol('WM_DELETE_WINDOW', cerrar_ventana)

ciudad_label = tk.Label(window, text='Ingrese la ciudad a consultar:')
ciudad_label.pack()

ciudad_entry = tk.Entry(window)
ciudad_entry.pack()

obtener_info_button = tk.Button(window, text='Obtener Pronóstico', command=obtener_info_clima)
obtener_info_button.pack()

weather_info = tk.Text(window, height=10, width=50)
weather_info.pack()

window.mainloop()
