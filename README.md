# Video to GIF Converter


Ця програма створює GIF з перших 20 кадрів відео.
Вона зменшує розмір кадрів до 320x240 і зберігає їх у GIF.

Щоб працювало, встанови бібліотеки:

pip install opencv-python pillow


Як користуватись:

Відкрий файл з кодом (наприклад, video-to-gif.py).

Внизу виклич функцію так:

video_frame_img(r"шлях_до_відео.mp4", "назва.gif")


Наприклад:

video_frame_img(r"C:\Users\USER\Downloads\example_video.mp4", "output.gif")


Програма збереже GIF і виведе повідомлення.
Якщо відео не відкриється або нема кадрів — буде помилка.

Кількість кадрів, розмір і швидкість GIF можна змінити в коді.
[![Open in Replit](https://replit.com/badge/github/yyvolovyk-1983-edu/video-to-gif)](https://replit.com/new/github/yyvolovyk-1983-edu/video-to-gif)

