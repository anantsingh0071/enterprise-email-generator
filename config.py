"""
config.py
--------------------------------------------------
Application Configuration
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==================================================
# Gemini Configuration
# ==================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

LLM_TEMPERATURE = float(
    os.getenv(
        "LLM_TEMPERATURE",
        "0.1"
    )
)

# ==================================================
# Output
# ==================================================

OUTPUT_DIRECTORY = "output"