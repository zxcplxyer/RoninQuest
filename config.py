from random import randint


class Player:
	hp = 5 # здоровье
	mana = 5 # мана
	max_hp = 5 # максимальное здоровье
	max_mana = 5 # максимальная мана
	pw = 2 # сила(урон с руки)
	lvl = 0 # уровень
	sp = 5 # скилл поинт
	xp = 0 # опыт
	max_xp = 10 # максималный опыт
	if hp > max_hp:
		hp = max_hp
	if mana > max_mana:
		mana = max_mana

class Enemy:
		hp = 1
		pw = 1

class Items:
	health_potion = 0 # зелье здоровья
	mana_potion = 0 # зелье маны
	scroll = 0 # свиток магии

class Skills:
	
	# fireball
	fbsLevel = 0 # уровень заклинания "Огненный шар"
	fbsDamage = 3 # урон
	fbsManaCost = 4 # потребление маны за 1 использование
	
	# heal
	hsLevel = 0 # уровень заклинания "Лечение"
	hsHeal = 2 # лечение
	hsManaCost = 3 # # потребление маны за 1 использование
