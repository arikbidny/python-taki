import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox
from client import GameClient

class TakiGameGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Taki Game')
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((0, 128, 128))
            pygame.display.flip()

        pygame.quit()


class TakiMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Taki Game Menu")

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

        self.root.mainloop()

    def start_game(self):
        messagebox.showinfo("Taki Game", "Welcome to the Taki Game!")
        self.root.destroy()
        client = GameClient()
        client.run()

if __name__ == "__main__":
    gui = TakiGameGUI()
    TakiMenu()
    gui.run()
