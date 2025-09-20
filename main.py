import tkinter as tk
from theme import set_dark_theme
from ui.main_view import MainView
from data import get_categories, get_applications, load_data

def main():
    # Charger les données sauvegardées
    load_data()
    
    root = tk.Tk()
    root.title("Lanceur d'applications")
    root.geometry("900x600")
    set_dark_theme(root)
    app = MainView(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()