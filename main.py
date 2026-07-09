"""
main.py
--------------------------------------------------
Entry point for the Email Generator.
"""

from generators.email_generator import EmailGenerator
from services.dataset_service import DatasetService
from services.eml_generator import EMLGenerator


def main():

    dataset = DatasetService()

    record = dataset.get_record(index=0)

    generator = EmailGenerator()

    email_data = generator.generate_email(record)

    eml_generator = EMLGenerator()

    file_path = eml_generator.save(
        email_data=email_data,
        filename=f"{record['policy_number']}.eml",
    )

    print(f"Email saved to: {file_path}")


if __name__ == "__main__":
    main()