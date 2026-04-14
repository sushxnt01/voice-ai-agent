import streamlit as st
from utils.stt import transcribe
from utils.intent import detect_intent
from utils.actions import create_file, write_code, summarize

st.title("🎤 Voice AI Agent")

st.write("Upload an audio file and see the AI work!")

audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if audio_file is not None:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    st.subheader("📝 Transcription")
    text = transcribe("temp.wav")
    st.write(text)

    st.subheader("🧠 Intent")
    intent = detect_intent(text)
    st.write(intent)

    st.subheader("⚙️ Action")
    if intent == "create_file":
        result = create_file()
    elif intent == "write_code":
        result = write_code()
    elif intent == "summarize":
        result = summarize(text)
    else:
        result = "Chat response"

    st.write(result)

    st.subheader("✅ Final Output")
    st.success("Task completed successfully!")