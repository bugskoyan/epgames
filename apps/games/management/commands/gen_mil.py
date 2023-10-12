
from typing import Any
import random
from django.core.management.base import BaseCommand
from games.models import Game


GAMES_RAND = ["The Witcher 3", "Red Dead Redemption 2", "Minecraft", "Fortnite", "Among Us",
    "Fallout 4", "Cyberpunk 2077", "GTA V", "The Legend of Zelda: Breath of the Wild",
    "Overwatch", "Doom Eternal", "Halo Infinite", "Call of Duty: Warzone", "Apex Legends",
    "Assassin's Creed Valhalla", "FIFA 22", "NBA 2K22", "League of Legends", "Valorant",
    "Rainbow Six Siege", "Rocket League", "Stardew Valley", "Death Stranding", "Spider-Man: Miles Morales",
    "Horizon Zero Dawn", "Sekiro: Shadows Die Twice", "Resident Evil Village", "Mass Effect: Legendary Edition",
    "Animal Crossing: New Horizons", "The Elder Scrolls V: Skyrim"]




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        num_objects_to_create = 100  # Количество объектов для создания

        # Создаем список объектов для bulk_create
        objects_to_create = []
        for _ in range(num_objects_to_create):
            objects_to_create.append(Game(name = random.choice(GAMES_RAND), price = random.randint(1,20)))

        try:
            # Выполняем bulk_create для создания объектов
            Game.objects.bulk_create(objects_to_create, batch_size=1000)  # batch_size можете настроить по вашему усмотрению
            self.stdout.write(self.style.SUCCESS(f'Успешно создано {num_objects_to_create} объектов'))
        except Exception as exc:
            self.stderr.write(self.style.ERROR(f'Ошибка при создании объектов: {str(exc)}'))