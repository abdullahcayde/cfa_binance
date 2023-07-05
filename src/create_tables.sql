CREATE TABLE IF NOT EXISTS hourly (
                        id serial PRIMARY KEY,
                        id_asset NUMERIC,
                        timestamp TIMESTAMP,
                        open NUMERIC, 
                        high NUMERIC,
                        low NUMERIC,
                        close NUMERIC,
                        volume NUMERIC,
                        close_time TIMESTAMP,
                        quote_asset_volume NUMERIC,
                        number_of_trades NUMERIC,
                        taker_buy_base_asset_volume NUMERIC,
                        taker_buy_quote_asset_volume NUMERIC,
                        ignore NUMERIC
                        );

CREATE TABLE IF NOT EXISTS daily (
                        id serial PRIMARY KEY,
                        id_asset NUMERIC,
                        timestamp TIMESTAMP,
                        open NUMERIC, 
                        high NUMERIC,
                        low NUMERIC,
                        close NUMERIC,
                        volume NUMERIC,
                        close_time TIMESTAMP,
                        quote_asset_volume NUMERIC,
                        number_of_trades NUMERIC,
                        taker_buy_base_asset_volume NUMERIC,
                        taker_buy_quote_asset_volume NUMERIC,
                        ignore NUMERIC
                        );

CREATE TABLE IF NOT EXISTS weekly (
                        id serial PRIMARY KEY,
                        id_asset NUMERIC,
                        timestamp TIMESTAMP,
                        open NUMERIC, 
                        high NUMERIC,
                        low NUMERIC,
                        close NUMERIC,
                        volume NUMERIC,
                        close_time TIMESTAMP,
                        quote_asset_volume NUMERIC,
                        number_of_trades NUMERIC,
                        taker_buy_base_asset_volume NUMERIC,
                        taker_buy_quote_asset_volume NUMERIC,
                        ignore NUMERIC
                        );

CREATE TABLE IF NOT EXISTS weekly (
                        id serial PRIMARY KEY,
                        id_asset NUMERIC,
                        timestamp TIMESTAMP,
                        open NUMERIC, 
                        high NUMERIC,
                        low NUMERIC,
                        close NUMERIC,
                        volume NUMERIC,
                        close_time TIMESTAMP,
                        quote_asset_volume NUMERIC,
                        number_of_trades NUMERIC,
                        taker_buy_base_asset_volume NUMERIC,
                        taker_buy_quote_asset_volume NUMERIC,
                        ignore NUMERIC
                        );

CREATE TABLE IF NOT EXISTS monthly (
                        id serial PRIMARY KEY,
                        id_asset NUMERIC,
                        timestamp TIMESTAMP,
                        open NUMERIC, 
                        high NUMERIC,
                        low NUMERIC,
                        close NUMERIC,
                        volume NUMERIC,
                        close_time TIMESTAMP,
                        quote_asset_volume NUMERIC,
                        number_of_trades NUMERIC,
                        taker_buy_base_asset_volume NUMERIC,
                        taker_buy_quote_asset_volume NUMERIC,
                        ignore NUMERIC
                        );

CREATE TABLE IF NOT EXISTS daily_proceed (
                        id int,
                        timestamp TIMESTAMP,
                        close NUMERIC,
                        FOREIGN KEY (id) REFERENCES daily (id)
                        );