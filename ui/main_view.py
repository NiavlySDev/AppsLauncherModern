import tkinter as tk
from theme import *
from data import get_categories
from ui.add_category_dialog import AddCategoryDialog
from ui.category_view import CategoryView

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=DARK_BG)
        self.master = master
        self.create_widgets()
        self.refresh_categories()

    def create_widgets(self):
        self.header = tk.Label(self, text="Applications", font=("Arial", 22, "bold"), bg=HEADER_BG, fg=HEADER_FG)
        self.header.pack(pady=30)
        self.cards_frame = tk.Frame(self, bg=DARK_BG)
        self.cards_frame.pack(padx=20, pady=10, fill="both", expand=True)
        self.add_cat_btn = tk.Button(self, text="Nouvelle Catégorie", bg=BUTTON_GREEN, fg="white", font=("Arial", 13, "bold"), relief="flat", command=self.open_add_category)
        self.add_cat_btn.pack(pady=20, ipadx=20, ipady=8)

    def refresh_categories(self):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        cats = get_categories()
        if not cats:
            return
        for idx, (cat_id, cat) in enumerate(cats.items()):
            card = tk.Frame(self.cards_frame, bg=CARD_BG, width=150, height=120)
            card.grid(row=idx//4, column=idx%4, padx=18, pady=16)
            card.bind("<Button-1>", lambda e, c=cat_id: self.show_category(c))
            cat_label = tk.Label(card, text=cat["name"], bg=cat.get("color", CATEGORY_LABEL), fg="white", font=("Arial", 12, "bold"), anchor="w")
            cat_label.place(x=0, y=0, width=95, height=28)
            corner = tk.Label(card, bg=CATEGORY_LABEL_2)
            corner.place(x=95, y=0, width=55, height=28)
            icon = tk.Label(card, text=cat["icon"] or "[Icône]", bg=CARD_BG, fg="#333", font=("Arial", 10))
            icon.place(relx=0.5, rely=0.55, anchor="center")
            for widget in (card, cat_label, corner, icon):
                widget.bind("<Button-1>", lambda e, c=cat_id: self.show_category(c))

    def open_add_category(self, parent=None):
        def on_create():
            self.refresh_categories()
        AddCategoryDialog(self, on_create)

    def show_category(self, cat_id):
        for widget in self.master.winfo_children():
            widget.destroy()
        cat_view = CategoryView(self.master, cat_id, go_back=self.go_back, open_add_category=self.open_add_category)
        cat_view.pack(fill="both", expand=True)

    def go_back(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        new_main = MainView(self.master)
        new_main.pack(fill="both", expand=True)