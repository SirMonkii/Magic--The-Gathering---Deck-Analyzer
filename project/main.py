from pywebio import start_server
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_table, put_buttons, put_html, clear
import scryfall_api
import mana_analysis

deck = {}

def add_card():
    while True:
        card_name = input(
        "Digite o nome da carta (ou clique em 'EXIT' para finalizar):",
        type="text")
        
        if card_name.lower() == "exit":
            break
        
        card_info = scryfall_api.get_card_info(card_name)
        
        if card_info:
            deck[str(card_info["name"]).lower()] = card_info
            put_text(f"Adicionada: {card_info['name']} - {card_info['mana_cost']}")
            put_html(f"<img src =\"{card_info['image_uris']['small']}\" alt=\"card_image\" style=\"max-width:80%;\">")

            
        else:
            put_text("Carta não encontrada. Tente novamente.")

def analyze_deck():
    if not deck:
        put_text("Nenhuma carta adicionada ao deck ainda.")
        return
    
    clear()
    
    mana_analysis.color_count(deck)
    mana_analysis.average_mana(deck)
    mana_analysis.average_cmc(deck)
    
    put_table([
        ["Cor", "Quantidade"],
        ["Vermelho (R)", mana_analysis.red_mana],
        ["Azul (U)", mana_analysis.blue_mana],
        ["Verde (G)", mana_analysis.green_mana],
        ["Branco (W)", mana_analysis.white_mana],
        ["Preto (B)", mana_analysis.black_mana],
        ["CMC Médio", f"{mana_analysis.cmc / len(deck):.2f}"],
    ])

def main():
    put_text("Bem-vindo ao analisador de deck de Magic: The Gathering!")
    put_buttons(["Adicionar Cartas", "Analisar Deck"], [add_card, analyze_deck])

if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
