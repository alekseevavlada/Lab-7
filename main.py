# Алексеева Влада 367801
import numpy as np
import random
from time import perf_counter
import pandas as pd
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

file = pd.read_csv('data1.csv', encoding='cp1251', delimiter=';')
time = file['Время']
dross = file['Положение дроссельной заслонки (%)']
o = file['Обороты двигателя (об/мин)']


def graph():

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-10, 50])
    ax.set_ylim([-2, 1000])
    ax.set_title('Мой график matplotlib')
    ax.set_xlabel('Время')
    ax.set_ylabel('Положение дроссельной заслонки (%);Обороты двигателя (об/мин)')
    plt.plot(time, dross)
    plt.plot(time, o)
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
    zs = np.tan(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='*', c='pink')
    plt.title('3D  график')
    plt.show()

start()
graph()
plot3d()
