import os
from PIL import Image

def resize_image(image_path, max_width, max_height):
    """
    Изменяет размер изображения, сохраняя соотношение сторон и не превышая максимальную высоту и ширину.

    Args:
        image_path (str): Путь к изображению.
        max_width (int): Максимальная ширина.
        max_height (int): Максимальная высота.

    Returns:
        bool: True, если изменение размера прошло успешно, False - если произошла ошибка.
    """
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Ошибка при открытии {image_path}: {e}")
        return False

    original_width, original_height = img.size

    if original_width <= max_width and original_height <= max_height:
        print(f"Изображение {image_path} уже подходит под заданные размеры. Изменение не требуется.")
        return True
    print(f"Изменяем размер {image_path}...")

    # Определяем новый размер
    width_ratio = max_width / original_width
    height_ratio = max_height / original_height

    scale_ratio = min(width_ratio, height_ratio)
    new_width = int(original_width * scale_ratio)
    new_height = int(original_height * scale_ratio)

    # Изменяем размер
    try:
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)  # Используем LANCZOS для лучшего результата
        resized_img.save(image_path)  # Сохраняем изменения
        print(f"  Успешно изменен размер до {new_width}x{new_height}.")
        return True
    except Exception as e:
        print(f"  Ошибка при изменении размера {image_path}: {e}")
        return False

def process_directory(directory, max_width, max_height):
    """
    Обрабатывает все PNG изображения во всех поддиректориях указанной директории.

    Args:
        directory (str): Путь к директории с изображениями.
        max_width (int): Максимальная ширина.
        max_height (int): Максимальная высота.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(".png"):
                image_path = os.path.join(root, filename)
                resize_image(image_path, max_width, max_height)

if __name__ == "__main__":
    target_directory = "ROOT"  # Замените на путь к вашей директории
    max_image_width = 480     # Максимальная ширина в пикселях
    max_image_height = 480    # Максимальная высота в пикселях

    if not os.path.exists(target_directory):
       print("Ошибка: Указанная директория не существует")
    else:
       process_directory(target_directory, max_image_width, max_image_height)
       print("Завершено!")
