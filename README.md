# Stock Trend Predictor

**Hackathon:** [SH Hacks 2025](https://www.shhacks.com/)

**Developers:** Thomas Wu ([@TakumiBC](https://github.com/TakumiBC)) & Lily Ding ([@Lily-D-coder](https://github.com/Lily-D-coder))  

**School:** [Shanghai Starriver Bilingual School](https://www.ssbs.sh.cn/)

---

## Introduction

The Stock Trend Predictor is an innovative tool that forecasts the future performance of AAPL stock. By combining multiple analytical methods, this project delivers a robust prediction of stock trends over the next two months. It highlights the practical power of data analytics and advanced mathematics to derive actionable insights in finance.

---

## Methodology

### Data Acquisition
- **Source:** Historical stock data is retrieved from Alpha Vantage.
- **Purpose:** Ensures a reliable foundation for our analysis.

### Data Processing
- **Cleaning & Organization:** The raw data is cleansed, structured, and transformed into numerical values.
- **Preparation:** Dates are converted into numeric format to enable mathematical modeling.

### Predictive Modeling
1. **Calculus-based Polynomial Regression:**  
   A higher-degree polynomial is fitted to the data to capture non-linear trends using calculus, revealing the underlying growth pattern.
2. **Holt’s Linear Trend Model:**  
   A time-series forecasting method that analyzes recent trends and levels to predict future values.

### Ensemble Forecasting
- **Combination:** Predictions from both methods are averaged to form an ensemble forecast.
- **Advantage:** This integrated approach enhances overall prediction accuracy.

### Visualization
- **Graphical Insight:** A comprehensive graph displays historical stock prices alongside the predicted trend for the next two months, providing clear insights into potential future performance.

---

## Key Features

- **Robust Predictions:**  
  The ensemble approach leverages the strengths of both polynomial regression and Holt’s model, resulting in a more reliable forecast.
  
- **Clear Visual Representation:**  
  Graphs clearly delineate historical data from future predictions, making complex trends easily understandable.


---

## Conclusion

The Stock Trend Predictor exemplifies how advanced analytical methods can be combined to effectively forecast financial trends. Developed by Thomas Wu and Lily Ding, this project from Shanghai Starriver Bilingual School not only offers practical insights into stock market behavior but also embodies the innovative spirit of SH Hacks 2025. We look forward to inspiring further exploration at the intersection of technology, mathematics, and finance.

---

## License

This project is licensed under the [MIT License](LICENSE).
