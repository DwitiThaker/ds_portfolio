# Stock Price Prediction using Linear Regression and LSTM

This project by This project by [Dwiti Thaker](https://github.com/DwitiThaker/stock_price_prediction/blob/main/Stock_price_prediction.ipynb) demonstrates a comparative analysis...
 demonstrates a comparative analysis of two modeling techniques—**Linear Regression** and **Long Short-Term Memory (LSTM)**—for forecasting stock prices based on historical trends and technical indicators.

## Project Overview

This notebook walks through the end-to-end process of stock price prediction, including:

- Data preprocessing and visualization
- Feature engineering using EMA, WMA, and other technical indicators
- Model training and evaluation for both Linear Regression and LSTM
- Metrics used: MAE, RMSE, R²
- Visual comparisons of model predictions vs actual stock prices

## Key Insight

Although it is commonly believed that LSTM and other deep learning models perform best on time series data, this project highlights a valuable exception. Here, **Linear Regression outperforms LSTM**, suggesting that simpler models may generalize better in certain structured scenarios where the underlying patterns are more linear and the features are informative.

This underscores the importance of evaluating multiple approaches and **letting the data guide model choice rather than assumptions**.

## Tech Stack

- Python
- Google Colab
- NumPy, Pandas
- Scikit-learn
- Keras (TensorFlow backend)
- Matplotlib, Seaborn

## How to Run

1. Clone the repository: https://github.com/DwitiThaker/stock_price_prediction.
2. Open the `.ipynb` file using Jupyter Notebook or Google Colab
3. Place or link the stock data (if not included) and run the notebook step-by-step

## Author

Created by **Dwiti Thaker**  
Feel free to connect or reach out with suggestions, ideas, or collaborations.

## License

This project is released under the [MIT License](LICENSE).

