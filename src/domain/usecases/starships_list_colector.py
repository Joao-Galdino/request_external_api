from abc import ABC, abstractclassmethod
from typing import Dict, List


class StarshipsListColectorInterface(ABC):
    """Starships Colector Interface"""

    @abstractclassmethod
    def list(cls, page: int) -> List[Dict]:
        """Must implement"""
        raise Exception("Must implement list method")
