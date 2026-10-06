import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):  # Clase padre abstracta
    def __init__(self, name: str):
        self.name = name

    @abstractmethod  # Método obligatorio para las clases hijas
    def turn_on(self) -> str:
        pass

    @abstractmethod  # Nuevo método polimórfico obligatorio
    def turn_off(self) -> str:
        pass


class SmartTV(SmartDevice):
    def __init__(self, name: str = "LG Smart TV"):
        super().__init__(name)

    def turn_on(self) -> str:
        return f"{self.name} is on and is playing the Harry Potter movie"

    def turn_off(self) -> str:
        return f"{self.name} is turned off"


class SmartSpeaker(SmartDevice):
    def __init__(self, name: str = "Echo Dot 5"):
        super().__init__(name)  # Usar la variable name recibida

    def turn_on(self) -> str:
        return f"{self.name} is playing Lofi music at volume 20%"

    def turn_off(self) -> str:
        return f"{self.name} is now turned off and music stopped"


class SmartWatch(SmartDevice):
    def __init__(self, name: str = "Huawei Fit"):
        super().__init__(name)  # Usar la variable name recibida

    def turn_on(self) -> str:
        return f"{self.name} is on and is tracking your heart rate"

    def turn_off(self) -> str:
        return f"{self.name} is turned off and entering sleep mode"


# Nuevo dispositivo para demostrar escalabilidad
class SmartLight(SmartDevice):
    def __init__(self, name: str = "Philips Hue"):
        super().__init__(name)

    def turn_on(self) -> str:
        return f"{self.name} is turned on with warm light at 100%"

    def turn_off(self) -> str:
        return f"{self.name} is turned off"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism GUI by Arantza Gutierrez Dominguez")
        self.geometry("480x520")
        self.resizable(False, False)

        # Ruta dinámica a tu archivo "work-from-home.png"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "work-from-home.png")

        if os.path.exists(icon_path):
            self.app_icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(True, self.app_icon)  # Aplica el icono a la ventana
        else:
            print("The icon file doesn't exist")

        # --- 2. OBJECT REGISTRY---
        self.items = {
            "TV": SmartTV("Living Room TV"),
            "Speaker": SmartSpeaker("Echo Dot 5"),
            "Watch": SmartWatch("Huawei Fit"),
            "Light": SmartLight("Living Room Light"),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="Smart Home Center",
            font=("Helvetica Neue", 14, "normal"),
            fg="#1d1d1f"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("Arial", 12, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Buttons
        btn_on = tk.Button(
            self,
            text="Turn On Device",
            command=self._handle_turn_on,
            bg="#2980b9",
            fg="white",
            font=("Helvetica Neue", 12, "normal"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_on.pack(pady=5)

        btn_off = tk.Button(
            self,
            text="Turn Off Device",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Helvetica Neue", 12, "normal"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_off.pack(pady=5)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click a button.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        # Activity Log Box
        lbl_log_title = tk.Label(
            self,
            text="Activity Log:",
            font=("Arial", 10, "bold"),
            fg="#1d1d1f"
        )
        lbl_log_title.pack(anchor="w", padx=20, pady=(10, 2))

        self.log_listbox = tk.Listbox(
            self,
            font=("Arial", 9),
            height=5
        )
        self.log_listbox.pack(fill="x", padx=20, pady=5)

    def _handle_turn_on(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]

        # POLYMORPHIC EXECUTION:
        result_message = active_object.turn_on()

        # Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self.log_listbox.insert(tk.END, result_message)

    def _handle_turn_off(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]

        # POLYMORPHIC EXECUTION:
        result_message = active_object.turn_off()

        # Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self.log_listbox.insert(tk.END, result_message)


# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()