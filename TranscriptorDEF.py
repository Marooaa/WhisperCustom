import os
import whisper
from pydub import AudioSegment
import math

# Configuración
audio_folder = "D:/whisperr/Audios"  # Ruta de la carpeta de audios
output_dir = "D:/whisperr/Transcripciones"  # Ruta donde se guardarán las transcripciones

# Función para convertir a WAV
def convert_audio_to_wav(audio_path):
    try:
        print(f"Convirtiendo {audio_path} a formato WAV...")
        audio = AudioSegment.from_file(audio_path)
        wav_path = audio_path.replace(".mp3", ".wav").replace(".m4a", ".wav")
        audio.export(wav_path, format="wav")
        print(f"Archivo convertido a WAV: {wav_path}")
        return wav_path
    except Exception as e:
        print(f"Error al convertir {audio_path} a WAV: {e}")
        return None

# Función para dividir el audio en segmentos de 4 minutos (240 segundos)
def split_audio(audio_path, segment_length=240):
    try:
        print(f"Dividiendo el audio {audio_path} en segmentos de {segment_length} segundos...")
        audio = AudioSegment.from_wav(audio_path)
        duration_ms = len(audio)  # Duración en milisegundos
        num_segments = math.ceil(duration_ms / (segment_length * 1000))  # número de segmentos
        segments = []

        for i in range(num_segments):
            start_ms = i * segment_length * 1000
            end_ms = min((i + 1) * segment_length * 1000, duration_ms)
            segment = audio[start_ms:end_ms]
            segment_path = f"{audio_path}_part_{i + 1}.wav"
            segment.export(segment_path, format="wav")
            print(f"Segmento guardado: {segment_path}")
            segments.append(segment_path)

        return segments
    except Exception as e:
        print(f"Error al dividir el audio {audio_path}: {e}")
        return []

# Función para convertir segundos a formato HH:MM:SS
def seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Función para transcribir el audio
def transcribe_audio(audio_path, model):
    try:
        print(f"Transcribiendo el archivo {audio_path}...")
        result = model.transcribe(audio_path)
        print(f"Transcripción completada para {audio_path}")
        return result["text"], result["segments"]
    except Exception as e:
        print(f"Error al transcribir el archivo {audio_path}: {e}")
        return "", []

# Procesamiento
def process_audio(audio_path):
    model = whisper.load_model("large-v2")  # O el modelo que prefieras
    wav_path = convert_audio_to_wav(audio_path)  # Convierte el audio a WAV
    if not wav_path:
        print(f"Error: No se pudo convertir {audio_path} a WAV. Saltando este archivo.")
        return

    segments = split_audio(wav_path)  # Divide el audio en segmentos
    if not segments:
        print(f"Error: No se pudieron generar segmentos para {wav_path}. Saltando este archivo.")
        return

    full_transcription = []
    
    for i, segment in enumerate(segments):
        print(f"Procesando segmento {i+1}/{len(segments)}: {segment}")
        transcription, srt_segments = transcribe_audio(segment, model)

        # Guardar transcripción en .txt
        txt_file_path = os.path.join(output_dir, f"{os.path.basename(audio_path).replace('.mp3', '').replace('.m4a', '')}_transc.txt")
        with open(txt_file_path, 'a', encoding='utf-8') as f:
            for s in srt_segments:
                start_time = seconds_to_hms(s['start'])
                end_time = seconds_to_hms(s['end'])
                f.write(f"{start_time} --> {end_time} {s['text']}\n")
        
        full_transcription.append(transcription)
    
    print(f"Transcripción completada para {audio_path}. Guardado en: {output_dir}")

# Procesar todos los audios en la carpeta
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith(".mp3") or audio_file.endswith(".wav") or audio_file.endswith(".m4a"):
        audio_path = os.path.join(audio_folder, audio_file)
        print(f"Procesando archivo: {audio_file}")
        process_audio(audio_path)

print("Procesamiento completado.")