# python.exe -m pip install --upgrade pip
# pip install stable_baselines3
# pip install pandas
# pip install numpy
# pip install finrl
# pip install matplotlib
# pip install torch
# python -m venv new_env
# new_env\Scripts\activate
# pip install torch
# D:\interview g\coding interview\DataStructure\Trade_Enviroment\.venv\Scripts\activate
# pip install alpaca_trade_api
# pip install yfinance
# pip install gym
# pip install tensorflow
# pip install tensorflow-gpu
# pip install backtrader
# pip install pyfolio

# import sys
# sys.path.append('D:\\interview g\\coding interview\\DataStructure\\Trade_Enviroment\\.venv\\Lib\\site-packages')


from finrl.config import config
from finrl.marketdata.yahoodownloader import YahooDownloader
from finrl.env.env_stocktrading import StockTradingEnv
from finrl.model.models import DRLAgent
from finrl.trade.backtest import backtest_stats, get_daily_return, get_baseline

# تنظیمات اولیه
initial_amount = 1000000  # مقدار اولیه سرمایه
transaction_cost_pct = 0.001  # هزینه تراکنش
reward_scaling = 1e-4  # مقیاس‌بندی پاداش

# بارگیری داده‌های تاریخی برای آموزش مدل
historical_data = YahooDownloader(start_date='2020-01-01',
                                  end_date='2021-01-01',
                                  ticker_list=config.DOW_30_TICKER).fetch_data()

# تنظیم محیط برای آموزش
train_env = StockTradingEnv(df=historical_data,
                            initial_amount=initial_amount,
                            transaction_cost_pct=transaction_cost_pct,
                            reward_scaling=reward_scaling)

# تعریف و آموزش عامل با استفاده از الگوریتم A2C
agent = DRLAgent(env=train_env)
model_a2c = agent.get_model('a2c')
trained_a2c = agent.train_model(model=model_a2c, tb_log_name='a2c', total_timesteps=100000)

# بارگیری داده‌های زنده برای تجارت زنده
live_data = YahooDownloader(start_date='2024-04-17',
                            end_date='2024-04-18',
                            ticker_list=config.DOW_30_TICKER).fetch_data()

# تنظیم محیط تجارت زنده
live_env = StockTradingEnv(df=live_data,
                           initial_amount=initial_amount,
                           transaction_cost_pct=transaction_cost_pct,
                           reward_scaling=reward_scaling)

# بارگذاری مدل آموزش دیده
agent = DRLAgent(env=live_env)
model = agent.load_model('a2c', 'trained_a2c.pth')

# تنظیم پارامترهای مدل برای بهینه‌سازی
model_params = {
    'gamma': 0.99,  # نرخ تخفیف
    'learning_rate': 0.0005,  # نرخ یادگیری
    'batch_size': 64,  # اندازه دسته
    # ... سایر پارامترها
}

# بهینه‌سازی مدل برای تجارت زنده
optimized_model = agent.train_model(model=model,
                                    model_params=model_params,
                                    tb_log_name='a2c_optimized',
                                    total_timesteps=50000)

# اجرای مدل در محیط تجارت زنده
trade = agent.trade(model=optimized_model, test_data=live_data)

# نظارت و بهینه‌سازی مداوم
# این بخش باید شامل کدهایی باشد که عملکرد مدل را نظارت کرده و در صورت لزوم تنظیمات را بهینه‌سازی می‌کنند.
