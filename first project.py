# Импортируем модуль для случайных значений
import random
from enum import Enum


class Human:
    def __init__(self, name, race, clas, level, exp, hp, strenght, agility, intelekt, dex, damage, armor, money, inv):
        self.name = name
        self.race = race
        self.clas = clas
        self.level = level
        self.exp = exp  #
        self.hp = hp  # Здоровье
        self.strenght = strenght  # тем больше сила,больше хп и урона будет.
        self.agility = agility  # Если устанем,будет шанс промахнутся по сопернику.
        self.intelekt = intelekt  # Обмануть торговца
        self.dex = dex  # Шанс уклонится от атак.
        self.damage = damage  # cколько урона мы наносим.
        self.armor = armor  # Отрожает урон.
        self.money = money  # Деньги игрока
        self.inv = []  # Инвентарь игрока
        self.maxhp = hp  # Макс хп
        self.timebuff = 0  # Отвечает за количевство битв с баффом

        # Добавляем плюсы расы

    def apply_race(self):
        if self.race == "human":
            self.hp += 10
            self.strenght += 5
            self.agility += 0
            self.intelekt += 1
            self.dex += 0
            self.damage += 5
            self.armor += 5
        elif self.race == "angel":
            self.hp += 20
            self.strenght += 10
            self.agility += 5
            self.intelekt += 10
            self.dex += 0
            self.damage += 15
            self.armor += 10
        elif self.race == "mink":
            self.hp += 10
            self.strenght += 5
            self.agility += 20
            self.intelekt += 20
            self.dex += 30
            self.damage += 10
            self.armor += 15
        elif self.race == "cyborg":
            self.hp += 40
            self.strenght += 30
            self.agility += 20
            self.intelekt += 25
            self.dex += 20
            self.damage += 50
            self.armor += 40

    def clas(self):
        if self.clas == "guardian":
            self.hp += 20
            self.strenght += 15
            self.agility += 10
            self.intelekt += 9
            self.dex += 10
            self.damмнage += 5
            self.armor += 25
        elif self.race == "archor":
            self.hp += 10
            self.strenght += 5
            self.agility += 0
            self.intelekt += 20
            self.dex += 1
            self.damage += 15
            self.armor += 5
        elif self.race == "witch":
            self.hp += 20
            self.strenght += 10
            self.agility += 5
            self.intelekt += 0
            self.dex += 5
            self.damage += 30
            self.armor += 10

            # добавляем функцию показа статистик по команде

    def show_stats(self):
        print(f"🙉Имя: {self.name}!")
        print(f"🧨Раса: {self.race}")
        print(f"🔮Класс: {self.clas}")
        print(f"🎲Уровень: {self.level}")
        print(f"🎨Экспа: {self.exp}")
        print(f"💓Здоровье: {self.hp}")
        print(f"👊Сила: {self.strenght}")
        print(f"🛠Усталость: {self.agility}")
        print(f"🧠Интелект: {self.intelekt}")
        print(f"🐇Ловкость: {self.dex}")
        print(f"🔋Урон: {self.damage}")
        print(f"🧔Броня: {self.armor}")

        # функция прокачки левела

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.damage += 5
        self.dex += 5
        self.strenght += 5
        self.intelekt += 5
        self.agility += 3
        print(f"Вы повысили уровень до {self.level}! Вы можете проверить свои статистики.")

        # функция для получение опыта

    def exp(self, exp):
        self.exp += exp
        print(f"Вы получили {exp} Опыта!")
        x = 0
        while self.exp >= 50:
            self.exp -= 50
            x += 1
        print(f"Получено {x} Уровней!")

    def show_inv(self):
        for i, j in enumerate(self.inv, 0):
            print(f"{i} {j.name} {j.price} ")

    def use_item(self, num):
        item = self.inv[num]
        if item.item_tupe == "heal":
            if self.hp == self.maxhp:
                print(f"У вам максимальное количевство здоровья!")
            elif self.maxhp < self.hp <= item.value:
                self.hp = self.maxhp
                print(f"Вы потеряли своё зелье! У вас максимальное количевство здоровья")
            else:
                self.hp += item.value
                print(
                    f"Вы потеряли своё зелье и восстановили {item.value} здоровья! У вас теперь {self.hp} Здоровья!!!")

            self.inv.remove(item)
        elif item.item_tupe == "buff":
            if item in self.inv:
                if "Сила" in item.name:
                    self.damage += 4
                    self.timebuff = 2
                    item.remove(item)
                    print(f"Вы использовали зелье силы! к вашему урону добавилось 4 единицы! Это будет длится 2 боя!")
        elif item.item_tupe == "Зелье ловкости":
            self.dex += 5
            self.timebuff += 2
            print(f"Вы использовали зелье ловкости!!!")
            self.inv.remove(item)

        elif item.item_tupe == "armor":
            self.damage += item.value
            print(f"Вы успешно одели {item.name}! Броня увеличена на {item.value}!")
            self.inv.remove(item)

        elif item.item_tupe == "weapon":
            self.damage += item.value
            print(f"Вы успешно взяли {item.name}! Урон увеличен на {item.value}!!! ")
            self.inv.remove(item)


