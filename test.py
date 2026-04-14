from utils.stt import transcribe
from utils.intent import detect_intent
from utils.actions import create_file, write_code, summarize

text = transcribe("sample.wav")
print("Text:", text)

intent = detect_intent(text)
print("Intent:", intent)

if intent == "create_file":
    result = create_file()

elif intent == "write_code":
    result = write_code()

elif intent == "summarize":
    result = summarize(text)

else:
    result = "Chat response"

print("Result:", result)