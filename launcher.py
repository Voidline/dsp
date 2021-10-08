from main import fft, upload, mat


def menu():
    while True:
        try:
            index = int(input("1 - Задать параметры сигнала\n"
                              "2 - Провести анализ сохраненных данных\n"
                              "3 - Открыть из .mat файла\n"
                              "0 - Закрыть программу\n  >> "))
            if index == 1:
                w = [int(input(f"Частота ({i + 1}/2): ")) for i in range(2)]
                fft(w[0], w[1])
            if index == 2:
                upload()
            if index == 3:
                mat()
            if index == 0:
                break
        except:
            print("\nНеверные данные\n")


if __name__ == "__main__":
    menu()
