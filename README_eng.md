# Tutorial: Setting Up and Running the Transcription Script with Whisper

This tutorial will guide you through all the steps required to set up your environment and execute the audio transcription script with segmentation and timestamps using Python and Whisper.

---

## 1. Prerequisites

Before starting, ensure you meet the following requirements:

### Hardware:
- **GPU** recommended for optimal performance (though it also works on CPU).
- Sufficient disk space to handle audio files and transcriptions.

### Software:
- Operating system: Windows, Linux, or macOS.
- Python 3.10 or later (Python 3.11 recommended).
- **Visual Studio Build Tools** (on Windows) with the “Desktop development with C++” component installed.
- **FFmpeg** installed and configured in the system environment variables.

---

## 2. Installation and Configuration

### Step 1: Install Python

Download and install the latest version of Python from [python.org](https://www.python.org/). During installation, make sure to check the **Add Python to PATH** option.

### Step 2: Install Visual Studio Build Tools (Windows)

1. Download Visual Studio Build Tools from: [Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. During installation, select the **Desktop development with C++** workload.

### Step 3: Install FFmpeg

1. Download FFmpeg from: [FFmpeg](https://ffmpeg.org/download.html).
2. Extract the files into a folder, e.g., `C:\ffmpeg`.
3. Add the path to the FFmpeg executable to your system environment variables:
   - Go to “System Properties > Advanced System Settings > Environment Variables”.
   - Find the `Path` variable and add the path to the `bin` directory of FFmpeg, e.g., `C:\ffmpeg\bin`.
4. Verify the installation by running the following command in the terminal:
   ```bash
   ffmpeg -version
   ```

### Step 4: Install Python Dependencies

Run the following commands in the terminal or a compatible bash environment:

```bash
pip install openai-whisper
pip install pydub
pip install ffmpeg-python
```

---

## 3. How to Change the Whisper Model

The script uses the **large-v2** model by default, but you can change it based on your needs:

- Available models: `tiny`, `base`, `small`, `medium`, `large`, `large-v2`.
- To change the model, locate the following line in the code:

```python
model = whisper.load_model("large-v2")
```

- Replace `large-v2` with the model of your choice. For example:

```python
model = whisper.load_model("medium")
```

**Note:** Larger models offer better accuracy but are slower and consume more memory.

---

## 4. Project Structure

### Files and Folders:
- Input audio folder: `D:/whisperr/Audios`.
- Output transcription folder: `D:/whisperr/Transcriptions`.
- Python script: Ensure the script is saved in an accessible location.

---

## 5. Running the Script

1. Place your audio files (`.mp3`, `.wav`, `.m4a`) in the `D:/whisperr/Audios` folder.
2. Ensure the `D:/whisperr/Transcriptions` folder exists. If not, create it manually.
3. Run the script using the following command in the terminal:

```bash
python your_script_name.py
```

4. The script will process each file in the input folder and generate a `.txt` file in the output folder with the same name as the audio file, appended with `_transc`.

---

## 6. Expected Output

For each audio file, you will get a `.txt` file with the following format:

```
00:00:00 --> 00:04:00
Transcribed text of the first segment...

00:04:00 --> 00:08:00
Transcribed text of the second segment...
```

---

## 7. Troubleshooting

### Error: “No module named ...”
Ensure you have installed all dependencies with the following command:
```bash
pip install openai-whisper pydub ffmpeg-python
```

### FFmpeg-Related Errors
Verify that FFmpeg is correctly installed and configured in your environment variables. Run:
```bash
ffmpeg -version
```

### Other Issues
If the script doesn’t work as expected, check:
- The path to your audio files.
- That audio file names do not contain special characters.

---

## 8. Customizing the Script

### Changing Segment Duration
In the code, you can adjust the segment duration by modifying the `segment_length` value (in seconds):

```python
segments = split_audio(audio_path, segment_length=240)  # 4 minutes
```

### Adding Support for More Audio Formats
To add support for other audio formats, ensure FFmpeg supports them and update this line:

```python
if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
```

For example, to include `.m4a`:

```python
if audio_file.endswith(".mp3") or audio_file.endswith(".wav") or audio_file.endswith(".m4a"):
```

---
