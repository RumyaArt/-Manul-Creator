from psd_tools import PSDImage
from PIL import Image
import os

def sanitize_filename(filename):
    """Удаляет недопустимые символы из имени файла."""
    return "".join(c if c.isalnum() or c in " ._-()" else "_" for c in filename)

def export_layer(layer, output_folder, prefix="", canvas_size=(2048, 2048)):
    """
    Экспортирует слой или группу слоёв с учётом положения и размера.
    Если это папка, создаёт вложенную директорию.
    """
    layer_name = sanitize_filename(layer.name or "unnamed_layer")
    layer_path = os.path.join(output_folder, prefix, layer_name)

    if layer.is_group():
        os.makedirs(layer_path, exist_ok=True)
        for sublayer in layer:
            export_layer(sublayer, output_folder, os.path.join(prefix, layer_name), canvas_size)
    else:
        try:
            if layer.has_pixels():
                image = layer.topil()  # Извлекаем содержимое слоя
                if image:
                    # Создаём холст (2048x2048) с прозрачным фоном
                    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
                    # Вставляем слой на холст с учётом его положения
                    left, top = layer.offset
                    canvas.paste(image, (left, top), mask=image)
                    
                    os.makedirs(os.path.join(output_folder, prefix), exist_ok=True)
                    output_file = os.path.join(output_folder, prefix, f"{layer_name}.png")
                    canvas.save(output_file, "PNG")  # Сохраняем слой с учётом положения
                    print(f"Слой '{layer_name}' экспортирован в {output_file}")
            else:
                print(f"Слой '{layer_name}' не содержит пикселей, пропущен.")
        except Exception as e:
            print(f"Ошибка при экспорте слоя '{layer_name}': {e}")

def export_psd_with_folders(psd_path, output_folder, canvas_size=(2048, 2048)):
    """
    Экспортирует все слои PSD с сохранением структуры папок и учётом положения слоёв.
    """
    psd = PSDImage.open(psd_path)
    os.makedirs(output_folder, exist_ok=True)

    for layer in psd:
        export_layer(layer, output_folder, canvas_size=canvas_size)

# Пример использования
psd_file_path = "MC.psd"  # Укажи путь к PSD-файлу
output_dir = "Манул_Креатор_layers"  # Папка для сохранения PNG
canvas_size = (2048, 2048)  # Размер изображения
export_psd_with_folders(psd_file_path, output_dir, canvas_size)
