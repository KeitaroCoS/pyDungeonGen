import random

def generate_rooms(room_quantity, console_width, console_height, room_size_x, room_size_y):
    console = [[' '] * console_width for _ in range(console_height)]  # Initialize the console grid
    rooms = []  # List to store room coordinates and sizes

    for _ in range(room_quantity):
        # room_fits = False
        # while not room_fits:
        #     # Generate random starting point for the room
        start_x = random.randint(0, console_width - room_size_x - 1)
        start_y = random.randint(0, console_height - room_size_y - 1)

        #     # Check if the room overlaps with existing rooms
        #     overlap = False
        #     for room in rooms:
        #         if (start_x < room['x'] + room['width'] and start_x + room_size_x > room['x'] and
        #                 start_y < room['y'] + room['height'] and start_y + room_size_y > room['y']):
        #             overlap = True
        #             break

        #     if not overlap:
        #         room_fits = True

        # Add the room to the list
        room_data = {'x': start_x, 'y': start_y, 'width': room_size_x, 'height': room_size_y}
        rooms.append(room_data)

        # Draw the room's walls on the console grid
        for y in range(room_size_y):
            console[start_y + y][start_x] = '#'  # Left wall
            console[start_y + y][start_x + room_size_x - 1] = '#'  # Right wall
        for x in range(room_size_x):
            console[start_y][start_x + x] = '#'  # Top wall
            console[start_y + room_size_y - 1][start_x + x] = '#'  # Bottom wall

    # Print the console grid
    for row in console:
        print(''.join(row))

# Example usage
roomQuantity = 10
consoleWidth = 100
consoleHeight = 45
roomSizeX = 20
roomSizeY = 10

generate_rooms(roomQuantity, consoleWidth, consoleHeight, roomSizeX, roomSizeY)
