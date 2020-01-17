import backtrader as bt
import pandas as pd


# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.datetime(0)
        print('{}, {}'.format(dt, txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataopen = self.datas[0].open
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        self.dataclose = self.datas[0].close

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, {:.2f}'.format(self.dataclose[0]))

        if self.dataclose[0] < self.dataclose[-1]:
            # current close less than previous close

            if self.dataclose[-1] < self.dataclose[-2]:
                # previous close less than the previous close

                # BUY, BUY, BUY!!! (with all possible default parameters)
                self.log('BUY CREATE, {:.2f}'.format(self.dataclose[0]))
                self.buy()


if __name__ == '__main__':
    # csv path
    csv_path = '../data/test.csv.bz2'

    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    df = pd.read_csv(csv_path)
    df = df.set_index(pd.to_datetime(df['Time'])).drop('Time', axis=1)
    data = bt.feeds.PandasData(dataname=df)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Set oanda spread 0.008 for USD/JPY
    cerebro.broker.setcommission(commission=0.008)

    # Print out the starting conditions
    print('Starting Portfolio Value: {:.2f}'.format(cerebro.broker.getvalue()))

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: {:.2f}'.format(cerebro.broker.getvalue()))
