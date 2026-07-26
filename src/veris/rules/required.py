from __future__ import annotations

import pandas as pd

from veris.rules.base import BaseRule

class RequiredRule(BaseRule):

    name = "required"

    def validate(
            self,
            column_name: str,
            series: pd.Series,
    ) -> list[int]:
        
        failed = series[series.isna()]

        return failed.index.tolist()