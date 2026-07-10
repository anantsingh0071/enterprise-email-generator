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
        """
        Initialize the Gemini client.
        """

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

        Parameters
        ----------
        system_prompt : str
            Instructions for the model.

        user_prompt : str
            User input.

        Returns
        -------
        str
            Generated response.
        """

        if not system_prompt.strip():
            raise ValueError(
                "System prompt cannot be empty."
            )

        if not user_prompt.strip():
            raise ValueError(
                "User prompt cannot be empty."
            )

        try:

            response = self.client.models.generate_content(
                model=self.model,
                config={
                    "system_instruction": system_prompt,
                    "temperature": LLM_TEMPERATURE,
                },
                contents=user_prompt,
            )

        except Exception as error:

            raise RuntimeError(
                f"Failed to generate response from Gemini: {error}"
            ) from error

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text.strip()