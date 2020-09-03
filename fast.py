import matplotlib.pyplot as plt
import numpy as np
import threading

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

depth = 64
arr = np.zeros((detail, detail))

def calc(args):

    for x in range(args[0], args[1]):
        for y in range(args[2], args[3]):

            cn = ComplexNumber(0, 0)
            cn2 = ComplexNumber(start[0] + x * steps[0], start[1] + y * steps[1])

            for x2 in range(0, depth):

                cn.add(cn2)
                cn = cn.square()

                if cn.real * cn.real + cn.imaginary * cn.imaginary > 4:
                    arr[y][x] = x2
                    break   

a = ( 0, int(arr.shape[0] / 2), 0, int(arr.shape[1] / 2))
b = ( int(arr.shape[0] / 2), arr.shape[0], 0 ,int(arr.shape[1] / 2))
thread1 = threading.Thread(target=calc, args=(a,  ))
thread2 = threading.Thread(target=calc, args=(b,  ))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

arr += np.flip(arr, 0)

plt.imshow(arr)
plt.show()
