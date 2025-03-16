import scryfall_api  # Módulo para interagir com a API Scryfall
import mana_analysis  # Módulo para análise de mana do deck
import os  # Módulo para comandos do sistema operacional

# Limpa o terminal sempre que o código for executado (para melhor visualização durante testes)
os.system("cls")

insert_cards = True  # Variável de controle para inserção de cartas

deck = {}  # Dicionário que armazenará as cartas do deck

# Loop para permitir a inserção contínua de cartas
while insert_cards:
    card_name = scryfall_api.set_card_name()  # Obtém o nome da carta digitado pelo usuário
    
    if card_name.lower() == "exit":  # Se o usuário digitar "exit", o loop é interrompido
        break
    
    card_info = scryfall_api.get_card_info(card_name)  # Busca informações da carta na API
    
    if card_info:  # Se a carta for encontrada, exibe suas informações
        scryfall_api.show_card_info(card_info)
    
    if card_info is not None:  # Se a carta for válida, adiciona ao deck
        deck[str(card_info["name"]).lower()] = card_info
    
# Realiza a contagem de cores de mana no deck inserido
mana_analysis.color_count(deck)
mana_analysis.average_mana(deck)
mana_analysis.average_cmc(deck)