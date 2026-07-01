import pandas as pd
import plotly.graph_objects as go

from services.analysis_service import analyze


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

    df = pd.DataFrame(candles)

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
    # Structure (HH HL LH LL)
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

    if bos:

        for item in bos:

            idx = item["break_index"]

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
    # CHoCH
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
# Telegram uchun
# ==================================================

def create_chart(symbol, timeframe):

    result = analyze(symbol, timeframe)

    filename = draw_chart(

        candles=result["candles"],

        pivots=result["pivots"],

        swings=result["swings"],

        structure=result["structure"],

        bos=result["bos"],
        
        order_blocks=result["order_blocks"],  

        filename="chart.png"

    )

    return filename