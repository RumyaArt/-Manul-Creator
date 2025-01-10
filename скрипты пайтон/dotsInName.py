import os
import shutil

def rename_directories(root_dir):
    """
    Переименовывает все директории в указанной ветке, добавляя точку в начало их имени.

    Args:
        root_dir: Путь к корневой директории, с которой начинается переименование.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dir_name = "." + dirname  # Добавляем точку в начало имени
            new_dir_path = os.path.join(dirpath, new_dir_name)

            try:
                # Переименовываем только если папка не начинается с точки
                if not dirname.startswith('.'):
                  os.rename(old_dir_path, new_dir_path)
                  print(f"Переименована директория: '{old_dir_path}' -> '{new_dir_path}'")
                else:
                  print(f"Пропущена директория, уже начинается с точки: '{old_dir_path}'")
            except OSError as e:
                print(f"Ошибка при переименовании '{old_dir_path}': {e}")

if __name__ == "__main__":
    dr = 'Манул_Креатор_layers'
    listdr = os.listdir(dr)
    for dirc in listdr:
        root_directory = os.path.join(dr, dirc)
        if os.path.isdir(root_directory):
            rename_directories(root_directory)
        else:
            print("Указанный путь не является директорией.")
