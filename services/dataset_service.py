"""
dataset_service.py
--------------------------------------------------
Dataset Service

Responsible for providing one insurance record
to the Email Generator.
"""

from __future__ import annotations


class DatasetService:
    """
    Provides insurance records.

    Currently uses dummy data.
    Later this can be replaced with:
        - CSV
        - Excel
        - Database
        - API
    """

    def __init__(self) -> None:

        self.records = [

            {
                "policy_number": "POL-100001",
                "insurer_name": "ABC General Insurance",
                "insurer_email": "claims@abcinsurance.com",
                "broker_name": "Michael Johnson",
                "broker_id": "BRK-1001",
                "broker_email": "michael.johnson@brokerlink.com",
            },

            {
                "policy_number": "POL-100002",
                "insurer_name": "SecureLife Insurance",
                "insurer_email": "underwriting@securelife.com",
                "broker_name": "Sarah Williams",
                "broker_id": "BRK-1002",
                "broker_email": "sarah.williams@brokerlink.com",
            },

            {
                "policy_number": "POL-100003",
                "insurer_name": "Guardian Mutual Insurance",
                "insurer_email": "claims@guardianmutual.com",
                "broker_name": "David Brown",
                "broker_id": "BRK-1003",
                "broker_email": "david.brown@brokerlink.com",
            },

            {
                "policy_number": "POL-100004",
                "insurer_name": "Everest Insurance",
                "insurer_email": "commercial@everestinsurance.com",
                "broker_name": "Emily Davis",
                "broker_id": "BRK-1004",
                "broker_email": "emily.davis@brokerlink.com",
            },

            {
                "policy_number": "POL-100005",
                "insurer_name": "Global Risk Insurance",
                "insurer_email": "claims@globalrisk.com",
                "broker_name": "Robert Wilson",
                "broker_id": "BRK-1005",
                "broker_email": "robert.wilson@brokerlink.com",
            }

        ]

    def get_record(self, index: int = 0) -> dict:
        """
        Return one insurance record.
        """

        if index < 0 or index >= len(self.records):
            raise IndexError(
                f"Record index {index} is out of range. "
                f"Available records: 0 to {len(self.records) - 1}"
            )

        return self.records[index]