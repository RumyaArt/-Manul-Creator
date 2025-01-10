import os
import shutil

def replace_dots_in_folder_names(directory):
    """
    Заменяет точки на нижние подчёркивания во всех названиях папок в указанной директории.

    Args:
        directory (str): Путь к директории, в которой нужно переименовать папки.
    """
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if "." in dir_name:
                old_path = os.path.join(root, dir_name)
                new_name = dir_name.replace(".", "_")
                new_path = os.path.join(root, new_name)
                try:
                    shutil.move(old_path, new_path)
                    print(f"Переименовано: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Ошибка при переименовании {old_path}: {e}")

if __name__ == "__main__":
    target_directory = input("Введите путь к директории: ")

    if not os.path.isdir(target_directory):
        print("Указанный путь не является директорией.")
    else:
        replace_dots_in_folder_names(target_directory)
        print("Операция завершена.")
