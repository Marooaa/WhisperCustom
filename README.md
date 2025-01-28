# WhisperCustom
Transcribe audios a texto con timestamps

# Tutorial: Configuración y Ejecución del Transcriptor con Whisper

Este tutorial te guiará paso a paso para configurar tu entorno y ejecutar el script de transcripción de audios con segmentación y timestamps en Python utilizando Whisper.

---

## 1. Requisitos previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

### Hardware:
- **GPU** recomendada para un rendimiento óptimo (aunque también funciona en CPU).
- Espacio suficiente en disco para manejar los audios y transcripciones.

### Software:
- Sistema operativo: Windows, Linux o macOS.
- Python 3.10 o superior (se recomienda Python 3.11).
- **Visual Studio Build Tools** (en Windows) con el componente “Desktop development with C++” instalado.
- **FFmpeg** instalado y configurado en las variables de entorno.

---

## 2. Instalación y configuración

### Paso 1: Instalar Python

Descarga e instala la versión más reciente de Python desde [python.org](https://www.python.org/). Durante la instalación, asegúrate de marcar la casilla **Add Python to PATH**.

### Paso 2: Instalar Visual Studio Build Tools (Windows)

1. Descarga Visual Studio Build Tools desde: [Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. Durante la instalación, selecciona el paquete **Desktop development with C++**.

### Paso 3: Instalar FFmpeg

1. Descarga FFmpeg desde: [FFmpeg](https://ffmpeg.org/download.html).
2. Extrae los archivos en una carpeta, por ejemplo, `C:\ffmpeg`.
3. Agrega la ruta del ejecutable FFmpeg a las variables de entorno:
   - Ve a “Propiedades del sistema > Configuración avanzada del sistema > Variables de entorno”.
   - Busca la variable `Path` y agrega la ruta al directorio `bin` de FFmpeg, por ejemplo: `C:\ffmpeg\bin`.
4. Verifica la instalación ejecutando el siguiente comando en el terminal:
   ```bash
   ffmpeg -version
   ```

### Paso 4: Instalar las dependencias de Python

Ejecuta los siguientes comandos en el terminal o en un entorno bash compatible:

```bash
pip install openai-whisper
pip install pydub
pip install ffmpeg-python
```

---

## 3. Cómo cambiar el modelo Whisper

El script utiliza el modelo **large-v2** por defecto, pero puedes cambiarlo dependiendo de tus necesidades:

- Modelos disponibles: `tiny`, `base`, `small`, `medium`, `large`, `large-v2`.
- Para cambiarlo, busca la siguiente línea en el código:

```python
model = whisper.load_model("large-v2")
```

- Sustituye `large-v2` por el modelo que prefieras. Por ejemplo:

```python
model = whisper.load_model("medium")
```

**Nota:** Modelos más grandes ofrecen mejor precisión, pero son más lentos y consumen más memoria.

---

## 4. Estructura del proyecto

### Archivos y carpetas:
- Carpeta de entrada de audios: `D:/whisperr/Audios`.
- Carpeta de salida de transcripciones: `D:/whisperr/Transcripciones`.
- Script de Python: Asegúrate de guardar el script en una ubicación accesible.

---

## 5. Ejecución del script

1. Coloca tus archivos de audio (`.mp3`, `.wav`, `.m4a`) en la carpeta `D:/whisperr/Audios`.
2. Asegúrate de que la carpeta `D:/whisperr/Transcripciones` exista. Si no, créala manualmente.
3. Ejecuta el script con el siguiente comando en el terminal:

```bash
python nombre_del_script.py
```

4. El script procesará cada archivo en la carpeta de entrada y generará un archivo `.txt` en la carpeta de salida con el mismo nombre del audio seguido de `_transc`.

---

## 6. Resultado esperado

Por cada archivo de audio, obtendrás un archivo `.txt` con el siguiente formato:

```
00:00:00 --> 00:04:00
Texto transcrito del primer segmento...

00:04:00 --> 00:08:00
Texto transcrito del segundo segmento...
```

---

## 7. Solución de problemas

### Error: “No module named ...”
Asegúrate de haber instalado todas las dependencias con el comando:
```bash
pip install openai-whisper pydub ffmpeg-python
```

### Error relacionado con FFmpeg
Verifica que FFmpeg esté correctamente instalado y configurado en las variables de entorno. Ejecuta:
```bash
ffmpeg -version
```

### Otros problemas
Si el script no funciona correctamente, verifica:
- La ruta de los archivos de audio.
- Que los nombres de los archivos no contengan caracteres especiales.

---

## 8. Personalización del script

### Cambiar la duración de los segmentos
En el código, puedes ajustar la duración de los segmentos cambiando el valor `segment_length` (en segundos):

```python
segments = split_audio(audio_path, segment_length=240)  # 4 minutos
```

### Cambiar los formatos de entrada
Para agregar soporte a otros formatos de audio, asegúrate de que FFmpeg los admita y actualiza esta línea:

```python
if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
```

Por ejemplo, para agregar `.m4a`:

```python
if audio_file.endswith(".mp3") or audio_file.endswith(".wav") or audio_file.endswith(".m4a"):
```

---
