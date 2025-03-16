red_mana = 0
blue_mana = 0
green_mana = 0
white_mana = 0
black_mana = 0
cmc = 0

def color_count(cards):  # Função que conta a quantidade de mana de cada cor no deck
    global red_mana, blue_mana, green_mana, white_mana, black_mana
 
    
    for key in cards:  # Itera sobre todas as cartas no deck
        colors = cards[key]["mana_cost"]  # Obtém o custo de mana da carta
        
        # Conta a quantidade de cada símbolo de mana
        red_mana += colors.count("R")
        blue_mana += colors.count("U")
        green_mana += colors.count("G")
        white_mana += colors.count("W")
        black_mana += colors.count("B")
 
    # Exibe a quantidade de cada tipo de mana presente no deck
    print(f"R:{red_mana}, U:{blue_mana}, G:{green_mana}, W:{white_mana}, B:{black_mana}")
    
def average_mana(cards):
    
    red_average = red_mana / len(cards)
    blue_average = blue_mana / len(cards)
    green_average = green_mana / len(cards)
    white_average = white_mana / len(cards)
    black_average = black_mana / len(cards)
    
    print(f"R:{red_average:.2f}, U:{blue_average:.2f}, G:{green_average:.2f}, W:{white_average:.2f}, B:{black_average:.2f}")

def average_cmc(cards):
    global cmc
    
    for key in cards:
        converted_cost = cards[key]["cmc"]
        
        cmc += converted_cost
        
    print(cmc)
    
    average_cost = cmc / len(cards)
    
    print(f"{average_cost:.2f}")