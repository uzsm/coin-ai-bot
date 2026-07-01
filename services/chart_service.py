import pandas as pd
import plotly.graph_objects as go

from services.analysis_service import analyze
from services.indicator_service import calculate_indicators

def draw_chart(
    candles,
    pivots=None,
    swings=None,
    structure=None,
    bos=None,
    choch=None,
    order_blocks=None,
    filename="chart.png",
):

    print("=" * 50)
    print(candles[0])
    print("=" * 50)

    df = pd.DataFrame(candles)
    # ==========================================
    # EMA
    # ==========================================

    df["ema20"] = df["close"].ewm(span=20).mean()

    df["ema50"] = df["close"].ewm(span=50).mean()

    df["ema200"] = df["close"].ewm(span=200).mean()

    print(df.columns)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    fig = go.Figure()

    # ==================================================
    # Candlestick
    # ==================================================

    fig.add_trace(

        go.Candlestick(

            x=df["time"],

            open=df["open"],

            high=df["high"],

            low=df["low"],

            close=df["close"],

            name="Candles"

        )

    )
    fig.add_trace(

    go.Scatter(

        x=df["time"],

        y=df["ema20"],

        mode="lines",

        name="EMA20",

        line=dict(
            color="cyan",
            width=1
        )

        )

    )
    
    fig.add_trace(

    go.Scatter(

        x=df["time"],

        y=df["ema50"],

        mode="lines",

        name="EMA50",

        line=dict(
            color="yellow",
            width=1
        )

        )
  
    )
    fig.add_trace(

    go.Scatter(

        x=df["time"],

        y=df["ema200"],

        mode="lines",

        name="EMA200",

        line=dict(
            color="magenta",
            width=2
        )

        )

    ) 
     
    # ==================================================
    # Pivot
    # ==================================================

    if pivots:

        high_x = []
        high_y = []

        low_x = []
        low_y = []

        for p in pivots:

            t = df.iloc[p["index"]]["time"]

            if p["type"] == "HIGH":

                high_x.append(t)
                high_y.append(p["price"])

            else:

                low_x.append(t)
                low_y.append(p["price"])

        fig.add_trace(

            go.Scatter(

                x=high_x,

                y=high_y,

                mode="markers",

                marker=dict(
                    color="red",
                    size=10,
                    symbol="triangle-up"
                ),

                name="Pivot High"

            )

        )

        fig.add_trace(

            go.Scatter(

                x=low_x,

                y=low_y,

                mode="markers",

                marker=dict(
                    color="green",
                    size=10,
                    symbol="triangle-down"
                ),

                name="Pivot Low"

            )

        )

    # ==================================================
    # Swings
    # ==================================================

    if swings:

        sx = []
        sy = []

        for s in swings:

            sx.append(df.iloc[s["index"]]["time"])
            sy.append(s["price"])

        fig.add_trace(

            go.Scatter(

                x=sx,

                y=sy,

                mode="lines+markers",

                line=dict(
                    color="orange",
                    width=2
                ),

                marker=dict(
                    size=6
                ),

                name="Swings"

            )

        )

    # ==================================================
    # Structure
    # ==================================================

    if structure:

        for item in structure:

            fig.add_annotation(

                x=df.iloc[item["index"]]["time"],

                y=item["price"],

                text=item["label"],

                showarrow=True,

                arrowhead=2,

                font=dict(
                    size=11,
                    color="white"
                )

            )

    # ==================================================
    # BOS
    # ==================================================

    print("BOS:")
    print(bos)
    if bos:

        for item in bos:

            idx = item["index"]

            if idx >= len(df):
                continue

            color = "blue"

            if item["type"] == "BEARISH":
                color = "purple"

            fig.add_annotation(

                x=df.iloc[idx]["time"],

                y=item["price"],

                text="BOS",

                showarrow=True,

                arrowhead=2,

                arrowcolor=color,

                font=dict(
                    color=color,
                    size=12
                )

            )

    # ==================================================
    # ORDER BLOCK
    # ==================================================
    print("ORDER BLOCKS:")
    print(order_blocks)   

    if order_blocks:

        for ob in order_blocks:

            idx = ob["index"]

            if idx >= len(df):
                continue

            color = "rgba(0,255,0,0.25)"

            if ob["type"] == "BEARISH":
                color = "rgba(255,0,0,0.25)"

            fig.add_shape(

                type="rect",

                x0=df.iloc[idx]["time"],

                x1=df.iloc[min(idx + 8, len(df)-1)]["time"],

                y0=ob["low"],

                y1=ob["high"],

                fillcolor=color,

                line=dict(width=0),

                layer="below"

            )

    # ==================================================
    # CHOCH
    # ==================================================

    if choch:

        for item in choch:

            idx = item["index"]

            if idx >= len(df):
                continue

            fig.add_annotation(

                x=df.iloc[idx]["time"],

                y=item["price"],

                text="CHOCH",

                showarrow=True,

                arrowhead=2,

                arrowcolor="yellow",

                font=dict(
                    color="yellow",
                    size=12
                )

            )

    # ==================================================
    # Layout
    # ==================================================

    fig.update_layout(

        title="Coin AI Analysis",

        template="plotly_dark",

        xaxis_title="Time",

        yaxis_title="Price",

        xaxis_rangeslider_visible=False,

        legend=dict(
            orientation="h"
        ),

        height=900

    )

    fig.write_image(filename)

    return filename


# ==================================================
# Telegram
# ==================================================

def create_chart(symbol, timeframe):

    result = analyze(symbol, timeframe)

    return draw_chart(

        candles=result["candles"],

        pivots=result["pivots"],

        swings=result["swings"],

        structure=result["structure"],

        bos=result["bos"],

        choch=None,

        order_blocks=result["order_blocks"],

        filename="chart.png"

    )