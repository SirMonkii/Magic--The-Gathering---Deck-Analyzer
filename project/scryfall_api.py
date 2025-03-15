import requests

base_url = "https://api.scryfall.com"

def get_card_info(name):
    url = f"{base_url}/cards/named?fuzzy={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        card_data = response.json()
        return card_data
    else:
        print(f"\nFailed to obtain the card data. Status code: {response.status_code}\n")
        return None  # Retorna None para evitar erros na exibição

def set_card_name():
    name = input("Please enter the full name of your card: ")  # Captura o nome corretamente
    return name

def show_card_info(card_info):
        print(f"\nCard Name: {card_info['name']}")
        print(f"Converted Mana Cost: {card_info['cmc']}")
        print(f"Color Identity: {card_info['color_identity']}")
        print(f"Mana cost: {card_info['mana_cost']}")
