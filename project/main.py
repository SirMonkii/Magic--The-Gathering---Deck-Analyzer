import scryfall_api

card_name = scryfall_api.set_card_name()  # Captura o nome da carta
card_info = scryfall_api.get_card_info(card_name)  # Obtém os detalhes da API

if card_info:  # Só exibe os detalhes se a requisição foi bem-sucedida
    scryfall_api.show_card_info(card_info)
