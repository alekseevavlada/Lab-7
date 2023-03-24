# Алексеева Влада 367801
import numpy as np
import random
import pandas as pd
from time import perf_counter
import matplotlib.pyplot as plt

# Task 1


def start():
    array_1 = []
    for i in range(1000000):
        array_1.append(random.random())
    array_2 = []
    for i in range(1000000):
        array_2.append(random.random())

    start_time = perf_counter()

    time_now = perf_counter() - start_time
    print(time_now)

    time_now = perf_counter()
    array_1 = np.random.rand(1000000)
    array_2 = np.random.rand(1000000)
    end = np.multiply(array_1, array_2)
    print('Итог:', perf_counter() - time_now)


# Task 2

x_1 = 'Положение дроссельной заслонки (%)'
y_2 = 'Обороты двигателя (об/мин)'


def graph():

    time = []
    dross = []
    o = []
    with open('data1.csv', 'r') as f:
        for row in f:
            time.append(row['Время'])
            o.append(float(row[x_1]))
            dross.append(float(row[y_2]))
        f.close()

    time = np.array(time, float)
    dross = np.array(dross, float)
    o = np.array(o, float)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-2, 2])
    ax.set_title('Мой график matplotlib')
    ax.set_xlabel('Время')
    ax.set_ylabel('Положение дроссельной заслонки (%);Обороты двигателя (об/мин)')
    plt.plot(np.array(time), np.array(dross))
    plt.plot(np.array(time), np.array(o))
    plt.show()

    plt.title('График корреляции')
    plt.xlabel('Положение дроссельной заслонки (%)')
    plt.ylabel('Обороты двигателя (об/мин)')
    plt.plot(dross, o, 'o')
    plt.show()


# Task 3


def plot3d():
    np.random.seed(40)
    xs = np.linspace(-1*np.pi, 1*np.pi, 100)
    ys = xs
    zs = np.tg(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='*', c='pink')
    plt.title('3D  график')
    plt.show()

