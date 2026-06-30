import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.analysis_service import analyze
from services.scoring_service import calculate_score

result = analyze("BTCUSDT", "15m")

score = calculate_score(result)

print(score)