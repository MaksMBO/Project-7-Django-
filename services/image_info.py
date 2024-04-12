import os
from PIL import Image
from typing import Union, Tuple


def open_image(image_path: str) -> Tuple[Image.Image, str]:
    """
    Відкриває зображення з заданого шляху.
    """
    return Image.open(image_path), image_path


def resize_image(img: Image.Image, image_path: str) -> Tuple[Image.Image, str]:
    """
    Змінює розмір зображення, якщо його розміри перевищують 800x800 пікселів.
    """
    if img.height > 800 or img.width > 800:
        output_size = (800, 800)
        img.thumbnail(output_size)
        img.save(image_path)
    return img, image_path


def convert_to_webp(img: Image.Image, image_path: str) -> Union[Tuple[str, str], Tuple[None, None]]:
    """
    Конвертує зображення в формат WEBP, якщо воно не знаходиться у цьому форматі.
    """
    first_path = image_path
    if img.format != 'WEBP':
        img = img.convert('RGB')
        image_path = os.path.splitext(image_path)[0]
        webp_path = f"{image_path}.webp"
        img.save(webp_path, 'WEBP')
        return os.path.relpath(webp_path, 'media'), first_path
    return None, None


def resize_and_convert_image(image_path: str) -> Tuple[str, str]:
    """
    Змінює розмір та конвертує зображення в WEBP.
    """
    img, original_path = open_image(image_path)
    img, _ = resize_image(img, original_path)
    return convert_to_webp(img, original_path)


def handle_image(instance) -> None:
    """
    Обробляє зображення моделі, змінюючи його розмір та конвертуючи у формат WEBP.
    """
    if instance.image:
        new_image_path, old_image_path = resize_and_convert_image(instance.image.path)
        if new_image_path:
            instance.image.name = new_image_path
            instance.save()
            if old_image_path and os.path.exists(old_image_path):
                os.remove(old_image_path)
