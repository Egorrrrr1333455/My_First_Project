#создать класс персонажа , продумать его характеристики добавить механику выбора рассы и класса.

class Human:
    def __init__(self,name,race,clas,level,exp,hp,strenght,agility,intelekt,dex,damage,armor):
        self.name = name
        self.race = race
        self.clas = clas
        self.level = level
        self.exp = exp #
        self.hp = hp #Здоровье
        self.strenght = strenght #тем больше сила,больше хп и урона будет.
        self.agility = agility #Если устанем,будет шанс промахнутся по сопернику.
        self.intelekt = intelekt #Обмануть торговца
        self.dex = dex #Шанс уклонится от атак.
        self.damage = damage #cколько урона мы наносим.
        self.armor = armor #Отрожает урон.
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
    def level_up(self):
        self.level += 1
        self.hp += 10
        self.damage += 5
        self.dex += 5
        self.strenght += 5
        self.intelekt += 5
        self.agility += 3
        print(f"Вы повысили уровень до {self.level}! Вы можете проверить свои статистики.")
    def exp(self,exp):
        self.exp += exp
        print(f"Вы получили {exp} Опыта!")
        x = 0
        while self.exp >= 50:
            self.exp -= 50
            x += 1
        print(f"Получено {x} Уровней!")



    def
class Enemy:
    def __init__(self,damage,armor,intelekt,hp,level,exp,dex,name):
        self.damage = damage
        self.armor = armor
        self.intelekt = intelekt
        self.hp = hp
        self.level = level
        self.exp = exp
        self.dex = dex
        self.name = name
    def show_statss(self):
        print(f"Имя врага: {self.name}")
        print(f"Дамаг: {self.damage}")
        print(f"Здоровье: {self.hp}")
        print(f"Уровень: {self.level}")
        print(f"Экспа: {self.exp}")
        print(f"Ловкость:{self.dex}")
        print(f"Броня: {self.armor}")
        print(f"Интелект: {self.intelekt}")
class Item:
    def __init__(self,name:str,item_tupe:str,value:int,price:float,stats:dict = None):
class Trader:
    chance = {
        "Мечник":{"Шансы":0.2,"имя":"Диабло"},
        "Броник": {"Шансы":0.4,"имя":"Урбан"},
        "Алхимик": {"Шансы":0.3,"имя":"Александр"},
        "Волшебник": {"Шансы":0.1,"имя":"Пётр"}

    }

    def __init__(self,name,tupe):
        if tupe in self.chance:
            self.tupe = tupe
            self.name = self.chance [self.tupe]["имя"]

