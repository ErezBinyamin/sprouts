#!/usr/bin/python3.6m
import sys

gamestate={}

def init_game(n):
	for i in range(0,n):
		gamestate[i]=[None]

# Connect A to B
def connect_dots(a,b):
	if None in gamestate[a]:
		gamestate[a] = [ b ]
	elif 3 > len(gamestate[a]):
		gamestate[a].append(b)

def draw_line(route):
	a=route[0]
	b=route[len(route)-1]
	if not ((3 > len(gamestate[a])) and (3 > len(gamestate[b]))):
		return 1
	# Make new dot
	newDot=len(gamestate)
	gamestate[newDot]=[route[0],route[len(route)-1]]
	# Connect dots
	if 2==len(route):
		connect_dots(route[0], newDot)
		connect_dots(route[len(route)-1], newDot)

def print_game():
	print(gamestate)

def sprouts():
	init_game(2)
	print_game()
	draw_line([0,1])
	print_game()
	draw_line([0,1])
	print_game()
	draw_line([0,1])
	print_game()
	draw_line([3,4])
	print_game()

if __name__ == "__main__":
	sprouts()
