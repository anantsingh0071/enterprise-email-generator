"""
email_generator.py
--------------------------------------------------
Enterprise Email Generator

Runs the complete prompt chain.

Workflow

Insurance Record
        │
        ▼
Analyzer Prompt
        │
        ▼
Planner Prompt
        │
        ▼
Writer Prompt
        │
        ▼
Reviewer Prompt
        │
        ▼
Final Email
"""

from __future__ import annotations

import json
from pathlib import Path

from services.llm_service import LLMService


class EmailGenerator:
    """
    Enterprise Email Generator.

    Responsible for executing the complete
    prompt chain and returning the final email.
    """

    def __init__(self):
        self.llm = LLMService()

    def _load_prompt(self, filename: str) -> str:
        """
        Load a prompt file from the prompts directory.
        """

        prompt_path = Path(__file__).parent.parent / "prompts" / filename

        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()

    def generate_email(
        self,
        record: dict,
    ) -> dict:
        """
        Generate one professional insurance email.
        """

        # Prompt 1
        business_context = self._analyze_record(record)

        # Prompt 2
        email_blueprint = self._plan_email(
            business_context
        )

        # Prompt 3
        draft_email = self._write_email(
            business_context,
            email_blueprint,
        )

        # Prompt 4
        final_email = self._review_email(
            draft_email
        )

        return final_email

    # --------------------------------------------------
    # Prompt 1 - Analyzer
    # --------------------------------------------------

    def _analyze_record(self, record: dict) -> str:
        """
        Analyze the insurance record and generate
        structured business context.
        """

        system_prompt = self._load_prompt(
            "analyzer_system.txt"
        )

        user_prompt = self._load_prompt(
            "analyzer_user.txt"
        )

        user_prompt = user_prompt.format(
            policy_number=record.get("policy_number", ""),
            insurer_name=record.get("insurer_name", ""),
            insurer_email=record.get("insurer_email", ""),
            broker_name=record.get("broker_name", ""),
            broker_id=record.get("broker_id", ""),
            broker_email=record.get("broker_email", ""),
        )

        return self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

    # --------------------------------------------------
    # Prompt 2 - Planner
    # --------------------------------------------------

    def _plan_email(
        self,
        business_context: str,
    ) -> str:
        """
        Create the email blueprint.
        """

        system_prompt = self._load_prompt(
            "planner_system.txt"
        )

        user_prompt = self._load_prompt(
            "planner_user.txt"
        )

        user_prompt = user_prompt.format(
            business_context=business_context
        )

        return self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

    # --------------------------------------------------
    # Prompt 3 - Writer
    # --------------------------------------------------

    def _write_email(
        self,
        business_context: str,
        email_blueprint: str,
    ) -> str:
        """
        Generate the draft email.
        """

        system_prompt = self._load_prompt(
            "writer_system.txt"
        )

        user_prompt = self._load_prompt(
            "writer_user.txt"
        )

        user_prompt = user_prompt.format(
            business_context=business_context,
            email_blueprint=email_blueprint,
        )

        return self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

    # --------------------------------------------------
    # Prompt 4 - Reviewer
    # --------------------------------------------------
    
    def _review_email(
        self,
        draft_email: str,
    ) -> dict:
        """
        Review and polish the email.

        Returns
        -------
        dict
            Final reviewed email as JSON.
        """

        system_prompt = self._load_prompt(
            "reviewer_system.txt"
        )

        user_prompt = self._load_prompt(
            "reviewer_user.txt"
        )

        user_prompt = user_prompt.format(
            generated_email=draft_email
        )

        reviewed_email = self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        print("\n========== REVIEWER OUTPUT ==========")
        print(reviewed_email)
        print("=====================================\n")

        # Remove markdown code fences if Gemini returns them
        reviewed_email = reviewed_email.strip()

        if reviewed_email.startswith("```json"):
            reviewed_email = reviewed_email.replace(
                "```json",
                "",
                1,
            ).strip()

        if reviewed_email.startswith("```"):
            reviewed_email = reviewed_email.replace(
                "```",
                "",
                1,
            ).strip()

        if reviewed_email.endswith("```"):
            reviewed_email = reviewed_email[:-3].strip()

        try:
            return json.loads(reviewed_email)

        except json.JSONDecodeError as error:

            print("\n========= INVALID JSON =========")
            print(reviewed_email)
            print("===============================\n")

            raise ValueError(
                "Reviewer prompt returned invalid JSON."
            ) from error
