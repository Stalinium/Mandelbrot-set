import matplotlib.pyplot as plt
import numpy as np

class ComplexNumber:

    def __init__(self, real, imaginary):

        self.real = real
        self.imaginary = imaginary

    def add(self, cn):

        self.real += cn.real
        self.imaginary += cn.imaginary
        

    def square(self):

        return ComplexNumber(self.real * self.real - 1 * self.imaginary * self.imaginary, 2 * self.real * self.imaginary)

    def __str__(self):

        return "(" + str(self.real) + " + " + str(self.imaginary) + "i)"


start = (-1.5, 1.5)
end = (0.5, -1.5)
detail = 1000
steps = ((end[0] - start[0]) / detail, (end[1] - start[1]) / detail)

arr = np.zeros((detail, detail))


for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):

        cn = ComplexNumber(0, 0)
        cn2 = ComplexNumber(start[0] + x * steps[0], start[1] + y * steps[1])

        for x2 in range(0, 16):

            cn.add(cn2)
            cn = cn.square()

            if cn.real * cn.real + cn.imaginary * cn.imaginary > 4:
                arr[x][y] = 1
                break

    print(str((x / arr.shape[0]) * 100) + " %")

plt.imshow(arr)
plt.show()
