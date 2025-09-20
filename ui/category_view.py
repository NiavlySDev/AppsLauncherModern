import tkinter as tk
from tkinter import messagebox
import os
from theme import *
from data import get_categories, get_applications, launch_application
from ui.add_application_dialog import AddApplicationDialog
from icon_manager import icon_manager

class CategoryView(tk.Frame):
    def __init__(self, master, cat_id, go_back, open_add_category):
        super().__init__(master, bg=DARK_BG)
        self.cat_id = cat_id
        self.go_back = go_back
        self.open_add_category = open_add_category
        self.create_widgets()

    def create_widgets(self):
        from data import categories
        cat_name = categories[self.cat_id]["name"]

        self.header = tk.Label(self, text=cat_name, font=("Arial", 22, "bold"), bg=HEADER_BG, fg=HEADER_FG)
        self.header.pack(pady=30)

        self.cards_frame = tk.Frame(self, bg=DARK_BG)
        self.cards_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.refresh_content()

        btns = tk.Frame(self, bg=DARK_BG)
        btns.pack(pady=20)
        add_cat_btn = tk.Button(btns, text="Nouvelle Catégorie", bg=BUTTON_GREEN, fg="white", font=("Arial", 13, "bold"), relief="flat", command=lambda: self.open_add_category(self.cat_id))
        add_cat_btn.pack(side="left", padx=20, ipadx=20, ipady=8)
        add_app_btn = tk.Button(btns, text="Nouvelle Appli", bg=BUTTON_BLUE, fg="white", font=("Arial", 13, "bold"), relief="flat", command=self.open_add_app)
        add_app_btn.pack(side="left", padx=20, ipadx=20, ipady=8)

        back_btn = tk.Button(self, text="← Retour", bg=HEADER_BG, fg="white", font=("Arial", 11, "bold"), relief="flat", command=self.go_back)
        back_btn.place(x=10, y=10, width=80, height=28)

    def refresh_content(self):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        subcats = get_categories(parent=self.cat_id)
        apps = get_applications(category=self.cat_id)
        idx = 0
        for subcat_id, subcat in subcats.items():
            card = tk.Frame(self.cards_frame, bg=CARD_BG, width=150, height=120)
            card.grid(row=idx//4, column=idx%4, padx=18, pady=16)
            cat_label = tk.Label(card, text="Sous Catégorie", bg=CATEGORY_LABEL, fg="white", font=("Arial", 11, "bold"), anchor="w")
            cat_label.place(x=0, y=0, width=95, height=28)
            corner = tk.Label(card, bg=CATEGORY_LABEL_2)
            corner.place(x=95, y=0, width=55, height=28)
            icon = tk.Label(card, text=subcat["icon"] or "[Icône]", bg=CARD_BG, fg="#333", font=("Arial", 10))
            icon.place(relx=0.5, rely=0.55, anchor="center")
            for widget in (card, cat_label, corner, icon):
                widget.bind("<Button-1>", lambda e, c=subcat_id: self.master.show_category(c))
            idx += 1
        for app_id, app in apps.items():
            card = tk.Frame(self.cards_frame, bg=CARD_BG, width=150, height=120)
            card.grid(row=idx//4, column=idx%4, padx=18, pady=16)
            cat_label = tk.Label(card, text="Application", bg=CATEGORY_LABEL, fg="white", font=("Arial", 11, "bold"), anchor="w")
            cat_label.place(x=0, y=0, width=95, height=28)
            corner = tk.Label(card, bg=CATEGORY_LABEL_2)
            corner.place(x=95, y=0, width=55, height=28)
            
            # Essayer d'afficher l'icône réelle si disponible
            icon_widget = self.create_app_icon(card, app)
            
            # Nom de l'application
            name_label = tk.Label(card, text=app["name"], bg=CARD_BG, fg="white", font=("Arial", 9, "bold"))
            name_label.place(relx=0.5, rely=0.85, anchor="center")
            
            # Bind du clic pour lancer l'application
            for widget in (card, cat_label, corner, icon_widget, name_label):
                widget.bind("<Button-1>", lambda e, aid=app_id: self.launch_app(aid))
            idx += 1

    def create_app_icon(self, parent, app):
        """Crée et retourne le widget d'icône pour une application"""
        try:
            # Utiliser le gestionnaire d'icônes pour obtenir une icône de haute qualité
            icon_widget = icon_manager.get_icon_widget(parent, app["name"], app.get("shortcut_path"))
            icon_widget.place(relx=0.5, rely=0.55, anchor="center")
            return icon_widget
            
        except Exception as e:
            print(f"Erreur lors de la création de l'icône: {e}")
            # Fallback sur l'icône texte
            icon_text = app["icon"] or "[App]"
            icon_widget = tk.Label(parent, text=icon_text, bg=CARD_BG, fg="#333", font=("Arial", 10))
            icon_widget.place(relx=0.5, rely=0.55, anchor="center")
            return icon_widget

    def launch_app(self, app_id):
        """Lance une application"""
        if launch_application(app_id):
            print(f"Application {app_id} lancée avec succès")
        else:
            messagebox.showerror("Erreur", "Impossible de lancer l'application.")

    def open_add_app(self):
        def on_create():
            self.refresh_content()
        AddApplicationDialog(self, self.cat_id, on_create)