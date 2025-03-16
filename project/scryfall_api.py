import requests  # Biblioteca para realizar requisições HTTP

base_url = "https://api.scryfall.com"  # URL base da API Scryfall


def get_card_info(name):  # Função para buscar informações da carta pelo nome
    url = f"{base_url}/cards/named?fuzzy={name}"  # Monta a URL de busca na API
    response = requests.get(url)  # Faz a requisição HTTP GET
    
    if response.status_code == 200:  # Se a requisição for bem-sucedida
        card_data = response.json()  # Converte a resposta para JSON
        return card_data  # Retorna os dados da carta
    else:
        card_data = response.json()  # Converte a resposta para JSON em caso de erro
        print(f"\nFailed to obtain the card data. Status code: {response.status_code}\n{card_data['details']}\n\n")
        return None  # Retorna None em caso de falha


def set_card_name():  # Função para receber o nome da carta do usuário
    name = input("Please enter the full name of your card: (To finish entering your cards, type 'EXIT')\n\n") 
    return name  # Retorna o nome da carta digitado


def show_card_info(card_info):  # Função para exibir informações da carta
    print(f"\nCard Name: {card_info['name']}")
    print(f"Converted Mana Cost: {card_info['cmc']}")
    print(f"Color Identity: {card_info['color_identity']}")
    print(f"Mana cost: {card_info['mana_cost']}\n\n")