class Enemy:
    def __init__(self, damage, armor, intelekt, hp, level, exp, dex, name):
        self.damage = damage
        self.armor = armor
        self.intelekt = intelekt
        self.hp = hp
        self.level = level
        self.exp = exp
        self.dex = dex
        self.name = name

        # Статистика врага

    def show_statss(self):
        print(f"Имя врага: {self.name}")
        print(f"Дамаг: {self.damage}")
        print(f"Здоровье: {self.hp}")
        print(f"Уровень: {self.level}")
        print(f"Экспа: {self.exp}")
        print(f"Ловкость:{self.dex}")
        print(f"Броня: {self.armor}")
        print(f"Интелект: {self.intelekt}")


class Rarity(Enum):
    rare = "Редкий"
    epic = "Эпический"
    mythic = "Мифический"
    legendary = "Легендарный"


class Item:
    def __init__(self, name: str, item_tupe: str, value: int, price: float, rarity: str,
                 stats: dict = None):  # создаём класс предметов и класс трэйдера
        self.name = name
        self.item_tupe = item_tupe
        self.value = value
        self.price = price
        self.rarity = rarity
    @staticmethod
    def generation_item(level,item_tupe):
        chance_random_item = random.randint(1, 100)
        if level <= 15:
            if chance_random_item <= 5:
                rarity = Rarity.legendary
                price_multy, value_multy = 3, 3
            elif chance_random_item <= 13:
                rarity = Rarity.mythic
                price_multy, value_multy = 1.8, 1.4
            elif chance_random_item <= 25:
                rarity = Rarity.epic
                price_multy, value_multy = 1.5, 1.2
            else:
                rarity = Rarity.rare
                price_multy, value_multy = 1, 0.6
        else:
            if chance_random_item <= 8:
                rarity = Rarity.legendary
                price_multy, value_multy = 3, 3
            elif chance_random_item <= 19:
                rarity = Rarity.mythic
                price_multy, value_multy = 1.8, 1.4
            elif chance_random_item <= 35:
                rarity = Rarity.epic
                price_multy, value_multy = 1.5, 1.2
            else:
                rarity = Rarity.rare
                price_multy, value_multy = 1, 0.6

        value = 10 #* value_multy
        price = 10 #* price_multy
        all_buffs = ["Ловкости", "Силы"]
        random_buff = random.choice(all_buffs)
        if item_tupe == "heal":
            name = "Зелье исцеления"
        elif item_tupe == "buff":
            name = f"Зелье {random_buff}"
        elif item_tupe == "weapon":
            name = f"{rarity} Меч!"
        else:
            name = f"{rarity} Броня"
        return Item(name, item_tupe, value, price, rarity)


