from openai import OpenAI
from key import key
from datetime import datetime

# Aktuelles Datum und Uhrzeit
jetzt = datetime.now()

# Umwandlung in einen String im gewünschten Format
jetzt_string = jetzt.strftime("%Y-%m-%d %H:%M")
client = OpenAI(api_key=key)


def text_to_speech(text, voice, filename):
    """
    Konvertiert Text in Sprache unter Verwendung der OpenAI Audio-API.

    :param text: Der umzuwandelnde Text.
    :param voice: Die Stimme, die für die Audioausgabe verwendet wird (standardmäßig 'nova').
    :return: Pfad zur erstellten Audiodatei.
    """
    try:
        # Setzen Sie hier Ihren OpenAI-API-Schlüssel ein
        

        # Erstellen der Sprachausgabe
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )

        # Speichern der Audiodatei
        audio_path = f"{filename}.mp3"
        response.stream_to_file(audio_path)

        return audio_path

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

# Beispieltext
mein_text = """

In Deutsch ist die Bewertung bei Schreibaufträgen deutlich subjektiver. Die Themen sind viel komplexer. Deswegen macht die Lehrkraft vorher Kriterien, Schwerpunkte und Bedingungen transparent, schon in der gemeinsamen Vorbereitung. 

Das kriegen aber die Eltern nicht mit!

"""

voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
for voice in voices:
    audio_datei = text_to_speech(mein_text, voice, f"{jetzt_string}_output_{voice}")

    if audio_datei:
        print(f"Audio wurde erstellt: {audio_datei}")
