from ingest import load_biosignal_data
from encoder import encode_signals
from llm_generator import generate_feedback

def run_feedback_pipeline(filepath):
    data = load_biosignal_data(filepath)
    embedding = encode_signals(data)
    context = {
        "calendar_event": data["calendar_event"],
        "location": data["location"]
    }
    feedback = generate_feedback(embedding, context)
    print("🧘 Daily Reflection:\n", feedback)
