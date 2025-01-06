# Манул Криэтор

Короч основная идея довольно проста:

Есть Манул редактор, который Мана сделала в виде PSD файла (я его добавил репозиторий в папке 
[Исходники](https://github.com/RumyaArt/-Manul-Creator/tree/main/%D0%98%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8). Зайди и посмотри PSD файл). 

Прикол в том, что включая или выключая слои, ты можешь, например, добавлять элементы одежды.

С помощью заливки можешь менять цвет одежды, шёрстки и прочего. Для этого элементы разделены на основной цвет, обводку и дополнительные элементы.

Идея сайта точно такая же. Всё для удобство редактирования (в нашем случае заливки) разделено на слои (основной цвет, обводка и дополнительные элементы).

Реализация редактора будет с помощью HTML5 Canvas. 
Предполагается, что будут обязательне слои в виде глаз, рта, причёски, куртки, шатнов, под каждый из которых который будет выделен отдегый канвас. Возможно, даже под каждый слой обязательного для удобства заливки.
В центре будет манул сайта будет манул, сбоку флаги включая и выключа котрые ты можешь соотвественно убирать и добавлять элементы.

В папке [Манул_Креатор_Layers](https://github.com/RumyaArt/-Manul-Creator/tree/main/%D0%9C%D0%B0%D0%BD%D1%83%D0%BB_%D0%9A%D1%80%D0%B5%D0%B0%D1%82%D0%BE%D1%80_layers) 
нахядся уже экспортированные с помощью python скрипта [psdtopng2.py](https://github.com/RumyaArt/-Manul-Creator/blob/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D1%8B%20%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD/psdtopng2.py) png файлы 
(их пути и названия для удобства тоже немного подредактированы с помощью другого python скрипта и немного вручную).

В словаре [data.json](https://github.com/RumyaArt/-Manul-Creator/blob/main/data.json) основной ветки находятся пути внутри [Манул_Креатор_Layers](https://github.com/RumyaArt/-Manul-Creator/tree/main/%D0%9C%D0%B0%D0%BD%D1%83%D0%BB_%D0%9A%D1%80%D0%B5%D0%B0%D1%82%D0%BE%D1%80_layers). Этот json тоже генерируется python скриптом [jsonPy2.py](https://github.com/RumyaArt/-Manul-Creator/blob/main/jsonPy2.py).

В [index.html](https://github.com/RumyaArt/-Manul-Creator/blob/main/index.html) находится разметка сайта.

В [styles.css](https://github.com/RumyaArt/-Manul-Creator/blob/main/styles.css) CSS-стиль.

В [script.js](https://github.com/RumyaArt/-Manul-Creator/blob/main/script.js), логично, скрипт сайта.

[images](https://github.com/RumyaArt/-Manul-Creator/tree/main/images) пустая папка и пока никак не используется.

В [fonts](https://github.com/RumyaArt/-Manul-Creator/tree/main/fonts) я собираюсь хранить шрифты. Мб чё поменяется.

В [скрипты пайтон](https://github.com/RumyaArt/-Manul-Creator/tree/main/%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D1%8B%20%D0%BF%D0%B0%D0%B9%D1%82%D0%BE%D0%BD) находятся скрипты пайтон.
