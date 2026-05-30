<div align="center">

# video-to-gif

**Конвертер відео в анімований GIF за допомогою OpenCV та Pillow**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/yyvolovyk-1983-edu/video-to-gif)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://github.com/yyvolovyk-1983-edu/video-to-gif)
[![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/yyvolovyk-1983-edu/video-to-gif)

</div>

---

## Як працює

```
відеофайл → OpenCV читає кадри → resize 320×240 → BGR→RGB → PIL Image → GIF
```

---

## Встановлення

```bash
git clone https://github.com/yyvolovyk-1983-edu/video-to-gif
cd video-to-gif
pip install opencv-python pillow
```

---

## Використання

```python
from video_to_gif import video_frame_img

video_frame_img(
    video_file="video.mp4",
    output_file="output.gif"
)
```

---

## Параметри

| Параметр | Тип | Опис |
|---|---|---|
| `video_file` | `str` | Шлях до вхідного відеофайлу |
| `output_file` | `str` | Ім'я вихідного GIF-файлу |

**Підтримувані формати:** MP4, AVI, MOV та інші формати OpenCV.

---

## Що робить скрипт

1. Відкриває відеофайл через `cv2.VideoCapture()`
2. Зчитує до **20 кадрів** послідовно
3. Змінює розмір кожного кадру до **320×240** пікселів
4. Конвертує колірний простір **BGR → RGB**
5. Перетворює кадр на `PIL Image`
6. Зберігає GIF з тривалістю **150 мс/кадр**, нескінченним повтором

---

## Структура

```
video-to-gif/
├── video_to_gif.py
├── example_video.mp4
└── README.md
```

---

## Залежності

```
opencv-python
pillow
```

---

<div align="center">

**Автор:** [Євген Воловик](https://github.com/yyvolovyk-1983-edu) · Харків, Україна
📧 y.y.volovyk@student.khai.edu · [LinkedIn](https://www.linkedin.com/in/yevhen-volovyk/)

</div>