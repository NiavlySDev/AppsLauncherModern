import tkinter as tk
from tkinter import filedialog, messagebox
import os
import win32com.client
from theme import *
from data import add_application
from icon_manager import icon_manager

class AddApplicationDialog(tk.Toplevel):
    def __init__(self, master, category_id, on_create):
        super().__init__(master)
        self.title("Nouvelle Application")
        self.geometry("500x320")
        self.configure(bg=DARK_BG)
        self.resizable(False, False)
        self.on_create = on_create
        self.category_id = category_id
        self.shortcut_path = None
        self.extracted_icon = None

        # Encadré central
        self.frame = tk.Frame(self, bg=ENTRY_BG)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=470, height=220)

        # Champ nom
        tk.Label(self.frame, text="Nom :", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=15)
        self.name_entry = tk.Entry(self.frame, font=("Arial", 11))
        self.name_entry.place(x=140, y=15, width=200)

        # Sélection de raccourci
        tk.Label(self.frame, text="Raccourci :", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=55)
        self.shortcut_btn = tk.Button(self.frame, text="Choisir un raccourci", bg=BUTTON_BLUE, fg="white", 
                                     font=("Arial", 10), command=self.select_shortcut)
        self.shortcut_btn.place(x=140, y=55, width=150, height=25)
        
        # Affichage du chemin sélectionné
        self.path_label = tk.Label(self.frame, text="Aucun raccourci sélectionné", bg=ENTRY_BG, fg="#666", 
                                  font=("Arial", 9), anchor="w")
        self.path_label.place(x=15, y=90, width=440, height=20)

        # Aperçu de l'icône
        tk.Label(self.frame, text="Aperçu icône :", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 11)).place(x=15, y=120)
        self.icon_preview = tk.Label(self.frame, text="[Aucune icône]", bg="white", relief="sunken", 
                                   width=8, height=4)
        self.icon_preview.place(x=140, y=120)

        # Champ icône texte (optionnel)
        tk.Label(self.frame, text="Icône texte\n(optionnel) :", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 10)).place(x=15, y=165)
        self.icon_entry = tk.Entry(self.frame, font=("Arial", 11))
        self.icon_entry.place(x=140, y=175, width=200)

        # Boutons
        self.create_btn = tk.Button(self, text="Créer", bg=BUTTON_GREEN, fg="white", font=("Arial", 12, "bold"), command=self.create_application)
        self.create_btn.place(relx=0.25, rely=0.92, anchor="center", width=120, height=32)
        self.cancel_btn = tk.Button(self, text="Annuler", bg=BUTTON_RED, fg="white", font=("Arial", 12, "bold"), command=self.destroy)
        self.cancel_btn.place(relx=0.75, rely=0.92, anchor="center", width=120, height=32)

    def select_shortcut(self):
        """Sélectionne un raccourci et extrait son icône"""
        filetypes = (
            ('Raccourcis Windows', '*.lnk'),
            ('Exécutables', '*.exe'),
            ('Tous les fichiers', '*.*')
        )
        
        filename = filedialog.askopenfilename(
            title="Sélectionner un raccourci ou une application",
            filetypes=filetypes,
            initialdir=os.path.join(os.path.expanduser("~"), "Desktop")
        )
        
        if filename:
            self.shortcut_path = filename
            # Afficher le nom du fichier
            display_name = os.path.basename(filename)
            if len(display_name) > 50:
                display_name = display_name[:47] + "..."
            self.path_label.config(text=display_name, fg="#333")
            
            # Auto-remplir le nom si vide
            if not self.name_entry.get():
                name = os.path.splitext(os.path.basename(filename))[0]
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, name)
            
            # Extraire et afficher l'icône
            self.extract_and_show_icon(filename)

    def extract_and_show_icon(self, file_path):
        """Extrait l'icône d'un fichier et l'affiche"""
        try:
            # Utiliser le gestionnaire d'icônes pour obtenir une icône de haute qualité
            app_name = os.path.splitext(os.path.basename(file_path))[0]
            
            # Créer un widget d'icône temporaire pour l'aperçu
            temp_frame = tk.Frame(self.frame)
            icon_widget = icon_manager.get_icon_widget(temp_frame, app_name, file_path)
            
            if hasattr(icon_widget, 'image') and icon_widget.image:
                # Si on a une vraie image, l'afficher
                self.extracted_icon = icon_widget.image
                self.icon_preview.config(image=self.extracted_icon, text="")
                print(f"Icône haute qualité obtenue pour {app_name}")
            else:
                # Sinon, afficher un placeholder
                self.icon_preview.config(image="", text="[Icône générée]")
                
        except Exception as e:
            print(f"Erreur lors de l'extraction de l'icône: {e}")
            self.icon_preview.config(image="", text="[Erreur icône]")

    def create_application(self):
        name = self.name_entry.get().strip()
        icon = self.icon_entry.get().strip()
        
        if not name:
            messagebox.showerror("Erreur", "Le nom de l'application est requis.")
            return
            
        if not self.shortcut_path:
            messagebox.showerror("Erreur", "Vous devez sélectionner un raccourci.")
            return
        
        if name:
            add_application(name, icon, self.category_id, self.shortcut_path)
            self.on_create()
            self.destroy()