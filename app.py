import streamlit as st
import cv2
import numpy as np
import os
import subprocess

st.set_page_config(page_title="AI Motion Blur Studio", layout="wide")

st.title("🎥 AI Motion Blur Studio (Final Version)")
st.caption("Smooth motion blur + large video support + audio export")

uploaded_file = st.file_uploader("Upload video", type=["mp4", "mov", "avi"])

if uploaded_file:

    # ---------------- SAVE FILE SAFELY ----------------
    input_path = "input.mp4"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        st.error("❌ Cannot open video")
        st.stop()

    # ---------------- VIDEO INFO ----------------
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = fps if fps > 0 else 30

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # ---------------- SETTINGS ----------------
    strength = st.slider("🎚 Motion Blur Strength", 2, 8, 3)

    start = st.button("🚀 Start Processing")

    raw_output = "output_no_audio.mp4"
    final_output = "final_output.mp4"

    writer = cv2.VideoWriter(
        raw_output,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    # ---------------- UI ----------------
    col1, col2 = st.columns(2)
    orig_box = col1.empty()
    blur_box = col2.empty()

    progress = st.progress(0)
    status = st.empty()

    # ---------------- PROCESS ----------------
    if start:

        buffer = []
        frame_index = 0

        status.info("Processing video... please wait ⏳")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # ---------------- MOTION BLUR ----------------
            buffer.append(frame)

            if len(buffer) > strength:
                buffer.pop(0)

            smooth_frame = np.mean(buffer, axis=0).astype(np.uint8)

            # cinematic blend
            smooth_frame = cv2.addWeighted(frame, 0.5, smooth_frame, 0.5, 0)

            writer.write(smooth_frame)

            # preview
            orig_box.image(frame, channels="BGR")
            blur_box.image(smooth_frame, channels="BGR")

            frame_index += 1
            progress.progress(frame_index / total_frames)

        cap.release()
        writer.release()

        status.success("✅ Processing complete! Adding audio 🎧")

        # ---------------- ADD AUDIO BACK ----------------
        subprocess.run([
            "ffmpeg", "-y",
            "-i", raw_output,
            "-i", input_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-map", "0:v:0",
            "-map", "1:a:0",
            final_output
        ])

        status.success("🎉 Done!")

        # ---------------- DOWNLOAD ----------------
        with open(final_output, "rb") as f:
            st.download_button(
                "⬇️ Download Final Video",
                f,
                file_name="ai_motion_blur.mp4",
                mime="video/mp4"
            )