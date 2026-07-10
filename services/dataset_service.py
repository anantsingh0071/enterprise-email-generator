"""
dataset_service.py
--------------------------------------------------
Dataset Service

Loads insurance records from a CSV file.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


class DatasetService:

    def __init__(self):

        csv_path = (
            Path(__file__).parent.parent
            / "data"
            / "insurance_dataset.csv"
        )

        dataframe = pd.read_csv(csv_path)

        self.records = dataframe.to_dict(
            orient="records"
        )

    def get_record(
        self,
        index: int = 0,
    ) -> dict:

        if index < 0 or index >= len(self.records):
            raise IndexError("Invalid record index.")

        return self.records[index]

    def get_all_records(self):

        return self.records