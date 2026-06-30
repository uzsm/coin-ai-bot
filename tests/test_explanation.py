import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.analysis_service import analyze
from services.signal_service import generate_signal
from services.explanation_service import explain_signal

result = analyze("BTCUSDT", "15m")

signal = generate_signal(result)

report = explain_signal(result, signal)

print(report)