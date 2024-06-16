import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display weather information
def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        city_label.config(text=weather['name'])
        temp_label.config(text=f"Temperature: {weather['main']['temp']}°C")
        desc_label.config(text=f"Condition: {weather['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "City not found")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("300x200")

# Create and place the widgets
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=show_weather)
search_button.pack(pady=5)

city_label = tk.Label(root, text="", font=("Helvetica", 16))
city_label.pack(pady=5)

temp_label = tk.Label(root, text="", font=("Helvetica", 14))
temp_label.pack(pady=5)

desc_label = tk.Label(root, text="", font=("Helvetica", 12))
desc_label.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()
