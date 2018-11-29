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
    def __init__(self, center, width, iterations):
        self.iterations = iterations
        self._coordinates = Fractal.createCoordinateMatrix(center, width)
        self._results = None

    @staticmethod
    def createCoordinateMatrix(center, width):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(complex)
        interval = np.abs(width * 2) / (RESOLUTION - 1)

        pixels_from_center = (RESOLUTION - 1) / 2

        print(center)
        print(center.imag, center.real)

        top = np.abs(center.imag + interval * pixels_from_center)
        left = center.real - interval * pixels_from_center

        print(top, left)

        def generateMatrix():
            for row in range(RESOLUTION):
                if row % 100 == 0:
                    print(row)
                yield [((top - interval * row) * 1j +
                    (left + interval * col)) for col in range(RESOLUTION)]

        return generateMatrix()

    # creates magnitude graph from coordinate matrix
    def create(self, verbose=False):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(float)

        for row in range(RESOLUTION):
            for column in range(RESOLUTION):
                temp_matrix[row][column] = np.abs(self._coordinates[row][column]).real

        if verbose == True:
            print(temp_matrix)

        self._results = temp_matrix

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
    def __init__(self, center, width, iterations, c):
        self.c = c
        super().__init__(center, width, iterations)

    def create(self, verbose=False):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(float)
        
        print("------------------------")
        print("Creating fractal...")
        print("------------------------")

        row_index = 0
        col_index = 0
        for row in self._coordinates:
            for z in row:
                temp_number = z
                for i in range(self.iterations):
                    temp_number = temp_number ** 2 + c
                    if np.abs(temp_number).real > THRESHOLD:
                        break
                temp_matrix[row_index][col_index] = np.abs(temp_number).real
                col_index += 1
            col_index = 0
            row_index += 1

        if verbose == True:
            print(temp_matrix)

        self._results = temp_matrix

class Mandelbrot(Fractal):
    def __init__(self, center, width, iterations):
        super().__init__(center, width, iterations)

    def create(self, verbose=False):
        temp_matrix = np.zeros((RESOLUTION, RESOLUTION)).astype(float)

        print("------------------------")
        print("Creating fractal...")
        print("------------------------")

        row_index = 0
        col_index = 0
        for row in self._coordinates:
            for c in row:
                temp_number = 0
                for i in range(self.iterations):
                    temp_number = temp_number ** 2 + c
                    if np.abs(temp_number).real > THRESHOLD:
                        break
                temp_matrix[row_index][col_index] = np.abs(temp_number).real
                col_index += 1
            col_index = 0
            row_index += 1

        if verbose == True:
            print(temp_matrix)

        self._results = temp_matrix


def takeFirstInput():
    if len(sys.argv) == 1:
        center = complex(input("Center? "))
        width = float(input("Width? "))
        iterations = int(input("Iterations? "))
        return (center, width, iterations)
    else:
        arguments = sys.argv.copy()
        arguments.pop(0)
        return tuple(arguments)

if __name__ == "__main__":
    selection = int(input("1: Julia, 2: Mandelbrot: "))
    if not (selection == 1 or selection == 2):
        raise ValueError("Incorrect value")
    elif selection == 1:
        c = complex(input("c? "))
    while 1:
        if selection == 1:
            first_fractal = Julia(*takeFirstInput(), c)
        else:
            first_fractal = Mandelbrot(*takeFirstInput())
        first_fractal.create(verbose=False)
        first_fractal.show(continuous=True)
        input("Zoom in?")
