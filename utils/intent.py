def detect_intent(text):
    text = text.lower()

    if "create" in text and "file" in text:
        return "create_file"

    elif "write" in text and "code" in text:
        return "write_code"

    elif "summarize" in text:
        return "summarize"

    else:
        return "chat"