import os
import shutil
from pathlib import Path


def move_images_to_folders(source_dir):
    """
    Переносит все изображения из указанной директории в папки,
    название которых совпадает с именем изображения.
    Сами изображения переименовываются в 'base'.

    Args:
        source_dir (str): Путь к директории с изображениями.
    """
    source_path = Path(source_dir)
    if not source_path.is_dir():
      print(f"Ошибка: Директория {source_dir} не существует")
      return

    for item in source_path.iterdir():
        if item.is_file() and item.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']: # можно добавить нужные расширения
            image_name_without_ext = item.stem  # Имя файла без расширения
            new_folder_path = source_path / image_name_without_ext  # Путь к новой папке

            # Создание новой папки, если ее нет
            new_folder_path.mkdir(exist_ok=True)

            # Перемещение и переименование файла
            new_image_path = new_folder_path / "base"
            #shutil.move(str(item), str(new_image_path) + item.suffix) #перемешение без расширения
            shutil.copy2(item, str(new_image_path) + item.suffix)  #копируем с сохранением метаданных
            print(f"Перемещено '{item.name}' в папку '{new_folder_path.name}'")
            item.unlink() #удаление оригинального файла


if __name__ == "__main__":
    while(True):
        target_directory = input("Введите путь к директории с изображениями: ")  # Получение пути из ввода
        move_images_to_folders(target_directory)
        print("Готово!")
