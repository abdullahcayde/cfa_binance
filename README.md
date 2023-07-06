# CryptoBot with Binance 

# Introduction
Today, the cryptosphere is beginning to play an increasingly significant role. Simply said, these financial markets built on Blockchain technology are highly volatile and unstable. The main objective of this project is to build a trading bot that would invest in cryptocurrency markets using a machine-learning model. Binance website is a cryptocurrency exchange platform that provides various services related to digital assets, including trading, investing, and storing cryptocurrencies. https://www.binance.com/en is the official website of Binance.
# Collecting the data
In order to gather data from Binance using a streaming architecture, we collect two types of data through the Binance API. The first type of data we retrieve is information on the prices of different markets, such as BTC-USDT and BTC-ETH. The objective is to create a generic data retrieval function that can obtain data from any market on Binance. 
To collect data from Binance using the API, we follow a series of steps to retrieve hourly, weekly, and monthly data for the "BTCUSDT" market. The API provides us with the necessary tools to access this data efficiently. Both of them are available in the Data folder.
## Getting Hourly, Weekly, and Monthly Data for "BTCUSDT" with API:
Continuing the process, we send a request to the Binance API, specifying the time interval as Hourly, Weekly, and Monthly. The API then supplies us with the most recent data for the "BTCUSDT" market. Once we have obtained the desired data from the Binance API, we store it in CSV formats for convenient and standardized data storage. Each type of data (hourly, weekly, and monthly) is saved in separate CSV files, ensuring proper organization and ease of access.
Furthermore, to facilitate efficient data management, we also store a copy of the data in a PostgreSQL database. This allows for seamless data querying and retrieval, enabling us to perform complex analyses and generate insights. The PostgreSQL database provides a robust and reliable storage solution for long-term data preservation.
## Machine learning models:
The code implements the ARIMA (AutoRegressive Integrated Moving Average) model for price prediction. It splits the data into training and test sets, trains the ARIMA model on the training data, and makes predictions for the test data. The performance of the model is evaluated using metrics such as mean absolute percentage error (MAPE). The code also includes model tuning using the auto_arima function to select optimal model parameters based on AIC (Akaike Information Criterion) and BIC (Bayesian Information Criterion) scores.
# Instruction
In order to run the code properly, please provide a .....py inside "./src" folder in this form
# Documentation for CryptoBot with Binance Dashboard and FastAPI.
# 1. Introduction:
Welcome to the CryptoBot with Binance Dashboard and FastAPI documentation. This guide is designed to help you get started with our dashboard quickly and easily. Our dashboard is a powerful tool that allows you to see the estimated price of the market in real-time and access information about cryptocurrency markets. The dashboard is designed to work well on different operating systems. Our FastAPI allows you to get more information.
# 2. Source Code:
All of our source code can be found on GitHub at

  ```
  https://github.com/abdullahcayde/cfa_binance
 ```

You can access our code and contribute to it if you like.

# 3. Setup:
## Step 1: Cloning Github Repo
To get started with our dashboard, you need to clone our Github repository to your local machine. Open your terminal and run the command:

  ```
  git clone https://github.com/abdullahcayde/cfa_binance.git
```

This will download our code to your local machine.
## Step 2: Using Docker Compose
Our dashboard uses Docker Compose to manage its containers. Open your terminal and navigate to the cfa_binance directory. Then run the following command:

  ``` 
  sudo docker-compose up --build -d
``` 
## Step 3: Checking Containers
Run the following command to check if all containers are up and running:
 ```
  docker ps
 ```
You should see containers: my_postgres

## Step 4: Loading Initial Data
## Step 5: Accessing the container locally from a web browser:
 ```
FastAPI: localhost:9090/docs
PostgreSQL: localhost:5434 User:abdullahcay PW:12345 db:binance
 ```
 
# 4. Usage:
## FastAPI
All endpoints are described in docs/...
 ```
  /
  /api/assets
  /api/predict/{assetid:int}
  /api/predictall
 ```
# 5. Conclusion:
We hope this guide has helped you get started with our CryptoBot with Binance Dashboard and FastAPI. 

