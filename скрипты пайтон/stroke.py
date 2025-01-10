import os
import re

def rename_files(root_dir):
    """
    Переименовывает все файлы с названием "stroke_panel" в "stroke" в указанной директории.

    Args:
        root_dir: Путь к корневой директории, в которой нужно переименовать файлы.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == "stroke_panel":
                old_filepath = os.path.join(dirpath, filename)
                new_filepath = os.path.join(dirpath, "stroke")
                try:
                    os.rename(old_filepath, new_filepath)
                    print(f"Переименован файл: '{old_filepath}' -> '{new_filepath}'")
                except OSError as e:
                    print(f"Ошибка при переименовании '{old_filepath}': {e}")
            else:
                # Если в начале названия 'stroke_panel' то тоже переименовываем
                if filename.startswith("stroke_panel"):
                    old_filepath = os.path.join(dirpath, filename)
                    new_filename = filename.replace("stroke_panel", "stroke",1)
                    new_filepath = os.path.join(dirpath, new_filename)
                    try:
                        os.rename(old_filepath, new_filepath)
                        print(f"Переименован файл: '{old_filepath}' -> '{new_filepath}'")
                    except OSError as e:
                        print(f"Ошибка при переименовании '{old_filepath}': {e}")
                # Если в названии есть 'stroke_panel' то тоже переименовываем
                elif "stroke_panel" in filename:
                    old_filepath = os.path.join(dirpath, filename)
                    new_filename = filename.replace("stroke_panel", "stroke")
                    new_filepath = os.path.join(dirpath, new_filename)
                    try:
                        os.rename(old_filepath, new_filepath)
                        print(f"Переименован файл: '{old_filepath}' -> '{new_filepath}'")
                    except OSError as e:
                        print(f"Ошибка при переименовании '{old_filepath}': {e}")

if __name__ == "__main__":
    root_directory = 'Манул_Креатор_layers'
    if os.path.isdir(root_directory):
        rename_files(root_directory)
    else:
        print("Указанный путь не является директорией.")
