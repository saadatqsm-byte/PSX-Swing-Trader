import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="PSX Swing Trader", layout="wide")

st.title("📈 PSX Swing Trader")
st.write("Pakistan Stock Exchange Analysis")

symbol = st.text_input("Stock Symbol", "MEBL")

if st.button("Analyze Stock"):
    try:
        data = yf.download(
            symbol + ".KA",
            period="3mo",
            interval="1d",
            progress=False
        )

        if data.empty:
            st.error("Data not available. Check stock symbol.")
        else:
            close = data["Close"]

            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]

            data["RSI"] = close.pct_change().rolling(14).mean() * 100

            st.subheader("Stock Price")
            st.line_chart(close)

            st.write("Latest Price:", round(float(close.iloc[-1]), 2))
            st.write("Data downloaded successfully!")

    except Exception as e:
        st.error(f"Error: {e}")
