import pandas as pd
import plotly.graph_objects as go


def draw_chart(
    candles,
    pivots=None,
    swings=None,
    structure=None,
    bos=None,
    choch=None,
    filename="chart.png",
):

    # -----------------------------
    # Candle DataFrame
    # -----------------------------
    df = pd.DataFrame(candles)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    fig = go.Figure()

    # -----------------------------
    # Candlestick
    # -----------------------------
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

    # -----------------------------
    # Pivotlar
    # -----------------------------
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

    # -----------------------------
    # Swinglar
    # -----------------------------
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

                line=dict(color="orange", width=2),

                marker=dict(size=6),

                name="Swings"

            )
        )

    # -----------------------------
    # Structure Label
    # -----------------------------
    if structure:

        for item in structure:

            fig.add_annotation(

                x=df.iloc[item["index"]]["time"],

                y=item["price"],

                text=item["label"],

                showarrow=True,

                arrowhead=1

            )

    # -----------------------------
    # Layout
    # -----------------------------
    fig.update_layout(

        title="Coin AI Analysis",

        xaxis_title="Time",

        yaxis_title="Price",

        template="plotly_dark",

        xaxis_rangeslider_visible=False,

        legend=dict(

            orientation="h"

        )

    )

    # -----------------------------
    # Save PNG
    # -----------------------------
    fig.write_image(filename)

    return filename
from services.analysis_service import analyze


def create_chart(symbol, timeframe):

    result = analyze(symbol, timeframe)

    filename = draw_chart(
        candles=result["candles"],
        pivots=result["pivots"],
        swings=result["swings"],
        structure=result["structure"],
        bos=result["bos"],
        filename="chart.png"
    )

    return filename