import numpy as np

def encode_signals(data):
    heart_rate = np.array(data['heart_rate'])
    hrv = np.array(data['hrv'])
    features = np.stack([heart_rate, hrv], axis=1)
    return features.mean(axis=0).tolist()  # simple summary embedding
