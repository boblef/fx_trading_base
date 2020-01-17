# Backtesting

Backtesting is a key component of effective trading system development. It is accomplished by reconstructing, with historical data, trades that would have occurred in the past using rules defined by a given strategy. The result offers statistics to gauge the effectiveness of the strategy.
<br>
If you are a Machine Learning engineer or a Data Scientist, backtesting is similar to evaluating a model on test data.

---

<strong>Backtrader</strong>
I implemented backtesting process with <a href="https://www.backtrader.com/docu/">Backtrader</a>, which is a framework in Python for backtesting.

<strong>Cutormize</strong>

- `backtesting.py`
  - `Strategy class`:<br> In `Strategy class`, there is a function, `next()`, which is where you basically implement you trading strategy.
  - `data`:<br>
    I created `data` object from `bt.feeds.PandasData` where I set df as a parameter which is a Pandas Dataframe containing (`Time`, `Open`, `High`, `Low`, `Close`, `Volume`).
    You can change the way to create data object by yourself.
    <a href="https://www.backtrader.com/docu/datafeed/">Here</a> is the link to the documentation.
