from __future__ import annotations

import pandas as pd

from validata.rules.base import BaseRule

class UniqueRule(BaseRule):

    name = "unique"

    def validate(
            self,
            column_name: str,
            series: pd.Series
    ) -> list[int]:
        
        duplicates = series.dropna().duplicated(keep="first")

        return duplicates[duplicates].index.tolist()