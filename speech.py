import streamlit as st
import speech_recognition as sr

def transcribe_speech(api, language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now...")
        audio_text = r.listen(source)
        st.info("Transcribing... Please wait.")
        
        try:
            if api == "Google Speech Recognition":
                text = r.recognize_google(audio_text, language=language)
            elif api == "Sphinx":
                text = r.recognize_sphinx(audio_text, language=language)
            else:
                return "Unsupported API selected."
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Sorry, there was an error with the speech recognition service: {e}"

def main():
    st.title("Enhanced Speech Recognition App")
    
    api_choice = st.selectbox("Select Speech Recognition API", ["Google Speech Recognition", "Sphinx"])
    language_choice = st.selectbox("Select Language", ["en-US", "es-ES", "fr-FR", "de-DE"])
    
    if st.button("Start Recording"):
        with st.spinner("Recording..."):
            text = transcribe_speech(api_choice, language_choice)
            st.success("Transcription complete!")
            st.write("Transcription: ", text)
            
            # Save to file
            if st.button("Save Transcription"):
                with open("transcription.txt", "w") as f:
                    f.write(text)
                st.success("Transcription saved to transcription.txt")

if __name__ == "__main__":
    main()