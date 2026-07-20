import asyncio

from src.llm.gemini import extract_json


async def extract_with_fallback(text: str):
    """
    LLM Orchestrator

    Gemini
        ↓
    (Future)
    Groq
        ↓
    DeepSeek
    """

    try:
        result = await extract_json(text)

        if result:
            return result

    except Exception as e:
        print("Gemini failed:", e)

    # Future fallback providers
    # result = await groq_extract(text)
    # if result:
    #     return result

    # result = await deepseek_extract(text)
    # if result:
    #     return result

    return None