"""
eml_generator.py
--------------------------------------------------
Enterprise EML Generator

Creates RFC 5322 compliant .eml files.
"""

from __future__ import annotations

from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from pathlib import Path


class EMLGenerator:
    """
    Generate Outlook/Gmail compatible .eml files.
    """

    def __init__(self) -> None:

        self.output_dir = (
            Path(__file__).parent.parent
            / "output"
        )

        self.output_dir.mkdir(
            exist_ok=True
        )

    def save(
        self,
        email_data: dict,
        filename: str,
    ) -> Path:
        """
        Save an email as a .eml file.

        Parameters
        ----------
        email_data : dict
            {
                "from_name": "...",
                "from_email": "...",
                "to_name": "...",
                "to_email": "...",
                "subject": "...",
                "body": "..."
            }

        filename : str
            Output filename.

        Returns
        -------
        Path
            Path to generated .eml file.
        """

        required_fields = [
            "from_name",
            "from_email",
            "to_name",
            "to_email",
            "subject",
            "body",
        ]

        for field in required_fields:

            if field not in email_data:
                raise KeyError(
                    f"Missing required field: {field}"
                )

        message = EmailMessage()

        message["From"] = (
            f'{email_data["from_name"]} '
            f'<{email_data["from_email"]}>'
        )

        message["To"] = (
            f'{email_data["to_name"]} '
            f'<{email_data["to_email"]}>'
        )

        message["Subject"] = email_data["subject"]

        message["Date"] = formatdate(
            localtime=True
        )

        message["Message-ID"] = make_msgid()

        message["MIME-Version"] = "1.0"

        # --------------------------------------------------
        # Normalize body formatting
        # --------------------------------------------------

        body = str(email_data["body"])

        # Convert literal escaped newlines into real newlines
        body = body.replace("\\r\\n", "\n")
        body = body.replace("\\n", "\n")

        # Normalize line endings
        body = body.replace("\r\n", "\n")
        body = body.strip()

        message.set_content(body)

        output_path = (
            self.output_dir
            / filename
        )

        with open(
            output_path,
            "wb",
        ) as file:

            file.write(
                message.as_bytes()
            )

        return output_path