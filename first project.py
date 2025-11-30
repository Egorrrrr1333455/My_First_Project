import random


class Hero:
    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.level = 1
        self.exp = 0
        self.hp = 100
        self.damage = 10
        self.armor = 5

        if race == "человек":
            self.hp += 20
            self.damage += 5
        elif race == "эльф":
            self.hp += 10
            self.damage += 10
        elif race == "гном":
            self.hp += 30
            self.damage += 3
        elif race == "орк":
            self.hp += 15
            self.damage += 15


    def show_stats(self):
        print(f"=== ТВОЙ ПЕРСОНАЖ ===")
        print(f"Имя: {self.name}")
        print(f"Раса: {self.race}")
        print(f"Класс: {self.clas}")
        print(f"Уровень: {self.level}")
        print(f"Опыт: {self.exp}/100")
        print(f"Здоровье: {self.hp}")
        print(f"Урон: {self.damage}")
        print(f"Броня: {self.armor}")

    def attack(self, enemy):

        hit = self.damage + random.randint(1, 5)
        enemy.hp -= hit
        return hit

class Enemy:
    def __init__(self, level):
        self.types = ["Гоблин", "Орк", "Скелет", "Волк", "Разбойник"]
        self.name = random.choice(self.types)
        self.level = level
        self.hp = 30 + (level * 10)
        self.damage = 5 + (level * 2)
        self.exp_reward = 20 + (level * 5)

    def show_stats(self):
        print(f"\n=== ВРАГ ===")
        print(f"Имя: {self.name}")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.hp}")
        print(f"Урон: {self.damage}")

    def attack(self, hero):
        hit = self.damage + random.randint(1, 3)
        hero.hp -= hit
        return hit

def create_hero():
    print("🎮 ДОБРО ПОЖАЛОВАТЬ В ИГРУ!")
    print("=" * 30)

    print("🎯ВЫБЕРИ РАСУ:")
    print("1. Человек (+20 HP, +5 урон)")
    print("2. Эльф (+10 HP, +10 урон)")
    print("3. Гном (+30 HP, +3 урон)")
    print("4. Орк (+15 HP, +15 урон)")

    race_choice = input("Твой выбор (1-4): ")
    races = ["", "человек", "эльф", "гном", "орк"]
    race = races[int(race_choice)]

    print("⚔️ВЫБЕРИ КЛАСС:")
    print("1. Воин (+20 HP, +10 урон, +10 брони)")
    print("2. Лучник (+10 HP, +15 урон, +5 брони)")
    print("3. Маг (+5 HP, +25 урон, +2 брони)")

    class_choice = input("Твой выбор (1-3): ")
    classes = ["","воин","лучник","маг"]
    clas = classes[int(class_choice)]

    hero = Hero(name, race, clas)
    hero.show_stats()
    return hero

def fight(hero, enemy):
    print(f"⚔️НАЧИНАЕТСЯ БОЙ С {enemy.name}!")

    while hero.hp > 0 and enemy.hp > 0:
        print("" + "=" * 30)
        print(f"Твое HP: {hero.hp} | HP врага: {enemy.hp}")

        input("Нажми Enter чтобы атаковать...")
        hero_hit = hero.attack(enemy)
        print(f"💥 Ты нанес {hero_hit} урона!")

        if enemy.hp <= 0:
            print(f"🎉 Ты победил {enemy.name}!")
            hero.exp += enemy.exp_reward
            print(f"Получено опыта: {enemy.exp_reward}")
            return True

        enemy_hit = enemy.attack(hero)
        print(f"👹 {enemy.name} нанес тебе {enemy_hit} урона!")

        if hero.hp <= 0:
            print("💀 Ты проиграл...")
            return False

def game():
    hero = create_hero()
    level = 1

    while hero.hp > 0:
        print(f"🏰Ты на уровне {level}")
        enemy = Enemy(level)
        enemy.show_stats()

        if not fight(hero, enemy):
            break

        if hero.exp >= 100:
            hero.level += 1
            hero.exp = 0
            hero.hp += 20
            hero.damage += 5
            print(f"🎉Ты достиг {hero.level} уровня!")
            hero.show_stats()

        level += 1
        input("Нажми Enter чтобы продолжить...")

    print("Игра окончена!")

game()