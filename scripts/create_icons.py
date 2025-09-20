from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon():
    """Créer l'icône de l'application"""
    
    # Créer une icône moderne 256x256
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fond dégradé moderne
    for y in range(size):
        # Dégradé du bleu au violet
        ratio = y / size
        r = int(100 + (150 * ratio))  # 100->250
        g = int(150 + (50 * ratio))   # 150->200  
        b = int(255 - (50 * ratio))   # 255->205
        
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    # Cercle central
    center = size // 2
    circle_radius = size // 3
    draw.ellipse([
        center - circle_radius, center - circle_radius,
        center + circle_radius, center + circle_radius
    ], fill=(255, 255, 255, 220), outline=(255, 255, 255, 255), width=8)
    
    # Icône fusée stylisée
    rocket_color = (50, 50, 50, 255)
    
    # Corps de la fusée
    draw.ellipse([
        center - 30, center - 50,
        center + 30, center + 50
    ], fill=rocket_color)
    
    # Pointe de la fusée
    draw.polygon([
        (center, center - 70),
        (center - 20, center - 50),
        (center + 20, center - 50)
    ], fill=rocket_color)
    
    # Flammes
    flame_colors = [(255, 100, 0, 200), (255, 200, 0, 150)]
    for i, color in enumerate(flame_colors):
        offset = i * 10
        draw.polygon([
            (center - 15 + offset, center + 50),
            (center + 15 - offset, center + 50),
            (center, center + 80 - offset)
        ], fill=color)
    
    # Sauvegarder en différentes tailles
    sizes = [16, 24, 32, 48, 64, 128, 256]
    
    for s in sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(f'assets/icon_{s}.png')
        
        # Sauvegarder aussi en ICO pour Windows
        if s in [16, 24, 32, 48]:
            resized.save(f'assets/icon_{s}.ico')
    
    # Icône principale
    img.save('assets/app_icon.png')
    
    # ICO multi-résolution pour Windows
    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icons = []
    
    for size_tuple in icon_sizes:
        resized = img.resize(size_tuple, Image.Resampling.LANCZOS)
        icons.append(resized)
    
    # Sauvegarder ICO multi-résolution
    icons[0].save('assets/app_icon.ico', format='ICO', sizes=icon_sizes, append_images=icons[1:])
    
    print("✅ Icônes créées avec succès dans assets/")

if __name__ == "__main__":
    create_app_icon()
