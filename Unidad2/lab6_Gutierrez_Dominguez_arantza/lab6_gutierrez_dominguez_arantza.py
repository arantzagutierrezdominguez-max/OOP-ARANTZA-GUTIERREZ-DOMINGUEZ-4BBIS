import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class SmartDevice(ABC):  # Clase padre abstracta
    def __init__(self, name: str):
        self.name = name

    @abstractmethod  # Método obligatorio para las clases hijas
    def turn_on(self) -> str:
        pass


class SmartTV(SmartDevice):
    def __init__(self, name: str = "LG Smart TV"):  # Valor por defecto opcional
        super().__init__(name)

    def turn_on(self) -> str:
        return f"{self.name} is on and is playing the Harry Potter movie"


class SmartSpeaker(SmartDevice):
    def __init__(self, name: str = "Echo Dot 5"):
        super().__init__("Echo Dot 5")

    def turn_on(self) -> str:
        return f"{self.name} is playing Lofi music at volume 20%"


class SmartWatch(SmartDevice):
    def __init__(self, name: str = "Huawei Fit"):
        super().__init__("Huawei Fit")

    def turn_on(self) -> str:
        return f"{self.name} is on and is tracking your heart rate"


class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism GUI by Arantza Gutierrez Dominguez")
        self.geometry("480x360")
        self.resizable(False, False)

        curret_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "app_icon.png")

        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file="icon_dir")
            self.icon_photo = (True, self.app_icon)
        else:
            print("the icon file doesn't exists")

        # --- 2. OBJECT REGISTRY---
        # Se instancian pasando el argumento 'name'
        self.items = {
            "TV": SmartTV("Living Room TV"),
            "Speaker": SmartSpeaker("Echo Dot 5"),
            "Watch": SmartWatch("Huawei Fit"),
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

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn On Device",
            command=self._handle_action,
            bg="#2980b9",
            fg="white",
            font=("Helvetica Neue", 12, "normal"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_action.pack(pady=15)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'Turn On Device'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # Se ejecuta el método correcto definido en la interfaz abstracta (turn_on)
        result_message = active_object.turn_on()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))


# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()-