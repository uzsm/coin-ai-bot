from services.binance_service import get_candles
import pandas as pd
import plotly.graph_objects as go

candles = get_candles("BTCUSDT", "15m", 200)

df = pd.DataFrame(candles)

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df.index,
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
        )
    ]
)

fig.update_layout(
    title="BTCUSDT 15m",
    xaxis_rangeslider_visible=False
)

# PNG qilib saqlaydi
fig.write_image("chart.png")

print("Grafik chart.png fayliga saqlandi.")