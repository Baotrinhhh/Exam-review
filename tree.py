import tkinter as tk
from math import sin, cos, pi
import random

class RandomTree:
    def __init__(self, root, width=500, height=500, flower_radius=1.5):
        self.root = root
        self.width = width
        self.height = height
        self.flower_radius = flower_radius

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#F0F8FF")
        self.canvas.pack()

        # Bind space key to redraw
        self.root.bind("<space>", self.draw)

        # Initial draw
        self.draw(None)

    def draw_branch(self, start_pos, branch_width, branch_length, angle):
        if branch_width < 1:
            # Draw a leaf as a small circle
            self.canvas.create_oval(
                start_pos[0] - self.flower_radius,
                start_pos[1] - self.flower_radius,
                start_pos[0] + self.flower_radius,
                start_pos[1] + self.flower_radius,
                fill="white", outline="white"
            )
            return

        # Randomly decide not to draw smaller branches
        if branch_width < 5 and random.random() < 0.3:
            return

        # Calculate the end position of the branch
        end_pos = (
            start_pos[0] + branch_length * cos((angle * pi) / 180),
            start_pos[1] + branch_length * sin((angle * pi) / 180)
        )

        # Draw the branch
        self.canvas.create_line(
            start_pos[0], start_pos[1],
            end_pos[0], end_pos[1],
            fill="#333", width=branch_width, capstyle=tk.ROUND
        )

        # Recursively draw the left and right branches
        self.draw_branch(end_pos, branch_width * 0.8, branch_length * 0.8, angle + random.randint(0, 30))
        self.draw_branch(end_pos, branch_width * 0.8, branch_length * 0.8, angle - random.randint(0, 30))

    def draw(self, event):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the initial tree structure
        self.draw_branch((0, 0), 10, 100, 90)

        # Center the tree on the canvas
        self.canvas.move("all", self.width / 2, self.height)

        # Flip the y-axis (so the tree grows upwards)
        self.canvas.scale("all", self.width / 2, self.height, 1, -1)

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Random Tree")

    # Create and start the tree drawer
    tree_drawer = RandomTree(root)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
