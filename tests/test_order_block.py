from services.analysis_service import analyze
from services.order_block_service import detect_order_blocks

result = analyze("BTCUSDT", "15m")

ob = detect_order_blocks(
    result["candles"],
    result["bos"]
)

print("Order Blocks:", len(ob))

for x in ob:
    print(x)