# Ронин-квест v1.0.2

import sys
import os
from sounds import *
from ctypes import *
# from config import parameter_condition
from config import Enemy
from config import Skills
from config import Player
from config import Items
from random import randint
from colorama import Fore, Back, Style
from colorama import init

init()

e = Enemy()
s = Skills()
p = Player()
i = Items()

print(Back.CYAN)
print(Fore.BLACK)

# Прокачка
def menu_upgrade(p):
		while p.sp <= 0:
			print("У вас сейчас "+ Back.WHITE + "{}".format(p.sp) + Back.CYAN + " скиллпоинтов. Вам " + Fore.RED + "недоступна " + Fore.BLACK + "прокачка!")
			input("Нажмите ENTER, чтобы выйти")
			menu_main(p)

		while p.sp > 0: # when skillpoint > 0
			print("У вас сейчас "+ Back.WHITE + "{}".format(p.sp) + Back.CYAN + " скиллпоинтов.")
			print("Выбери улучшение!")
			print("---")
			print(Back.WHITE + Fore.RED)
			print("Здоровье: " + str('{:.1f}'.format(p.hp)) + "/" + str('{:.1f}'.format(p.max_hp)))
			print("Мана: " + str('{:.1f}'.format(p.mana)) + "/" + str('{:.1f}'.format(p.max_mana)))
			print("Сила: {}".format(p.pw))
			print(Fore.BLACK + Back.CYAN)
			print(Fore.WHITE + "Нажмите ENTER чтобы вернуться назад" + Fore.BLACK)
			n = input("Действие: ")	

			if n == "Здоровье":
				p.max_hp += 1
				p.hp += 1
				p.sp -= 1
				menu_upgrade(p)
			if n == "Мана":
				p.max_mana += 1
				p.mana += 1
				p.sp -= 1
				menu_upgrade(p)
			if n == "Сила":
				p.pw += 1
				p.sp -= 1
				menu_upgrade(p)
			else:
				menu_main(p)

# Параметры
def menu_stats(p):
	print(Back.YELLOW)
	print("Характеристики героя")
	print()
	print("---")
	print("Здоровье: " + str('{:.1f}'.format(p.hp)) + "/" + str('{:.1f}'.format(p.max_hp)))
	print("Мана: " + str('{:.1f}'.format(p.mana)) + "/" + str('{:.1f}'.format(p.max_mana)))
	print("Сила: {}".format(p.pw))
	print("Опыт: {}/{}".format(p.xp, p.max_xp))
	print("Уровень: {}".format(p.lvl))
	print()
	print("Изученные заклинания:")
	print()
	print()
	if s.fbsLevel >= 1:
		print("Огненный шар ({} уровень)\n".format(s.fbsLevel))
		print("При использовании потребляет " + Fore.CYAN + str('{:.1f}'.format(s.fbsManaCost)) + Fore.BLACK +  " маны и наносит " + Fore.RED + str('{:.1f}'.format(s.fbsDamage)) + Fore.BLACK + " урона врагу")
		print()
		print()
	if s.hsLevel >= 1:
		print("Лечение ({} уровень)\n".format(s.hsLevel))
		print("При использовании потребляет " + Fore.CYAN + str('{:.1f}'.format(s.hsManaCost)) + Fore.BLACK + " маны и лечит " + Fore.RED + str('{:.1f}'.format(s.hsHeal)) + Fore.BLACK + " здоровья)")
		print()
		print()
	print(Back.YELLOW + "---")
	print(Back.CYAN)

# Главный экран
def menu_main(p):
	while True:
		print(Back.CYAN)
		print("Вперёд")
		print()
		print()
		print("Параметры")
		print()
		print()
		print("Прокачка")
		print()
		print()
		print("Инвентарь")
		print()
		print()
		print("Заклинания")
		print()
		print()
		print("---")
		print()
		print()
		print("Настройки")
		print()
		print()
		print()
		n = input("Действие: ")
		if n == "Вперёд":
			menu_fight(p)
		if n == "Параметры":
			menu_stats(p)
		if n == "Прокачка":
			menu_upgrade(p)
		if n == "Инвентарь":
			menu_inventory(p)
		if n == "Заклинания":
			menu_skills(s)
		if n == "Настройки":
			menu_settings()
			
 
