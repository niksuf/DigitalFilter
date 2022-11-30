# Модель интегрирующей и дифференцирующей электрической цепи
## Описание проекта
Проект моделирует работу интегрирующей и дифференцирующей электрических цепей. Возможно теоретически проанализировать цепи с разным количеством отсчетов и разными постоянными времени.
## Интерфейс
![screenshot of interface](https://github.com/niksuf/DigitalFilter/blob/master/img/interface.png)

После ввода количества отсчетов, постоянной времени и выбора типа цепи следуюет нажать "Построить", после чего программа выведет в новом окне график с результатом исследований. После этого график можно приближать, отдалять, сохранить как *.png и др.

## Инструкция по запуску
1. Скачать репозиторий к себе на компьютер при помощи команды:
```
git clone https://github.com/niksuf/DigitalFilter
```
2. Установить расширение для Python (нужно для графического пользовательского интерфейса):
```
pip install PyQt5
```
3. Запустить приложение командой:
```
python DigitalFilter.py
```
