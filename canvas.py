import numpy as np
from PIL import Image


class Canvas:
    """Object where all shapes are going to be drawn"""
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3D numpay array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, iamgepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(iamgepath)