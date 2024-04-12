from django.core.paginator import Paginator
from typing import List, Optional
from flower.models import Flower


def get_flower_dict(flower: Flower) -> dict:
    """
    Повертає словник, що містить інформацію про квітку.
    """
    return {
        'id': flower.id,
        'name': flower.name,
        'description': flower.description,
        'price': flower.price,
        'currency': flower.currency,
        'image': flower.image,
        'available': flower.available,
    }


def get_all_flowers(limit: Optional[int] = None, available: Optional[bool] = None) -> List[dict]:
    """
    Повертає список словників із інформацією про всі квіти.
    """
    flowers_query = Flower.objects.all().only(
        'id', 'name', 'description', 'price', 'currency', 'image', 'available'
    )

    if available is not None:
        flowers_query = flowers_query.filter(available=available)

    if limit is not None:
        flowers_query = flowers_query[:limit]

    all_flowers = list(flowers_query)
    return [get_flower_dict(flower) for flower in all_flowers]


def get_flower_by_id(flower_id: int) -> dict:
    """
    Повертає інформацію про квітку за її ідентифікатором.
    """
    flower = Flower.objects.get(pk=flower_id)
    return get_flower_dict(flower)


def get_paginated_flowers(page_number: int, per_page: int = 12) -> Paginator:
    """
    Повертає сторінку зі списком квітів за номером сторінки.
    """
    all_flowers = get_all_flowers()
    paginator = Paginator(all_flowers, per_page)
    page_obj = paginator.get_page(page_number)
    return page_obj
