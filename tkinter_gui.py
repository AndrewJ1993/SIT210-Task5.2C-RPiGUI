import tkinter
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


# Gui definitions
win = tkinter.Tk()
v = tkinter.IntVar()
win.title("Led toggle")


# Event functions
def led_toggle_red():
    led_toggle_off()
    GPIO.output(5, GPIO.HIGH)

def led_toggle_blue():
    led_toggle_off()
    GPIO.output(13, GPIO.HIGH)

def led_toggle_green():
    led_toggle_off()
    GPIO.output(26, GPIO.HIGH)

def led_toggle_off():
    GPIO.output(13, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)

def close_window():
    led_toggle_off()
    win.destroy()


# Widgets
tkinter.Radiobutton(win, text = "red", command = led_toggle_red, variable=v, value=1).grid(row=0, column=1)
tkinter.Radiobutton(win, text = "blue", command = led_toggle_blue, variable=v, value=2).grid(row=1, column=1)
tkinter.Radiobutton(win, text = "green", command = led_toggle_green, variable=v, value=3).grid(row=2, column=1)
led_button = tkinter.Button(win, text = "Exit",  command = close_window, height = 1, width = 24).grid(row=3, column=1)

win.mainloop()