class Trader:
    # шансы на трэдеров/торговцов
    chance = {
        "Мечник": {"Шансы": 0.2, "имя": "Диабло"},
        "Броник": {"Шансы": 0.4, "имя": "Урбан"},
        "Алхимик": {"Шансы": 0.3, "имя": "Александр"},
        "Волшебник": {"Шансы": 0.1, "имя": "Пётр"}

    }

    # предметы , стоимость и названия предметов у тороговцев
    ITEMS = {
        "Мечник": [
            Item.generation_item(level=15, item_tupe="weapon"),
            Item.generation_item(level=29, item_tupe="weapon"),
            Item.generation_item(level=39, item_tupe="weapon"),
            Item.generation_item(level=50, item_tupe="weapon")
        ],
        "Броник": [
            Item.generation_item(level=15, item_tupe="armor"),
            Item.generation_item(level=29, item_tupe="armor"),
            Item.generation_item(level=39, item_tupe="armor"),
            Item.generation_item(level=50, item_tupe="armor")
        ],
        "Алхимик": [
            Item.generation_item(level=15, item_tupe="buff"),
            Item.generation_item(level=29, item_tupe="buff"),
            Item.generation_item(level=39, item_tupe="buff"),
            Item.generation_item(level=50, item_tupe="buff")
        ]
    }

    # рандомайзер
    def __init__(self, name, tupe):
        if tupe in self.chance:
            self.tupe = tupe
            self.name = self.chance[self.tupe]["имя"]

            # Опять же рандомайзер на торговцев

    def shops(self):
        rand = random.randint(0, 100)
        if rand <= 20:
            return "Мечник"
        elif rand <= 60:
            return "Броник"
        elif rand <= 90:
            return "Алхимик"
        elif rand <= 100:
            return "Волшебник"

    # создаём рандомные оружия для торговцев

    def create_inv(self):
        inv = []
        special_items = []
        if self.tupe in self.ITEMS:
            special_items = self.ITEMS[self.tupe]

        cifras = random.randint(3, 5)
        for i in range(cifras):
            if special_items == True:
                item = random.choice(special_items)
                inv.append(item)
        return inv

    # Оружия)
    ITEMS = {
        "weapon": [
            Item.generation_item(level=15, item_tupe="weapon"),
            Item.generation_item(level=29, item_tupe="weapon"),
            Item.generation_item(level=35, item_tupe="weapon"),
            Item.generation_item(level=45, item_tupe="weapon"),
            Item.generation_item(level=60, item_tupe="weapon")
        ],
        "armor": [
            Item.generation_item(level=15, item_tupe="armor"),
            Item.generation_item(level=29, item_tupe="armor"),
            Item.generation_item(level=35, item_tupe="armor"),
            Item.generation_item(level=45, item_tupe="armor"),
            Item.generation_item(level=60, item_tupe="armor"),
        ],
        "potion": [
            Item.generation_item(level=15, item_tupe="heal"),
            Item.generation_item(level=29, item_tupe="buff"),
            Item.generation_item(level=39, item_tupe="buff"),

        ]
    }

    def Show_inv_trader(self, Trader):
        for i, j in enumerate(self.inv, 0):
            print(f"{i} {j.name} {j.price}")

    # класс врага


class Ennemy:
    def __init__(self, name, hp, level, exp, strength, agility, dex, damage, armor):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.dex = dex
        self.damage = damage
        self.armor = armor
        self.level = level
        self.exp = exp

        # Уровни врага
    @staticmethod
    def enemylevel(level):
        enemy = [Enemy(3, 1, 1, 10, 1, 10, 1, "Скелет"),
                 Enemy(5, 1, 1, 5, 3, 20, 5, "Зомби"),
                 Enemy(10, 1, 1, 10, 5, 25, 13, "Ведьма"),
                 Enemy(15, 15, 25, 35, 7, 50, 15, "Зомби-Гигант"),
                 Enemy(20, 30, 35, 55, 10, 65, 17, "Джеф-Убийца"),
                 Enemy(25, 15, 20, 50, 12, 70, 18, "Маг"),
                 Enemy(30, 45, 50, 70, 14, 100, 19, "Мега-Рыцарь"),
                 Enemy(45, 70, 90, 90, 17, 120, 22, "Падший-Ангел"),
                 Enemy(50, 0, 150, 150, 19, 170, 25, "Электро-ведьма"),
                 Enemy(80, 100, 190, 150, 251, 200, 25, "Титан"),

                 ]
        enemylvl = []
        bosslevel = max(1, level + random.randint(-1, 2))
        for i in enemy:
            if i.level <= bosslevel:
                enemylvl.append(i)

        randomch = random.choice(enemylvl)
        return randomch

        self.hp = 15
        self.strenght = 1
        self.agility = 2
        self.intelekt = 0
        self.dex = 0
        self.damage = 2
        self.armor = 5
        self.name = "Зомби"

        self.hp = 30
        self.strenght = 5
        self.agility = 5
        self.intelekt = 15
        self.dex = 0
        self.damage = 10
        self.armor = 3
        self.name = "Ведьма"

        self.hp = 55
        self.strenght = 5
        self.agility = 5
        self.intelekt = 15
        self.dex = 15
        self.damage = 25
        self.armor = 5
        self.name = "Маг"

        self.hp += 80
        self.strenght += 5
        self.agility += 5
        self.intelekt += 15
        self.dex += 0
        self.damage += 10
        self.armor += 25
        self.name = "Электро-маг"

        self.hp += 150
        self.strenght += 100
        self.agility += 50
        self.intelekt += 45
        self.dex += 50
        self.damage += 100
        self.armor += 50
        self.name = "Титан"


