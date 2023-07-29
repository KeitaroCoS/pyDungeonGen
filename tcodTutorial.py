import tcod.context

def main():
	screenHeight = 50
	screenWidth = 80

	player_x = int(screenWidth / 2)
	player_y = int(screenHeight / 2)

	tileset = tcod.tileset.load_tilesheet("data/10x10Tileset.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

	with tcod.context.new_terminal(
		screenWidth,
		screenHeight,
		tileset = tileset,
		title = "TCOD Tutorial",
		vsync = True,
	) as context:
		root_console = tcod.console.Console(screenWidth, screenHeight, order = "F")
		while True:
			root_console.print(player_x, player_y, string = "@")

			context.present(root_console)

			for event in tcod.event.wait():
				if event.type == "QUIT":
					raise SystemExit()

if __name__ == "__main__":
	main()