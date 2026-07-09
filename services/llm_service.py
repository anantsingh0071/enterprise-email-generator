"""
llm_service.py
--------------------------------------------------
LLM Service

Single Responsibility:
Communicate with the Large Language Model.
"""

from __future__ import annotations

from google import genai

from config import (
    GOOGLE_API_KEY,
    GEMINI_MODEL,
    LLM_TEMPERATURE,
)


class LLMService:
    """
    Enterprise wrapper around Gemini.
    """

    def __init__(self) -> None:

        if not GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

        self.model = GEMINI_MODEL

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """
        Generate a response from Gemini.
        """

        response = self.client.models.generate_content(
            model=self.model,
            config={
                "system_instruction": system_prompt,
                "temperature": LLM_TEMPERATURE,
            },
            contents=user_prompt,
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text.strip()