def bossdie(enemy):
    if enemy.hp <= 0:
        return True


def humandie(human):
    if human.hp <= 0:
        print(f"вы потерпели поражение😭!")
        return True


def Hit_Chance(enemy, human):
    hitchance = random.randint(human.dex, human.dex + 15) / 100
    if hitchance <= enemy.dex:
        print(f"Вы промахнулись!")
        return False
    else:
        return True


def enemy_hit_chance(human, enemy):
    enemyhitchance = random.randint(enemy.dex, enemy.dex + 15) / 100
    if enemyhitchance <= human.dex:
        print(f"Враг по вам попал и у вас осталось {human.hp} здоровья")
        return True
    else:
        print(f"Враг не попал! У него осталось {enemy.hp} Здоровья!")
        return False

    # битва с босом


def fight(human, enemy):
    print(f"Вы встретились с босом! его имя: {enemy.name}! у него {enemy.hp} Здоровья! Это легендарная битва.")

    print(f"Нажмите 1 что бы начать битву! Или нажмите 2 что-бы попытаться сбежать.")

    # выбор человека что он будет делать.
    vibor = input(f"Введите ваш выбор:")
    while human.hp > 0 and enemy.hp > 0:
        if vibor == 1:
            # Ну типа как они дратся будут
            vibor_bitvi = input(f"Нажмите 1 что-бы ударить, Нажмите 2 что бы увернутся")
            if vibor_bitvi == 1:
                check = Hit_Chance(enemy, human)
                if check == True:

                    enemy.hp -= human.strenght
                    print(f"Вы ударили врага у него осталось {enemy.hp}!")

                    # проверяем живой или мертвый босс
                    enemyliveordie = bossdie(enemy)
                    if enemyliveordie == True:
                        Human.exp(enemy.exp)
                        return f"Вы победили врага {enemy.name}"
                else:

                    print(f"Вы не попали по врагу! У него всё ещё {enemy.hp} Здоровья!")

        # Шанс уклона персонажа.
        dodge_chance = random.randint(1, 100)

        # Тем больше ловкость персонажа тем больше шанс уклонится
        if dodge_chance <= human.dex:
            print(f"Вы уклонились от атаки {enemy.name}")  # Уклонился
            continue

            # else:
            #
            # enemy_damage =
            # human.hp -= enemy_damage
            # print(f"{enemy.name} попал и нанёс {enemy.damage} урона! у вас осталось {human.hp} ХП.")

        if enemy.hp > 0:
            savee = enemy_hit_chance(human, enemy)
            if savee == True:
                human.hp -= enemy.damage
                print(f"{enemy.name} попал и нанёс {enemy.damage} урона! у вас осталось {human.hp} здоровье.")
                continue
            else:
                print(f"Вы увернулись!")
                continue


