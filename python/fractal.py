#!/usr/bin/env python3
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sys

RESOLUTION = 501
SCALE = 1
THRESHOLD = 2

class Fractal:
    def __init__(self, center, width, iterations, continuous, color, discrete=False, interior_shading=True):
        self.iterations = iterations
        self._coordinates = Fractal.createCoordinateMatrix(center, width)
        self._results = None
        self._discrete = discrete
        self._interior_shading = interior_shading
        self._continuous = continuous
        self._color = color

    @staticmethod
    def createCoordinateMatrix(center, width):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(complex)
        interval = np.abs(width * 2) / (RESOLUTION - 1)

        pixels_from_center = (RESOLUTION - 1) / 2

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
        for i in range(self.iterations):
            temp_number = self.fractal_func(temp_number, number)
            if np.abs(temp_number).real > THRESHOLD:
                break
            else:
                total_iterations += 1
        if self._interior_shading == True:
            if total_iterations == self.iterations:
                return 0
        if self._discrete == True:
            return total_iterations / (self.iterations)
        else:
            return np.abs(temp_number).real * (self.iterations - total_iterations)

    def fractal_func(self, z, c):
        return z

    def show(self):
        if self._results is None:
            raise ValueError("No fractal defined.")
        results = self._results
        results *= SCALE
        if self._continuous == True:
            results = np.mod(results, 1)
        else:
            results = np.log(results)
        im = Image.fromarray(np.uint8(getattr(cm, self._color)(results)*255))
        im.show()
        return

class Julia(Fractal):
    def __init__(self, center, width, iterations, c, continuous, color, discrete=False, interior_shading=True):
        self.c = c
        super().__init__(center, width, iterations, continuous, color, discrete, interior_shading)

    def fractal_func(self, z, c):
        return z ** 2 + self.c

class Mandelbrot(Fractal):
    def __init__(self, center, width, iterations, c, continuous, color, discrete=False, interior_shading=True):
        super().__init__(center, width, iterations, continuous, color, discrete, interior_shading)

    def fractal_func(self, z, c):
        return z ** 2 + c

def takeInitialInput():
    print("For the next couple of questions, type anything for 'yes' and type nothing for 'no'.")
    discrete = bool(input("Discrete shading? "))
    if discrete != True:
        interior_shading = bool(input("Interior shading? "))
        continuous = bool(input("Continuous colors? "))
        color = input("Color? ('grey' or 'gnuplot' are good choices): ")
        print("------------------------")
        return (discrete, interior_shading, continuous, color)
    color = input("Color? ('grey' or 'gnuplot' are good choices): ")
    print("------------------------")
    return (discrete, interior_shading)

def takeRecurringInput():
    center = complex(input("Center? "))
    width = float(input("Width? "))
    iterations = int(input("Iterations? "))
    return (center, width, iterations)

if __name__ == "__main__":
    initial_input = takeInitialInput()
    selection = int(input("1: Julia, 2: Mandelbrot: "))
    if not (selection == 1 or selection == 2):
        raise ValueError("Incorrect value")
    elif selection == 1:
        c = complex(input("c? "))
        hello
        hello
    while 1:
        if selection == 1:
            first_fractal = Julia(*takeRecurringInput(), c, *initial_input)
        else:
            first_fractal = Mandelbrot(*takeRecurringInput(), *initial_input)
            first_fractal.create(verbose=False)
            first_fractal.show()
            print("------------------------")
            input("Zoom in?")
            print("------------------------")