# Бой
def menu_fight(p):
	if p.lvl >= 0:
		e.hp = 2 * randint(1, 3)
		e.pw = 2 * randint(1, 2)
	elif p.lvl >= 3:
		e.hp = 2 * randint(4, 6)
		e.pw = 2 * randint(1, 4)
	elif p.lvl >= 5:
		e.hp = 2 * randint(5, 8)
		e.pw = 2 * randint(2, 6)
	while e.hp > 0:
		print(Back.WHITE)
		print(Back.WHITE + "---")
		print(Back.RED)
		print("Враг: ЗДОРОВЬЕ {}, СИЛА {}".format(e.hp, e.pw))
		print(Back.MAGENTA)
		print("Ты: ЗДОРОВЬЕ " + str('{:.1f}'.format(p.hp)) + "/" + str('{:.1f}'.format(p.max_hp)) + ", СИЛА " + str('{:.1f}'.format(p.pw)) + ", МАНА " + str('{:.1f}'.format(p.mana)) + "/" + str('{:.1f}'.format(p.max_mana)))
		print(Back.WHITE)
		print(Back.WHITE + "---" + Back.CYAN)
		print()
		print("Ударить (нанесёт " + "{}".format(p.pw) + " урона)")
		print()
		print("Сбежать")
		print()
		print("Инвентарь")
		print()
		print("Заклинания")
		print()
		print("Параметры")
		print()
		print(Back.WHITE + "---" + Back.CYAN)
		print()
		n = input("Действие: ")
		print(Back.WHITE + "---")
		# parameter_condition()
		if n == "Ударить":
			if p.mana < p.max_mana:
				p.mana += 1
			r = randint(1, 2)
			if r == 1:
				sound_punch()
				e.hp -= p.pw
				print(Back.YELLOW + "Вы нанесли врагу " + Back.RED +  "{}".format(p.pw) + Back.YELLOW + " урона!")
				print(Back.WHITE + "---")
				print()
			if r == 2:
				p.hp -= e.pw
				print(Back.YELLOW + "Враг нанес вам " + Back.RED +  "{}".format(e.pw) + Back.YELLOW + " урона!")
				print(Back.WHITE + "---")
				print()
				if p.hp <= 0:
					menu_dead(p)
		elif n == "Сбежать":
			if p.mana < p.max_mana:
				p.mana += 1
			r = randint(1, 2)
			if r == 2:
				print()
				print("Вы удачно сбежали!")
				print()
				print("---")
				menu_main(p)
			if r == 1:
				p.hp -= e.pw
				print()
				print("У вас не получилось сбежать.")
				print("Враг нанёс вам {} урона".format(e.pw))
				print()
				print("---")
				if p.hp <= 0:
					menu_dead(p)

		elif n == "Инвентарь":
			menu_inventory(p)
		elif n == "Заклинания":
			menu_skillsfight(p)
		elif n == "Параметры":
			menu_stats(p)
		else:
			print()
			print(Back.RED + Fore.GREEN +"Неверное действие!" + Back.CYAN + Fore.BLACK)
	
	print(Back.GREEN)
	sound_win()
	print("Вы победили врага!")
	print("---")
	print(Back.CYAN)
	p.xp += 5
	r = randint(1, 5)
	if r == 1:
		print("В этом бою вы заработали зелье лечения!")
		print()
		print()
		i.health_potion += 1
	if r == 2:
		print("В этом бою вы ничего не заработали.")
		print()
		print()
	if r == 3:
		print("В этом бою ты заработал зелье маны!")
		print()
		print()
		i.mana_potion += 1
	if r == 4:
		print("В этом бою вы ничего не заработали.")
		print()
		print()
	if r == 5:
		print("В этом бою вы заработали свиток!")
		print()
		print()
		i.scroll += 1

	if p.xp >= p.max_xp:
		menu_lvlup(p)

# Смерть
def menu_dead(p):
		print(Back.RED)
		print("Вы погибли! Начать игру заново?")
		print("---")
		print("Да")
		print("Нет")
		print("---")
		n = input("Действие: ")

		if n == "Да":

			menu_class()

		elif n == "Нет":
			sys.exit()
		else: 
			print(Back.RED + Fore.GREEN +"Неверное действие!" + Back.CYAN + Fore.BLACK)
			menu_dead(p)

# Использование скиллов
def menu_skillsfight(p):
	print("Выберите скилл")
	if s.fbsLevel >= 1:
		print(Back.YELLOW + "Огненный шар ({} лвл)".format(s.fbsLevel) + Back.CYAN)
	if s.hsLevel >= 1:
		print(Back.YELLOW + "Лечение ({} лвл)".format(s.hsLevel) + Back.CYAN)

	n = input("Действие: ")

	if n == "Огненный шар" and s.fbsLevel >= 1 and p.mana >= s.fbsManaCost:		
		e.hp -= s.fbsDamage
		r = randint(1, 3)
		if r == 1:
			p.hp -= e.pw
			print("Враг нанёс вам {} урона!".format(e.pw))
		p.mana -= s.fbsManaCost

	elif n == "Огненный шар" and s.fbsLevel >= 1 and p.mana < s.fbsManaCost:		
		print()
		print(Back.RED + Fore.WHITE + "Недостаточно маны!" + Back.CYAN + Fore.BLACK)

	if n == "Лечение" and s.hsLevel >= 1 and p.mana >= s.hsManaCost:
		p.hp += s.hsHeal
		p.mana -= s.hsManaCost
	elif n == "Лечение" and s.hsLevel >= 1 and p.mana < s.hsManaCost:	
		print()	
		print(Back.RED + Fore.WHITE + "Недостаточно маны!" + Back.CYAN + Fore.BLACK)

	if p.hp > p.max_hp:
		p.hp = p.max_hp