def events(human):
    events_spisok = ["озеро", "торговец", "Битва", "Сундук", "Цветок"]
    # цветок - лечебный
    eventss = "Битва" #random.choice(events_spisok)
    if eventss == "озеро":
        print(f"Вы нашли Волшебное Озеро ! Оно вам восстановит чу-чуть здоровья! ")
        human.hp += 5
        print(f"Вы восстановили здоровье! Теперь у вас {human.hp} Здоровья!")

    elif eventss == "торговец":
        print(f"Вы встретили торговца!")
        zelye = Item("Зелье Лечения","heal","20","10","rare")
        mech = Item("Старый Меч", "weapon", "5", "30", "rare")
        bronya = Item("Кожанная Броня", "armor", "3", "25", "rare")

        Torgovec = Trader()

        while True:
            Torgovec.Show_inv_trader()
            vopros = input("Нажмите 1 что-бы торговатся , нажмите 2 если хотите уйти.")
            if vopros == 1:
                print(f"Товары торговца")
                print(f"1 - {zelye.name} +  {zelye.value} HP {zelye.price} - Стоит монет.")
                print(f"1 - {mech.name} + {mech.value} Урона {mech.price} - Стоит монет.")
                print(f"1 - {bronya.name} + {bronya.value} Брони {bronya.price} - Стоит монет.")

                buy = input("Что хотите купить? (1-3)")

                if buy == "1" and human.money >= zelye.price:
                    human.money -= zelye.price
                    human.inv.append(zelye)
                    print(f"Вы купили {zelye.name}!")


                if buy == "2" and human.money >= mech.price:
                    human.money -= mech.price
                    human.inv.append(mech)
                    print(f"Вы купили {mech.name}!")

                if buy == "1" and human.money >= bronya.price:
                    human.money -= bronya.price
                    human.inv.append(bronya)
                    print(f"Вы купили {bronya.name}!")


            # Тут будет код!!!!!!!!!!!
            elif vopros == 2:
                break

    elif eventss == "Битва":
        print(f"⚔️ Вы встретили врага!")
        enemy = Ennemy.enemylevel(human.level)  # Ну вообщем это генерация подходящего босса под уровень нашего игрока.
        fight(human,enemy)

    elif eventss == "Сундук":
        print(f"💰Вы нашли сундук!")
        money_found = random.randint(10, 50)
        human.money += money_found
        print(f"Вы нашли {money_found} монет! 💰")

    elif eventss == "Цветок":
        print(f"🌸Вы нашли волшебный цветок!")
        heal = random.randint(5, 20)
        human.hp += heal
        print(f"🌸Цветок вам восстановил {heal} Здоровья! Теперь у вас {human.hp} Здоровья!!!")


def Games():
    print(f"Здравствуйте! Вы - путешественик ! На вашем пути будет происходить много событий. Удачи!")
    quest = input("Введите имя вашего персонажа:")
    print(f"Выберите вашу расу: 1 - Хюман , 2 - Ангел , 3 - Минк , 4 - Киборг.")
    race_choice = input("Введите свой выбор:")
    race_dict = {"1": "Human", "2": "Angel", "3": "Mink", "4": "Cyborg"}
    race = race_dict.get(race_choice, "Human")

    print(f"Выберите ваш класс: 1 - Рыцарь , 2 - Мечник , 3 - Ведьма.")
    clas_choice = input("Введите ваш выбор:")
    clas_dict = {"1": "Guardian", "2": "archor", "3": "Witch"}
    classs = clas_dict.get(clas_choice, "archor")

    player = Human(name=quest, race=race, clas=classs, level=1, exp=0, hp=50, strenght=10, agility=10, intelekt=5,
                   dex=0, damage=5, armor=5, money=1000, inv=[])
    player.show_stats()
    print(f"Игра начата.")
    while True:
        print(f"\n{"-" * 50}")
        print("\n1 - Продолжить путешевствие ")
        print("2 - Показать статистику ")
        print("3 - Показать инвентарь ")
        print("4 - Использовать предмет ")
        print("5 - Выйти из игры ")
        quest2 = input("Введите свой выбор:")

        if quest2 == "1":
            events(player)
        elif quest2 == "2":
            player.show_stats()
        elif quest2 == "3":
            player.show_inv()
        elif quest2 == "4":
            if player.inv:
                player.show_inv()
                index_item = int(input("Введите номер предмета:"))
                player.use_item(index_item)
            else:
                print(f"Ваш инвентарь пуст.")

        elif quest2 == "5":
            print(f"Спасибо что играли.")
            break
        else:
            print(f"Введите другое число.")

        if player.hp <= 0:
            print("Игра окончена. Вы трагически погибли.")
            break


Games()
