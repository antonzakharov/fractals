#!/usr/bin/env python3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sys

RESOLUTION = 1001
SCALE = 1
THRESHOLD = 2

class Fractal:
    def __init__(self, center, width, iterations, discrete=False, interior_shading=True):
        self.iterations = iterations
        self._coordinates = Fractal.createCoordinateMatrix(center, width)
        self._results = None
        self._discrete = discrete
        self._interior_shading = interior_shading

    @staticmethod
    def createCoordinateMatrix(center, width):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(complex)
        interval = np.abs(width * 2) / (RESOLUTION - 1)

        pixels_from_center = (RESOLUTION - 1) / 2

        print(center)

        top = np.abs(center.imag + interval * pixels_from_center)
        left = center.real - interval * pixels_from_center

        print("------------------------")
        print("Creating fractal...")
        print("------------------------")

        def generateMatrix():
            for row in range(RESOLUTION):
                if row != 0 and row % (RESOLUTION - 1) == 0:
                    print("100%")
                elif row % 100 == 0:
                    print("{}%".format(int((row / RESOLUTION) * 100)))
                yield [((top - interval * row) * 1j +
                    (left + interval * col)) for col in range(RESOLUTION)]

        return generateMatrix()

    # creates magnitude graph from coordinate matrix
    def create(self, verbose=False):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(float)

        row_index = 0
        col_index = 0
        for row in self._coordinates:
            for col in row:
                temp_matrix[row_index][col_index] = np.abs(self.calculate(col))
                col_index += 1
            col_index = 0
            row_index += 1

        if verbose == True:
            print(temp_matrix)

        self._results = temp_matrix

    def calculate(self, number):
        temp_number = number
        total_iterations = 0
        if self._discrete:
            for i in range(self.iterations):
                temp_number = self.fractal_func(temp_number, number)
                if np.abs(temp_number).real > THRESHOLD:
                    break
                else:
                    total_iterations += 1
            return (total_iterations % 20) / 20 
        else:
            for i in range(self.iterations):
                temp_number = self.fractal_func(temp_number, number)
                if np.abs(temp_number).real > THRESHOLD:
                    break
            return np.abs(temp_number).real

    def fractal_func(self, z, c):
        return z

    def show(self, continuous=False, colormap="twilight"):
        if self._results is None:
            raise ValueError("No fractal defined.")
        results = self._results
        results *= SCALE
        if continuous:
            results = np.mod(results, 1)
        im = Image.fromarray(np.uint8(getattr(cm, colormap)(results)*255))
        im.show()
        return

class Julia(Fractal):
    def __init__(self, center, width, iterations, c, discrete=False, interior_shading=True):
        self.c = c
        super().__init__(center, width, iterations, discrete, interior_shading)

    def fractal_func(self, z, c):
        return z ** 2 + self.c

class Mandelbrot(Fractal):
    def __init__(self, center, width, iterations, discrete=False, interior_shading=True):
        super().__init__(center, width, iterations, discrete, interior_shading)

    def fractal_func(self, z, c):
        return z ** 2 + c


def takeFirstInput():
    center = complex(input("Center? "))
    width = float(input("Width? "))
    iterations = int(input("Iterations? "))
    return (center, width, iterations)

if __name__ == "__main__":
    color = "gnuplot"
    discrete = True
    
    selection = int(input("1: Julia, 2: Mandelbrot: "))
    if not (selection == 1 or selection == 2):
        raise ValueError("Incorrect value")
    elif selection == 1:
        c = complex(input("c? "))
    while 1:
        if selection == 1:
            first_fractal = Julia(*takeFirstInput(), c, discrete=discrete)
        else:
            first_fractal = Mandelbrot(*takeFirstInput(), discrete=discrete)
        first_fractal.create(verbose=False)
        first_fractal.show(continuous=True, colormap=color)
        print("------------------------")
        input("Zoom in?")
        print("------------------------")
