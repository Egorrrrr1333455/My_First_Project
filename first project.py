#создать класс персонажа , продумать его характеристики добавить механику выбора рассы и класса.

class Human:
    def __init__(self,name,race,clas,level,exp,hp,strenght,agility,intelekt,dex,damage,armor):
        self.name = name
        self.race = race
        self.clas = clas
        self.level = level
        self.exp = exp
        self.hp = hp
        self.strenght = strenght
        self.agility = agility
        self.intelekt = intelekt
        self.dex = dex
        self.damage = damage
        self.armor = armor
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
            self.damage += 5
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