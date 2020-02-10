import tkinter as tk
import SetWeather

HEIGHT = 800
WIDTH = 800

root = tk.Tk() 

root.wm_title("Weather_App")   

# Display the weather report when the button is pressed...
def button_press():
    weather_report['text'] = SetWeather.get_weather(entry.get())
#...

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

# Background image on the canvas...
background_image = tk.PhotoImage(file = 'landscape.png')
background_lable = tk.Label(root, image = background_image)
background_lable.place(relwidth = 1, relheight = 1)
#...

upper_frame = tk.Frame(root, bg = "#80c1ff", bd = 7)
upper_frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = "n")

# Entry to give the city to check the weather...
entry = tk.Entry(upper_frame, font = 40)
entry.place(relwidth = 1, relheight = 1)
#...

Get_Weather = tk.Button(upper_frame, text = "Get Weather", font = 40, command = lambda: button_press())
Get_Weather.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lower_frame  = tk.Frame(root, bg = "#80c1ff", bd = 7)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

# Label to display the weather report of that city...
weather_report = tk.Label(lower_frame, bg = "white", font = 100)
weather_report.place(relheight = 1, relwidth = 1)
#...

root.mainloop()