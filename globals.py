from ai import ReviewWriter
import os

writer = ReviewWriter(os.getenv("OPENAI_API_KEY"))
