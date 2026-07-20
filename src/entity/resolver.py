from rapidfuzz import process

KNOWN_COMPANIES = [
    "OpenAI",
    "Anthropic",
    "Google DeepMind",
    "Perplexity",
    "Mistral AI",
    "Cursor",
    "Runway",
    "Midjourney",
]


def canonicalize(name):

    match = process.extractOne(name, KNOWN_COMPANIES)

    if match and match[1] > 85:
        return match[0]

    return name