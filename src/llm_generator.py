from transformers import pipeline

def generate_feedback(summary_embedding, context):
    prompt = (
        f"Based on heart rate and HRV trends: {summary_embedding}, "
        f"during {context['calendar_event']} at {context['location']}, "
        "generate a short wellness reflection."
    )
    generator = pipeline("text-generation", model="gpt2")
    return generator(prompt, max_length=50)[0]['generated_text']
