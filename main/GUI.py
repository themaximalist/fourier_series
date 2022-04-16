import PySimpleGUI as sg
from fourier_s import *

layout = [[sg.Text("Enter your Function")],
          [sg.Input()],
          [sg.Text("Enter The N:")],
          [sg.Input()],
          [sg.Text("Enter The Lower Bound:")],
          [sg.Input()],
          [sg.Text("Enter The Upper Bound:")],
          [sg.Input()],
          [sg.Text("Use \"pi\" for using PI number")],
          [sg.Text()],
          [sg.Text("Presented By Omid Shahbazi")],
          [sg.Button('Ok')]]

window = sg.Window('Fourier Series', layout)

event, values = window.read()

f = function(str(values[0]))
f_s = fourier(f, values[2], values[3], int(values[1]))
ploting(f, f_s, values[2], values[3])

window.close()

