# 🎥 AI Motion Blur Studio

A Python-based AI-style video processing tool that applies cinematic motion blur effects to videos using OpenCV and Streamlit.  
Supports large video files (local setup) and exports final video with audio using FFmpeg.

---

## 🚀 Features

- 🎬 Upload videos (MP4, MOV, AVI)
- 🎥 Real-time motion blur effect
- 🔊 Audio preserved using FFmpeg
- 📊 Progress bar during processing
- 👀 Before / After preview
- ⬇️ Download processed video
- 💻 Clean Streamlit web UI
- 📁 Supports large video files (local mode)

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- OpenCV 👁️
- NumPy 🔢
- FFmpeg 🎞️

---

## 📦 Installation (A → Z Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/EnukaSathmina/AI-Motion-Blur-Studio.git
cd ai-motion-blur-studio
```
### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```
Activate it:

#### Windows:
```bash 
venv\Scripts\activate
```
#### Mac/Linux:
```bash 
source venv/bin/activate
```
### 3️⃣ Install dependencies

```bash
pip install streamlit opencv-python numpy
```
### 4️⃣ Install FFmpeg

```bash
ffmpeg -version
```
If not installed, download from:
👉 https://www.gyan.dev/ffmpeg/builds/

Then add bin folder to PATH.

### 5️⃣ Run the project

```bash
streamlit run app.py
```

## ⚙️ Configuration (IMPORTANT)

To increase video upload size for local use, you can modify Streamlit’s server settings.

Create a file in your project:

``` .streamlit/config.toml ```

Then add:

```[server]```
```maxUploadSize = 5120```

#### 💡 Notes
```maxUploadSize``` is measured in MB
5120 = 5GB upload limit (local only)
This setting does NOT work on Streamlit Cloud
For best performance, always run the project locally
