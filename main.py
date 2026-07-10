"""
main.py
--------------------------------------------------
Entry point for the Enterprise Email Generator.
"""

from generators.email_generator import EmailGenerator
from services.dataset_service import DatasetService
from services.eml_generator import EMLGenerator


def main() -> None:
    """
    Execute the complete email generation workflow.
    """

    try:

        # Load one insurance record
        dataset = DatasetService()

        record = dataset.get_record(index=0)

        # Generate the email
        generator = EmailGenerator()

        email_data = generator.generate_email(
            record
        )

        # Save as .eml
        eml_generator = EMLGenerator()

        file_path = eml_generator.save(
            email_data=email_data,
            filename=f"{record['policy_number']}.eml",
        )

        print("\n===================================")
        print("Email generated successfully.")
        print(f"Saved to: {file_path}")
        print("===================================\n")

    except Exception as error:

        print("\n===================================")
        print("Email generation failed.")
        print(error)
        print("===================================\n")


if __name__ == "__main__":
    main()