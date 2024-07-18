import os
import math
from PIL import Image
import shutil

def process_images(folder_path, x1, x2, y1, y2):
    #lista plików
    files = os.listdir(folder_path)
    # tylko .jpg
    images = [f for f in files if f.lower().endswith('.jpg')]
    ilość_zdjęć = len(images)

    if ilość_zdjęć == 0:
        print("brak plikow")
        return

    # lokalizacja wyjsciowa
    processed_folder = os.path.join(folder_path, 'out')
    os.makedirs(processed_folder, exist_ok=True)

    for img_file in images:
        # znajdowanie nr zdjecia w nazwie pliku
        nr_zdjęcia = int(img_file[:4])

        # liczenie
        x = (x1 / 2) * math.cos(math.radians(360 * (nr_zdjęcia / ilość_zdjęć))) + (x2 / 2) * math.cos(math.radians((90 + 360) * (nr_zdjęcia / ilość_zdjęć)))

        y = (y1 / 2) * math.cos(math.radians(360 * (nr_zdjęcia / ilość_zdjęć))) + (y2 / 2) * math.cos(math.radians((90 + 360) * (nr_zdjęcia / ilość_zdjęć)))

        # ladowanie zdjecia
        img_path = os.path.join(folder_path, img_file)
        with Image.open(img_path) as img:
            # tworzenie nowego z przesunieciem
            new_img = Image.new(img.mode, img.size)
            new_img.paste(img, (int(x), int(y)))

            # zapis
            new_img.save(os.path.join(processed_folder, img_file))

    print(f"Processed images are saved in {processed_folder}")

# Example usage
folder_path = '/mnt/data'  # sciezka do plików wejsciowych
x1, x2, y1, y2 = 10, 20, 30, 40  # przesuniecie
process_images(folder_path, x1, x2, y1, y2)
