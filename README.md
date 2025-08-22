# LLM-Powered-Daily-Biofeedback-Companion
A lightweight LLM system that interprets biosignals from wearable devices (smartwatches, fitness bands, etc.) and generates natural language reflections on your physical and emotional state. It’s like journaling meets telemetry—your body speaks, and the LLM translates.


# PulsePrompt: LLM-Powered Daily Biofeedback Companion

PulsePrompt interprets biosignals from wearable devices and generates natural language reflections on your physical and emotional state. It blends time-series encoding with LLMs to create personalized wellness insights.

## Features
- Heart rate + HRV signal ingestion
- Context-aware feedback generation
- Hugging Face LLM integration
- Modular pipeline for expansion

## Example Output
🧘 “During your 2pm Team Sync, your heart rate and HRV suggest elevated stress. Consider a short walk before your next meeting.”

## Usage
```bash
python src/feedback.py
