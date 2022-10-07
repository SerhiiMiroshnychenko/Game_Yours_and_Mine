# Yours and Mine
# Твої та Мої
# Strategic war game on Python
import random
from prettytable import PrettyTable

y_warriors, m_warriors = 100, 0
y_gold, m_gold = 0, 0
y_farms, m_farms = 1, 1
y_gold_step = y_farms
m_gold_step = m_farms
day = 0
k = 0
while True:
    # розрахунок ціни ферми
    y_buy_farm = (4 + y_farms) * (1 + y_farms // 10)
    m_buy_farm = (4 + m_farms) * (1 + m_farms // 10) + day // 10
    # візуальний блок
    print('_' * 100)
    print("\n" + "\t" * 6 + f"ДЕНЬ {day}")
    print(f"Золото: {y_gold} \t\t\t\t\t\t\t Gold: {m_gold}")
    print(f"Ферми: {y_farms} \t\t\t\t\t\t\t Farms: {m_farms}")
    print(f"Воїни: {y_warriors} \t\t\t\t\t\t\t Warriors: {m_warriors}")
    print(f'\nЦіна однієї ферми: {y_buy_farm} золота. Щоб купити : натискайте "f" скільки ферм Вам треба.')
    print(f'Ціна сотні воїнів: 10 золота. Щоб купити : натискайте "w" скільки сотен Вам треба')
    print('Щоб накопичувати богатство: Enter')
    print('Щоб провтикати ход: все інше')

    # блок ігрока
    choice = input('\nЗробіть Ваш вибір: ')
    # купівля ферми
    if 'f' in choice.lower():
        choice_l = choice.lower()
        farms_numb = choice_l.count('f')
        if y_gold >= y_buy_farm * farms_numb:
            y_gold -= y_buy_farm * farms_numb
            y_farms += farms_numb
        else:
            print('Грошенят маловато!')
        # купівля військ
    if 'w' in choice.lower():
        choice_l = choice.lower()
        wars_numb = choice_l.count('w')
        if y_gold >= 10 * wars_numb:
            y_gold -= 10 * wars_numb
            y_warriors += 100 * wars_numb
        else:
            print('Грошенят маловато!')
        # пропуск хода
    elif '' in choice:
        pass
    else:
        pass

    # блок задання ворогів
    enemy = ""
    is_nomads = random.randint(0, 10)
    if day % 50 == 0 and day > 0:
        enemy = "black_hunters"
    elif day % 10 == 0 and day > 0:  # умова
        enemy = "barbarians"  # визначення хто вороги
    elif is_nomads == 0 and day > 0:  # умова
        enemy = "nomads"  # визначення хто вороги
    elif m_warriors > y_warriors:  # умова
        enemy = "computer"  # визначення хто вороги

    # довідник ворогів
    enemies = {
        '': {"names": "без ворогів",
             "number": 0,
             "damage_ind": 0,
             },
        "barbarians": {"names": "варвари",
                       "number": (day // 10) * (100 + 10 * random.randint(0, 11)),
                       "damage_ind": random.randint(1, 7),  # збільшити трохи урон + трохи кількість
                       },
        'nomads': {"names": "кочовики",
                   "number": (10 + random.randint(0, 21)) * day,  # зробити більшу кількість
                   "damage_ind": random.randint(1, 4),

                   },
        "computer": {"names": "мої",
                     "number": m_warriors,
                     "damage_ind": random.randint(1, 6),
                     },
        "black_hunters": {"names": "Чорні Мисливці",
                          "number": 1000 * day // 50,
                          "damage_ind": random.randint(5, 21),  # зробити більше урон
                          }
    }
    enemy_number = enemies[enemy]["number"]  # кількість ворогів
    loots = {'': 0,
             "barbarians": enemy_number // 20,
             'nomads': enemy_number // 15,

             "computer": m_gold,
             "black_hunters": 1000
             }
    # блок, що задає наявність бою
    if enemy == '':
        pass
    else:
        # блок нападу ворогів
        print("\n" + f" {chr(9760)} " * 20)
        print(f'!!! На Вас напали вороги! {enemies[enemy]["names"].title()} у кількості {enemies[enemy]["number"]}!!!')
        input("Нажміть Enter щоб продовжити! ")
        if enemy == "nomads":
            n_gold = enemy_number // 10
            print(f'Ви можете битися (нажміть "b") чи відкупитися за {n_gold} золота (нажміть "g")')
            k = 0
            while k == 0:
                choice_n = input("Зробіть вибір ('b' чи 'g'): ")
                if ('b' in choice_n.lower()) and (len(choice_n) == 1):
                    k = 1
                    break
                elif ('g' in choice_n.lower()) and (len(choice_n) == 1):
                    k = 2
                    y_gold -= n_gold
                    if y_gold >= 0:
                        print("Ви відкупилися. Кочьовики відступили.")
                    else:
                        y_gold = 0
                        destroy_f = y_farms // 3 if y_farms >= 3 else 1
                        y_farms -= destroy_f
                        print("!!! Вашого золота було замало і кочтовикі розграбили декілько ваших ферм !!!")
                else:
                    print("Зробіть правильний вибір! Треба вводити один з двох символів: 'b' чи 'g'!")
    if (enemy == '') or (k == 2):
        pass
    else:
        print("\n" + "\t" * 6 + 'БІЙ')
        print(f"Ваші війська: {y_warriors} \t\t\t\t\t\t\t {enemies[enemy]['names'].title()}: {enemy_number}")
        input("Enter: ")
        while y_warriors > 0 and enemy_number > 0:  # якщо ще є кому битися
            y_damage_ind = random.randint(0, 6)
            if y_damage_ind == 0:
                y_warriors += 100
                print("\t\t\tпідкріплення")
            y_damage = 10 * y_damage_ind
            e_damage = 10 * enemies[enemy]['damage_ind']
            y_warriors -= e_damage
            enemy_number -= y_damage
            y_warriors = y_warriors if y_warriors > 0 else 0
            enemy_number = enemy_number if enemy_number > 0 else 0
            print(f"              {y_warriors} \t\t\t\t\t\t\t          {enemy_number}")
        if y_warriors <= 0 and enemy_number > 0:  # пройграш
            if enemy == 'nomads':
                print('!!! ВИ ПРОГРАЛИ !!!')
                destroy_f = y_farms // 3 if y_farms >= 3 else 1
                loss_g = y_gold // 2
                print(f'Кочьовикі знищіли {destroy_f} ваших ферм і розграбили {loss_g} вашого золота!')
                y_farms -= destroy_f
                y_gold -= loss_g
            else:
                print('!!!!!!!!!!!!!!!!!!!')
                print('!!! ВИ ПРОГРАЛИ !!!')
                print('!!!!!!!!!!!!!!!!!!!')
                break
        elif y_warriors > 0 and enemy_number <= 0:  # виграш
            print('!!!!!!!ВІТАЮ!!!!!!!')
            print('!!! ВИ ВИЙГРАЛИ !!!')
            print(f'Ваша здобич {loots[enemy]} золота!')
            y_gold += loots[enemy]  # отримання здобичі
            if enemy == "computer":
                m_gold = 0
        elif y_warriors <= 0 and enemy_number <= 0:  # нічія
            print('!!! ПІРОВА ПЕРЕМОГА !!!')

    # блок додавання золота ігроку
    chance = random.randint(0, 11)
    if chance == 10:
        add_gold = 3
    elif chance == 9 or chance == 8:
        add_gold = 2
    elif chance == 0:
        add_gold = 10
    else:
        add_gold = 1
    y_gold_step = y_farms * add_gold
    y_gold += y_gold_step

    # блок компутера
    m_gold_step = m_farms
    m_gold += m_gold_step
    if m_gold >= m_buy_farm:
        m_gold -= m_buy_farm
        m_farms += 1
    elif m_gold >= 20:
        m_gold -= 20
        m_warriors += 100

    # рахунок днів
    if day == 100:
        print("\n" + "\t" * 4 + f"!!!   V.I.C.T.O.R.Y.   !!!")
        break
    day += 1
print("\n" + "\t" * 4 + f".....GAME OVER.....")

# Thank you for attention!
