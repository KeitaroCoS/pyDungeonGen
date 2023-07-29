#!/usr/bin/python3

import tcod
import random

def Generate_Rooms(roomQuantity, roomMaxSizeX, roomMaxSizeY, consoleWidth, consoleHeight):
	console = [['•'] * consoleWidth for y in range(consoleHeight)]
	rooms = []

	for room in range(roomQuantity):
		roomCenterX = random.randint(0, consoleWidth - 1)
		roomCenterY = random.randint(0, consoleHeight - 1)
		roomRandSizeX = random.randint(1, roomMaxSizeX)
		roomRandSizeY = random.randint(1, roomMaxSizeY)
		print(roomCenterX, roomCenterY)

		roomData = {'x':roomCenterX, 'y':roomCenterY, 'width':roomRandSizeX, 'height':roomRandSizeY}
		rooms.append(roomData)

		console[roomCenterY][roomCenterX] = '@'

	for row in console:
		print(''.join(row))


roomQuantity = 10
roomMaxSizeX = 10
roomMaxSizeY = 10
consoleWidth = 50
consoleHeight = 25

Generate_Rooms(roomQuantity, roomMaxSizeX, roomMaxSizeY, consoleWidth, consoleHeight)