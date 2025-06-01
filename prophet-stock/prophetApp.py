import holidays
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet 
import streamlit as st
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

st.title("Stock Price Forecasting with Prophet")

popular_tickers = {
    "RELIANCE.NS": "Reliance Industries",
    "TCS.NS": "Tata Consultancy Services",
    "INFY.NS": "Infosys",
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft"
}

ticker = st.selectbox("Select or enter stock ticker:", options=list(popular_tickers.keys()), format_func=lambda x: f"{x} - {popular_tickers[x]}")


ticker = st.text_input("Enter Stock Ticker (e.g., RELIANCE.NS):", "RELIANCE.NS")
start_date = st.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2024-12-31"))
forecast_period = st.slider("Forecast Period (days):", min_value=30, max_value=365, value=90)

df = None

if st.button("Run Forecast"):
    try:
        df = yf.download(ticker, start = start_date, end=end_date)

        if df.empty or len(df) < 30:
            st.error("Not enough data. Try another ticker or longer date range.")
        
        else:
            df = df.reset_index()      
            df = df[['Date','Close']]
            df.columns = ['ds','y']

            model = Prophet()
            model.fit(df)

            #Predict for next 90 days
            future = model.make_future_dataframe(periods=90)
            forecast = model.predict(future)

            #Visualizing Forecast
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=df['ds'],
                y=df['y'],
                mode='lines',
                name='Actual Stock price',
                line=dict(color='green', width=2)
            ))

            fig.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat'],
                mode = 'lines',
                name='Predicted price',
                line = dict(color='orange', width=2)
            ))

            fig.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat_upper'],
                name='Upper Bound',
                line=dict(width=0),
                showlegend=False
            ))

            fig.add_trace(go.Scatter(
                x=forecast['ds'],
                y=forecast['yhat_lower'],
                mode='lines',
                fill='tonexty',
                name='Confidence Interval',
                line=dict(width=0),
                fillcolor='rgba(255,165,0,0.2)'
            ))

            fig.update_layout(
                title='📈 Stock Forecast with Prophet (Plotly)',
                xaxis_title='Date',
                yaxis_title='Price (INR)',
                template='plotly_dark',  # Use 'plotly_white' if you prefer light mode
                hovermode='x unified',
                height=600
            )
            if df is not None:
                st.table(df.head(11))
                st.plotly_chart(fig, use_container_width=True)
                st.text("CI shows the range within which the actual stock price is expected to fall — with a certain confidence level, typically 80% or 95%.")

            #adding holiday effects
            with st.expander("Show Holiday Effects"):
            
                years = list(range(start_date.year, end_date.year+2))
                indian_holidays = holidays.India(years=years)
                holidays_df = pd.DataFrame([
                    {'ds': pd.to_datetime(date), 'holiday': name}
                    for date, name in indian_holidays.items()
                ])

                model = Prophet(holidays=holidays_df)
                model.fit(df)

                # Forecast
                future = model.make_future_dataframe(periods=forecast_period)
                forecast = model.predict(future)

                # Plot
                fig_holiday = go.Figure()
                fig_holiday.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='lines', name='Actual Price', line=dict(color='green')))
                fig_holiday.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted Price', line=dict(color='red')))
                fig_holiday.update_layout(title="Stock Forecast with Indian Holidays", xaxis_title='Date', yaxis_title='Price (INR)', template='plotly_dark')

                #see holiday impact
                fig2 = model.plot_components(forecast)
                st.plotly_chart(fig_holiday, use_container_width=True)
                st.pyplot(fig2)
            
            
    except Exception as e:
        st.error(f"Error: {e}")       



    



