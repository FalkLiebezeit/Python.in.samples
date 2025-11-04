import tkinter as tk
from tkinter import Label, Text, Button, RAISED, messagebox
from datetime import datetime
from PIL import ImageTk, Image
import requests
import os

class Weather:
    def __init__(self):
        # --- Initialize main window ---
        self.root = tk.Tk()
        self.root.geometry('800x300')
        self.root.title("Weather Application")
        self.root.maxsize(800, 300)
        self.root.minsize(800, 300)

        self.font = ('verdana', 10, 'bold')

        # --- Header section ---
        self.header = Label(self.root, width=100, height=2, bg="#00274c")
        self.header.place(x=0, y=0)
        self.date = Label(self.root, text=datetime.now().date(), bg="#00274c", fg="white", font=self.font)
        self.date.place(x=400, y=5)
        self.heading = Label(self.root, text="Weather Report", bg="#00274c", fg="white", font=self.font)
        self.heading.place(x=180, y=5)
        self.location = Label(self.root, text="Please enter location", bg="#00274c", fg="white", font=self.font)
        self.location.place(x=10, y=5)

        # --- Path for icons (relative to script location) ---
        file_path = os.path.join(os.path.dirname(__file__), 'icon_files')  # Use a subfolder for icons

        # --- Weather icon ---
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(file_path, 'icon.png')))
        self.image = Label(self.root, image=self.img)
        self.image.place(x=20, y=40)

        # --- Input section ---
        self.name = Label(self.root, text="City or Country Name", fg="#00274c", font=self.font)
        self.name.place(x=140, y=45)
        self.loc = Text(self.root, width=25, height=2)
        self.loc.place(x=140, y=70)
        self.button = Button(self.root, text="Search", bg="#00274c", fg="white", font=self.font,
                             relief=RAISED, borderwidth=3, command=self.weather_report)
        self.button.place(x=350, y=73)

        # --- Divider lines and report label ---
        self.line1 = Label(self.root, bg="#00274c", width=20, height=0)
        self.line1.place(x=0, y=150)
        self.line2 = Label(self.root, bg="#00274c", width=20, height=0)
        self.line2.place(x=360, y=150)
        self.report = Label(self.root, text="Weather Report", bg="#00274c", fg="white", font=self.font, padx=10)
        self.report.place(x=180, y=150)

        # --- Weather details section with icons and labels ---
        self.img2 = ImageTk.PhotoImage(Image.open(os.path.join(file_path, 'icon2.png')))
        self.image2 = Label(self.root, image=self.img2)
        self.image2.place(x=90, y=180)
        self.weather = Label(self.root, text="", fg="#00274c", font=self.font)
        self.weather.place(x=90, y=230)

        self.img3 = ImageTk.PhotoImage(Image.open(os.path.join(file_path, 'icon3.png')))
        self.image3 = Label(self.root, image=self.img3)
        self.image3.place(x=200, y=180)
        self.temperature = Label(self.root, text="", fg="#00274c", font=self.font)
        self.temperature.place(x=200, y=230)

        self.img4 = ImageTk.PhotoImage(Image.open(os.path.join(file_path, 'icon4.png')))
        self.image4 = Label(self.root, image=self.img4)
        self.image4.place(x=310, y=180)
        self.humidity = Label(self.root, text="", fg="#00274c", font=self.font)
        self.humidity.place(x=310, y=230)

        self.img5 = ImageTk.PhotoImage(Image.open(os.path.join(file_path, 'icon5.png')))
        self.image5 = Label(self.root, image=self.img5)
        self.image5.place(x=380, y=180)
        self.pressure = Label(self.root, text="", fg="#00274c", font=self.font)
        self.pressure.place(x=380, y=230)

        self.root.mainloop()

    def weather_report(self):

        """
        Fetch weather data from OpenWeatherMap API and update the UI.
        """
        
        api_key = "ceb9f975f5dbce2fb1e44e604ec50fbb"
        base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        cityname = self.loc.get(1.0, 'end').strip()

        if not cityname:
            messagebox.showwarning('Input Error', 'Please enter a city or country name.')
            return

        # Build the request URL
        url = f"{base_url}{cityname}&appid={api_key}"

        try:
            data = requests.get(url).json()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to fetch data: {e}')
            return

        if data.get('cod') == '404':
            messagebox.showerror('Error', 'City Not Found!')
            return

        # --- Update UI with weather data ---
        try:
            self.location['text'] = f"{data['name']}, {data['sys']['country']}"

            c = int(data['main']['temp_max'] - 273.15)
            f = c * 9 / 5 + 32

            self.weather['text'] = data['weather'][0]['main']
            self.weather['font'] = ('verdana', 20, 'bold')
            self.temperature['text'] = f'{c}°C \n {f:.1f}°F'
            self.temperature['font'] = ('verdana', 15, 'bold')
            self.humidity['text'] = data['main']['humidity']
            self.humidity['font'] = ('verdana', 15, 'bold')
            self.pressure['text'] = data['main']['pressure']
            self.pressure['font'] = ('verdana', 15, 'bold')
        except Exception as e:
            messagebox.showerror('Error', f'Unexpected data format: {e}')

if __name__ == '__main__':
    Weather()