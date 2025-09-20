import tkinter as tk
from theme import *
from data import add_category

class AddCategoryDialog(tk.Toplevel):
    def __init__(self, master, on_create):
        super().__init__(master)
        self.title("Nouvelle Catégorie")
        self.geometry("400x270")
        self.configure(bg=DARK_BG)
        self.resizable(False, False)
        self.on_create = on_create

        # Encadré central
        self.frame = tk.Frame(self, bg=ENTRY_BG)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=370, height=180)

        # Champ nom
        tk.Label(self.frame, text="Nom :", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=10)
        self.name_entry = tk.Entry(self.frame, font=("Arial", 11))
        self.name_entry.place(x=140, y=10, width=200)

        # Champ icône
        tk.Label(self.frame, text="Icône (texte):", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=50)
        self.icon_entry = tk.Entry(self.frame, font=("Arial", 11))
        self.icon_entry.place(x=140, y=50, width=200)

        # Champ couleur (simple, à améliorer)
        tk.Label(self.frame, text="Couleur (hex):", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=90)
        self.color_entry = tk.Entry(self.frame, font=("Arial", 11))
        self.color_entry.insert(0, CATEGORY_LABEL)
        self.color_entry.place(x=140, y=90, width=200)

        # Boutons
        self.create_btn = tk.Button(self, text="Créer", bg=BUTTON_GREEN, fg="white", font=("Arial", 12, "bold"), command=self.create_category)
        self.create_btn.place(relx=0.25, rely=0.92, anchor="center", width=120, height=32)
        self.cancel_btn = tk.Button(self, text="Annuler", bg=BUTTON_RED, fg="white", font=("Arial", 12, "bold"), command=self.destroy)
        self.cancel_btn.place(relx=0.75, rely=0.92, anchor="center", width=120, height=32)

    def create_category(self):
        name = self.name_entry.get().strip()
        icon = self.icon_entry.get().strip()
        color = self.color_entry.get().strip() or CATEGORY_LABEL
        if name:
            add_category(name, icon, color)
            self.on_create()
            self.destroy()