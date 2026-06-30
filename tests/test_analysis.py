import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.analysis_service import analyze


result = analyze("BTCUSDT", "15m")

print(result)