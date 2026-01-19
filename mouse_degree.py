import pygame
import math
import serial
import time

# Replace 'COM9' with your actual port
arduino_port = '/dev/cu.usbserial-8010'
baud_rate = 115200

# Establish a serial connection with Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the connection to initialize

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Angle Calculator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Center of the screen
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Font setup
font = pygame.font.SysFont(None, 36)

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the difference between mouse and center
    dx = mouse_x - center_x
    dy = mouse_y - center_y

    # Calculate angle in radians using atan2(y, x)
    # Note: In pygame, y increases downwards
    angle_rad = math.atan2(dy, dx)

    # Convert to degrees
    angle_deg = math.degrees(angle_rad)

    # Convert to 0-180 range
    # This makes the top and bottom halves symmetric (0 at Right, 180 at Left)
    angle_deg = abs(angle_deg)
    ser.write(f"{angle_deg}\n".encode())
    # Drawing
    screen.fill(WHITE)

    # Draw a line from center to mouse
    pygame.draw.line(screen, RED, (center_x, center_y), (mouse_x, mouse_y), 2)
    
    # Draw the center point
    pygame.draw.circle(screen, BLUE, (center_x, center_y), 5)

    # Display the angle text
    text_surface = font.render(f"Angle: {angle_deg:.2f}°", True, BLACK)
    screen.blit(text_surface, (10, 10))
    
    # Display coordinates text
    coord_surface = font.render(f"Pos: ({mouse_x}, {mouse_y})", True, BLACK)
    screen.blit(coord_surface, (10, 50))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

pygame.quit()