# Прокачка скиллов
def menu_skills(s):
	print()
	print(Back.YELLOW + "---")
	print()
	print("У вас " + Back.RED + Fore.WHITE + "{}".format(i.scroll) + Back.YELLOW + Fore.BLACK + " свитков")
	print()
	print("Что прокачать?")
	print()
	print(Back.RED + Fore.WHITE)
	print("Огненный шар ({} уровень)".format(s.fbsLevel))
	print()
	print("Лечение({} уровень)".format(s.hsLevel))
	print(Back.CYAN + Fore.BLACK)
	print(Fore.WHITE + "Напишите " + Back.WHITE + Fore.BLACK +"Назад" + Back.CYAN + Fore.WHITE + " чтобы вернуться назад" + Fore.BLACK)

	n = input("Действие: ")

	if n == "Огненный шар" and i.scroll > 0:
		print("Вы успешно прокачали скилл " + Fore.RED + Back.WHITE +"Огненный Шар" + Fore.BLACK + Back.CYAN +"!")
		s.fbsLevel += 1
		s.fbsDamage *= 1.5
		s.fbsManaCost *= 1.2
		i.scroll -= 1
		menu_skills(s)

	if n == "Огненный шар" and i.scroll <= 0:
		print("У вас недостаточно свитков!")
		menu_skills(s)

	if n == "Лечение" and i.scroll > 0:
		print("Вы успешно прокачали скилл " + Fore.GREEN + Back.WHITE + "Лечение" + Fore.BLACK + Back.CYAN + "!")
		s.hsLevel += 1
		s.hsHeal *= 1.2
		s.hsManaCost *= 1.2
		i.scroll -= 1
		menu_skills(s)

	if n == "Лечение" and i.scroll <= 0:
		print("У вас недостаточно свитков!")
		menu_skills(s)

	if n == "Назад":
		menu_main(p)

	else: 
		print()
		print(Fore.WHITE + Back.RED + "Такого заклинания нет!" + Fore.BLACK + Back.CYAN)
		menu_skills(s)

# Повышение уровня
def menu_lvlup(p):
	print("Ваш уровень повысился на 1!")
	p.hp = p.max_hp
	p.sp += 2
	p.xp = 0
	p.max_xp += 5
	p.lvl += 1

# Инвентарь
def menu_inventory(p):
	print("Что использовать?")


	if i.health_potion > 0:
		print(Back.YELLOW + "Зелье лечения x{}".format(i.health_potion) + Back.CYAN)
	if i.mana_potion > 0:
		print(Back.YELLOW + "Зелье маны x{}".format(i.mana_potion) + Back.CYAN)
	if i.scroll > 0:
		print(Back.YELLOW + "Свиток x{}".format(i.scroll) + Back.CYAN)

	print(Fore.WHITE + "Нажмите ENTER чтобы вернуться назад" + Fore.BLACK)

	n = input("Действие: ")

	if n == "Зелье лечения" and i.health_potion > 0 and p.hp == p.max_hp:
		i.health_potion -= 1
		menu_inventory(p)
	elif n == "Зелье лечения" and i.health_potion > 0:
		p.hp += 3
		i.health_potion -= 1
		menu_inventory(p)
	if n == "Зелье маны" and i.mana_potion > 0 and i.mana_potion == p.max_mana:
		i.mana_potion -= 1
		menu_inventory(p)
	elif n == "Зелье маны" and i.mana_potion > 0:
		p.mana += 4
		i.mana_potion -= 1
		menu_inventory(p)
	if n == "Свиток" and i.scroll > 0:
		# parameter_condition()
		menu_skills(s)

# Меню настройки

def menu_settings():
	print()
	print("Информация")

	print()
	n = input("Действие: ")

	if n == "Информация":
			print()
			print()
			print(Back.BLACK + Fore.WHITE +"Вся информация здесь: " + Fore.BLACK + Back.WHITE + "https://ronin-text-quest.fandom.com/ru/f" + Back.CYAN + Fore.BLACK)
			print()
			menu_settings()

# Выбор класса

def menu_class():
	while True:
		print(Back.CYAN)
		print("Выберите ваш класс")
		print()
		print()
		print("Воин")
		print()
		print()
		print("Маг")
		print()
		print()
		print()
		n = input("Действие: ")
		if n == "Воин":
			p.hp = 8
			p.max_hp = 8
			p.mana = 20
			p.max_mana = 20
			p.pw = 6
			i.health_potion = 5
			i.mana_potion = 5
			i.scroll = 3
			menu_main(p)
		if n == "Маг":
			p.mana = 8
			p.max_mana = 8
			i.scroll = 1
			i.health_potion = 2
			menu_main(p)

menu_class()

