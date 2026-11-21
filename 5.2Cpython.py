
import tkinter as tk
from gpiozero import PWMOutputDevice

# GPIO18 - Physical Pin 12
led = PWMOutputDevice(18, frequency=1000)

led_on = True

# Colours
BG = "#0f172a"
CARD = "#1e293b"
ACCENT = "#8b5cf6"
TEXT = "#f8fafc"
GREEN = "#22c55e"
RED = "#ef4444"


def change_brightness(value):
    brightness = int(float(value))
    brightness_label.config(text=f"{brightness}%")

    if led_on:
        led.value = brightness / 100


def turn_on():
    global led_on
    led_on = True
    led.value = brightness_slider.get() / 100
    status_label.config(
        text="● LED IS ON",
        fg=GREEN
    )


def turn_off():
    global led_on
    led_on = False
    led.off()
    status_label.config(
        text="● LED IS OFF",
        fg=RED
    )


def close_app():
    led.off()
    led.close()
    root.destroy()


# Main window
root = tk.Tk()
root.title("Smart LED Controller")
root.geometry("480x480")
root.configure(bg=BG)
root.resizable(False, False)

root.protocol("WM_DELETE_WINDOW", close_app)


# Header
tk.Label(
    root,
    text="SMART LED",
    font=("Arial", 25, "bold"),
    fg=ACCENT,
    bg=BG
).pack(pady=(25, 5))

tk.Label(
    root,
    text="RASPBERRY PI 4  |  GPIO 18",
    font=("Arial", 10, "bold"),
    fg="#94a3b8",
    bg=BG
).pack(pady=(0, 20))


# Main card
card = tk.Frame(
    root,
    bg=CARD,
    padx=25,
    pady=20
)
card.pack(padx=30, fill="both")


# Brightness heading
tk.Label(
    card,
    text="BRIGHTNESS LEVEL",
    font=("Arial", 11, "bold"),
    fg="#cbd5e1",
    bg=CARD
).pack(pady=(5, 10))


# Percentage
brightness_label = tk.Label(
    card,
    text="50%",
    font=("Arial", 42, "bold"),
    fg="#a78bfa",
    bg=CARD
)
brightness_label.pack(pady=5)


# Slider
brightness_slider = tk.Scale(
    card,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=350,
    command=change_brightness,
    bg=CARD,
    fg=TEXT,
    troughcolor=ACCENT,
    activebackground="#c4b5fd",
    highlightthickness=0,
    bd=0,
    sliderrelief="flat",
    font=("Arial", 10),
    showvalue=False
)

brightness_slider.set(50)
brightness_slider.pack(pady=15)


tk.Label(
    card,
    text="Adjust the slider to control LED intensity",
    font=("Arial", 9),
    fg="#94a3b8",
    bg=CARD
).pack(pady=(0, 15))


# Buttons
button_frame = tk.Frame(card, bg=CARD)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="TURN ON",
    command=turn_on,
    bg=GREEN,
    fg="#052e16",
    activebackground="#16a34a",
    font=("Arial", 11, "bold"),
    width=13,
    height=2,
    relief="flat",
    cursor="hand2"
).pack(side=tk.LEFT, padx=8)


tk.Button(
    button_frame,
    text="TURN OFF",
    command=turn_off,
    bg=RED,
    fg="white",
    activebackground="#b91c1c",
    font=("Arial", 11, "bold"),
    width=13,
    height=2,
    relief="flat",
    cursor="hand2"
).pack(side=tk.LEFT, padx=8)


# Status
status_label = tk.Label(
    root,
    text="● LED IS ON",
    font=("Arial", 14, "bold"),
    fg=GREEN,
    bg=BG
)
status_label.pack(pady=22)


# Footer
tk.Label(
    root,
    text="SMART LED CONTROL SYSTEM",
    font=("Arial", 8, "bold"),
    fg="#64748b",
    bg=BG
).pack(side=tk.BOTTOM, pady=12)


root.mainloop()
