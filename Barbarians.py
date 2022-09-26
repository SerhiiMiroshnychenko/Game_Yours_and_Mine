# Твої та Мої
# Barbarians are the only enemies
import random
from typing import Dict

y_warriors, m_warriors = 100, 0
y_gold, m_gold = 0, 0
y_farms, m_farms = 1, 1
y_gold_step = y_farms
m_gold_step = m_farms
day = 0
while True:
    # розрахунок ціни ферми
    y_buy_farm = (4 + y_farms) * (1 + y_farms // 10)
    m_buy_farm = (4 + m_farms) * (1 + m_farms // 10)
    # візуальний блок
    print('_'*100)
    print("\n"+"\t"*6 + f"ДЕНЬ {day}")
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

    # блок нападу варварів
    if day % 10 == 0 and day > 0:  # умова
        enemy = "barbarians"  # визначення хто вороги
        # довідник ворогів
        enemies = {"barbarians": {"names": "варвари",
                                  "number": (day // 10) * (100 + 10 * random.randint(0, 21)),
                                  "damage_ind": random.randint(1, 4),
                                  },
                   }
        enemy_number = enemies[enemy]["number"]  # кількість ворогі
        loots = {"barbarians" : enemy_number // 20}
        print("\n" + f" {chr(9760)} " * 20)
        print(f'!!! На Вас напали вороги! {enemies[enemy]["names"].title()} у кількості {enemies[enemy]["number"]}!!!')
        input("Нажміть Enter щоб продовжити! ")
        print("\n" + "\t" * 6 + 'БІЙ')
        print(f"Ваші війська: {y_warriors} \t\t\t\t\t\t\t {enemies[enemy]['names'].title()}: {enemy_number}")
        input("Enter: ")
        while y_warriors > 0 and enemy_number > 0:  # якщо ще є кому битися
            y_damage = 10 * random.randint(1, 5)
            e_damage = 10 * enemies[enemy]['damage_ind']
            y_warriors -= e_damage
            enemy_number -= y_damage
            y_warriors = y_warriors if y_warriors > 0 else 0
            enemy_number = enemy_number if enemy_number > 0 else 0
            print(f"              {y_warriors} \t\t\t\t\t\t\t          {enemy_number}")
        if y_warriors <= 0 and enemy_number > 0:  # пройграш
            print('!!!!!!!!!!!!!!!!!!!')
            print('!!! ВИ ПРОГРАЛИ !!!')
            print('!!!!!!!!!!!!!!!!!!!')
            break
        elif y_warriors > 0 and enemy_number <= 0:  # виграш
            print('!!!!!!!ВІТАЮ!!!!!!!')
            print('!!! ВИ ВИЙГРАЛИ !!!')
            print(f'Ваша здобич {loots[enemy]} золота!')
            y_gold += loots[enemy]  # отримання здобичі
        elif y_warriors <= 0 and enemy_number <= 0:  # нічія
            print('!!! ПІРОВА ПЕРЕМОГА !!!')
    else:
        pass

    # блок додавання золота ігроку
    chance = random.randint(0, 11)
    if chance == 10:
        add_gold = 3
    elif chance == 9 or chance == 8:
        add_gold = 2
    else:
        add_gold = 1
    y_gold_step = y_farms * add_gold
    y_gold += y_gold_step

    # рахунок днів
    if day == 100:
        print("\n"+"\t"*4 + f"!!!   V.I.C.T.O.R.Y.   !!!")
        break
    day += 1
print("\n"+"\t"*4 + f".....GAME OVER.....")
