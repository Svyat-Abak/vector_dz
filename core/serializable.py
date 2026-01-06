from abc import ABC, abstractmethod
from typing import Dict, Any


class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
