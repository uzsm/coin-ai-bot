import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.analysis_service import analyze
from services.signal_service import generate_signal

result = analyze("BTCUSDT", "15m")

signal = generate_signal(result)

print(signal)