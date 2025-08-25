import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QFontDatabase, QFont
from PyQt5.QtCore import Qt

class RetroPokemonCard(QWidget):
    def __init__(self, pokemon_data):
        super().__init__()

        # === Load Pixel Font ===
        font_id = QFontDatabase.addApplicationFont("../Data/PressStart2P-Regular.ttf")
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.pixel_font = QFont(family, 10)  # Pixel size

        # === Window Style ===
        self.setWindowTitle("Retro Pokémon Card")
        self.setStyleSheet("background-color: #FFDE59;")  # Retro Yellow BG

        # === Layout ===
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # === Pokémon Name ===
        name_label = QLabel(pokemon_data['name'].upper())
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setFont(self.pixel_font)
        name_label.setStyleSheet("""
            QLabel {
                color: black;
                background-color: #FF3B3F;
                border: 4px solid #FFD93D;
                padding: 6px;
            }
        """)
        layout.addWidget(name_label)

        # === Pokémon Sprite ===
        img_url = pokemon_data['sprites']['front_default']
        img_data = requests.get(img_url).content
        image = QImage.fromData(img_data)
        pixmap = QPixmap.fromImage(image)

        # Keep pixel art sharp
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)

        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        image_label.setStyleSheet("""
            QLabel {
                background-color: #FF3B3F;
                border: 4px solid #FFD93D;
            }
        """)
        layout.addWidget(image_label)

        # === Info Labels ===
        weight_label = QLabel(f"WEIGHT: {pokemon_data['weight']}")
        height_label = QLabel(f"HEIGHT: {pokemon_data['height']}")
        types = ", ".join([t['type']['name'] for t in pokemon_data['types']])
        types_label = QLabel(f"TYPES: {types.upper()}")
        ability = pokemon_data['abilities'][0]['ability']['name']
        ability_label = QLabel(f"ABILITY: {ability.upper()}")

        info_labels = [weight_label, height_label, types_label, ability_label]

        for lbl in info_labels:
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setFont(self.pixel_font)
            lbl.setStyleSheet("""
                QLabel {
                    color: black;
                    background-color: #FF3B3F;
                    border: 4px solid #FFD93D;
                    padding: 6px;
                }
            """)
            layout.addWidget(lbl)

        self.setLayout(layout)

    def setSize(self, param, param1):
        pass


def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching Pokémon data")
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    pokemon_name = "groudon-primal"  # 🔥 Change Pokémon here
    data = get_pokemon_info(pokemon_name)

    if data:
        card = RetroPokemonCard(data)
        card.setSize(300, 500)  # ✅ Fixes window size (no resizing)
        card.show()
        sys.exit(app.exec_())
