from src.domain.usecases import starships_list_colector
from src.infra import SwapiApiConsumer
from .starships_list_colector import StarshipsListColector

__all__ = [
    "StarshipsListColector",
]


def test_list():
    api_consumer = SwapiApiConsumer()
    starships_list_colector_ = StarshipsListColector(api_consumer)

    page = 1
    starships_list_colector_.list(page)
