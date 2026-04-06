# Jellyfin Transcode Guide

**Filename:** `jellyfin-transcode-guide.py`

A Python tool that analyzes your computer hardware and Jellyfin server settings, then provides optimal transcoding recommendations. Designed for both casual users and advanced tweakers.

---

## Features

- Detects CPU, RAM, and GPU (if available) across Windows, Linux, and Mac.
- Reads Jellyfin server transcoding configuration via API.
- Provides **standard** mode for quick, easy recommendations.
- Provides **advanced** mode with detailed reasoning and practical guidance.
- Console-only output; safe and non-destructive.
- Gracefully handles missing information or errors.

---

## Requirements

- Python 3.8+
- [psutil](https://pypi.org/project/psutil/)
- [requests](https://pypi.org/project/requests/)

Install dependencies via:

```bash
pip install -r requirements.txt

## Usage

Run the script with:
```bash
python jellyfin-transcode-guide.py

For advanced mode output:
```bash
python jellyfin-transcode-guide.py --advanced

## OUTPUT

Standard Mode
Provides clean, easy-to-read recommendations:

```bash
Hardware Acceleration: NVENC
Video Codec: H264
Tone Mapping: On (for HDR → SDR)
Maximum Bitrate: 20M
Transcoding Threads: handled by GPU
GPU Model: NVIDIA GeForce RTX 3060
GPU VRAM: 12 GB

Advanced Mode
Provides detailed reasoning and practical guidance:

```bash
=== RECOMMENDATION SUMMARY ===
- Hardware Acceleration: NVENC (NVIDIA GPU detected → NVENC selected)
- Codec: H264
- Tone Mapping: Enabled
- Max Bitrate: 20M
- Transcoding Threads: handled by GPU
- GPU Model: NVIDIA GeForce RTX 3060
- GPU VRAM: 12 GB

=== WHY THIS MAKES SENSE ===
- GPU encoding (NVENC) uses GeForce RTX 3060 with 12 GB → keeps CPU free.
- H264 is widely compatible.
- Tone mapping ensures HDR content displays correctly on SDR devices.

=== PRACTICAL GUIDANCE ===
- Prefer Direct Play whenever possible to avoid unnecessary transcoding.
- Avoid 4K → 1080p conversions unless required.
- Lower bitrate for weaker devices or limited networks.

## CONFIGUTATION

Set your Jellyfin server info in jellyfin_config.py:

```bash
JELLYFIN_SERVER = "http://your.server.address:8096"
API_KEY = "your_api_key_here"
USER_ID = "your_user_id_here"

## NOTES

The script does not modify your Jellyfin server; it only provides recommendations.
Unknown GPU or VRAM info is hidden in output.
Designed to work on a wide range of hardware with minimal resource use.

## LICENSE

This project is free to use for personal or hobby purposes. No warranties.
