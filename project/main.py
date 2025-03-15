import scryfall_api
import os

os.system("cls")

insert_cards = True

deck = {}

while insert_cards:
    
    card_name = scryfall_api.set_card_name()  # Captura o nome da carta
    
    if (card_name.lower() == "exit"):
        break
        
    
    card_info = scryfall_api.get_card_info(card_name)  # Obtém os detalhes da API

    if card_info:  # Só exibe os detalhes se a requisição foi bem-sucedida
        scryfall_api.show_card_info(card_info)
    
    deck[str(card_info["name"]).lower()] = card_info
    