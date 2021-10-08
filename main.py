import random
import json
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy.io

def peak(yf):
    peaks = list()
    size = len(yf)
    for i in range(size):
        if i + 1 < size:
            if yf[i + 1] < yf[i] and yf[i] > 0.25:
                peaks.append(i * 2)
    return peaks


def fft(hz1, hz2):
    N = 500
    T = 1 / 1000

    x = np.linspace(0.0, 0.5, 1000)
    x += [random.randint(0, 1) / 1000 for i in range(1000)]
    y = np.sin(hz1 * 2.0 * np.pi * x) + 0.5 * np.sin(hz2 * 2.0 * np.pi * x)

    yf = scipy.fftpack.fft(y)
    yf = 2.0 / N * np.abs(yf[:N // 2])
    xf = np.linspace(0.0, 1.0 / (2.0 * T), int(N / 2))
    peaks = peak(yf)
    s = {
        "signal": {
            "y": dict(enumerate(y)),
            "x": dict(enumerate(x))
        },
        "specter": {
            "yf": dict(enumerate(yf)),
            "xf": dict(enumerate(xf))
        },
        "peaks": {
            "1": peaks[0],
            "2": peaks[-1]
        }
    }

    with open(r"data.json", "w") as file:
        json.dump(dict(s), file, indent=2)

    fig, axs = plt.subplots(2, 1)
    color = 'green'
    axs[0].plot(x, y, color)
    axs[1].plot(xf, yf, color)

    axs[0].set(xlabel="Время, мс", ylabel="Амплитуда", title=f"Частоты: {hz1}, {hz2} Гц")
    axs[1].set(xlabel="Частота, Гц", title=f"Частоти {hz1}, {hz2} Гц")
    for ax in axs.flat:
        ax.grid(color="black")
        ax.minorticks_on()
    fig.suptitle(f"Данные сохранены в data.json", fontweight="bold")
    fig.set_figwidth(8)
    fig.set_figheight(12)
    plt.show()


def upload():
    with open(r"data.json", "r") as file:
        data = json.load(file)
        y = data['signal']['y']
        x = data['signal']['x']
        yf = data['specter']['yf']
        xf = data['specter']['xf']
        p1 = data['peaks']['1']
        p2 = data['peaks']['2']

    fig, axs = plt.subplots(2, 1)
    color = 'green'
    axs[0].plot(xf.values(), yf.values(), color)
    axs[1].plot(x.values(), y.values(), color)
    csfont = {'size': 13}
    axs[1].set(xlabel="Время, мс", ylabel="Амплитуда")
    axs[1].set_title(f"sin(2∙π∙{p1}∙t) + sin(2∙π∙{p2}∙t)",
                     fontproperties=csfont, fontname='Calibri')
    axs[0].set(xlabel="Частота, Гц", title=f"Возможные частоты: {p1}, {p2} Гц")

    for ax in axs.flat:
        ax.grid(color="black")
        ax.minorticks_on()

    fig.suptitle(f"Данные загружены из data.json", fontweight="bold")

    fig.set_figwidth(8)
    fig.set_figheight(12)
    plt.show()

def mat():
    N = 500
    T = 1 / 1000

    y = scipy.io.loadmat(r"variant_Lab1_10.mat")['y'][0]
    x = scipy.io.loadmat(r"variant_Lab1_10.mat")['t'][0]
    yf = scipy.fftpack.fft(y)
    yf = 2.0 / N * np.abs(yf[:N // 2])
    xf = np.linspace(0.0, 1.0 / (2.0 * T), int(N / 2))
    fig, axs = plt.subplots(2, 1)
    color = 'green'
    axs[0].plot(x, y, color)
    axs[1].plot(xf, yf, color)
    peaks = peak(yf)

    csfont = {'family': 'cursive',
              'size': 14}
    axs[1].set(xlabel="Время, мс", ylabel="Амплитуда")
    axs[1].set_title(f"sin(2∙π∙{peaks[0]}∙t) + sin(2∙π∙{peaks[int(len(peaks)/2)]}∙t) + sin(2∙π∙{peaks[-1]}∙t)",
                     fontproperties=csfont, fontname='Calibri')
    axs[0].set(xlabel="Частота, Гц", title=f"Возможные частоты: {peaks[0]}, {peaks[int(len(peaks)/2)]},  {peaks[-1]}  Гц")
    for ax in axs.flat:
        ax.grid(color="black")
        ax.minorticks_on()
    fig.set_figwidth(8)
    fig.set_figheight(12)
    plt.show()