import pygame
from pygame.locals import *
import random

size = width, height = (500, 800)
road_w = int(width/1.6)
roadmark_w = int(width/50)
box_w, box_h = int(road_w/4.5), 100
enemybox_h = 100

pygame.init()
running = True
player_movable_Left = True
player_movable_Right = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Johannes' Box Game")
screen.fill((60,220,0))

player_x_loc = width/2 + road_w/9
player_y_loc = height*0.8
enemy_X_loc = width/2 - road_w/3
enemy_y_loc = height/100

score = 0

pygame.display.update()

while running:
	score += 1
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key in [K_a, K_LEFT]:
				if player_movable_Left and player.x != width/2 - road_w/3:
					player_movable_Right = True
					player_x_loc = width/2 - road_w/3
					player_movable_Left = False

					"""
					if player_x_loc <= int(width/2-road_w/2+roadmark_w*4):
						player_movable_Left = False
					"""

				#print(player.x)
				#pygame.display.update()

			if event.key in [K_d, K_RIGHT]:
				if player_movable_Right and player.x != width/2 + road_w/9:
					player_movable_Left = True
					player_x_loc = width/2 + road_w/9
					player_movable_Right = False

					"""
					if player_x_loc >= int((width/2+road_w/2-roadmark_w*4)-box_w):
						player_movable_Right = False
					"""

				#print(player.x)
				#pygame.display.update()

	pygame.draw.rect(screen, (50,50,50), (width/2-road_w/2, 0, road_w, height))
	pygame.draw.rect(screen, (255,240,60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
	pygame.draw.rect(screen, (255,255,255), (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
	pygame.draw.rect(screen, (255,255,255), (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))
	player = pygame.draw.rect(screen, (0,0,255), (player_x_loc, player_y_loc, box_w, box_h))
	#print(dir(player))
	player.x, player.y = player_x_loc, player_y_loc
	enemy = pygame.draw.rect(screen, (255,0,0), (enemy_X_loc, enemy_y_loc, box_w, enemybox_h))
	enemy.x, enemy.y = enemy_X_loc, enemy_y_loc
	#print(player.x)

	if score < 5000:
		enemy_y_loc = enemy.y + 1
	elif score >= 5000:
		enemy_y_loc = enemy.y + 3
	elif score > 10000:
		enemy_y_loc = enemy.y + 10

	left = width/2 - road_w/3
	right = width/2 + road_w/9
	lane = (right, left)
	enemy_height = (100, 200, 300)
	if enemy.y > height:
		enemy_X_loc = random.choice(lane)
		enemybox_h = random.choice(enemy_height)
		enemy_y_loc = enemy.y - int(height*1.5)

	if player.y == (enemy.y+enemybox_h) and player.x == enemy.x:
		print("Game Over! You no sabi drive.")
		break

	print(score)

	pygame.display.update()


pygame.quit()