from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

class BaseRule(ABC):

    name: str = ""

    @abstractmethod
    def validate(
        self,
        column_name: str,
        series: pd.series
    ) -> list[int]:
        
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.name