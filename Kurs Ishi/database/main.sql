CREATE DATABASE IF NOT EXISTS onlinetrade;
USE onlinetrade;

-- onlinetrade.balance definition

CREATE TABLE IF NOT EXISTS `balance` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `AZN` varchar(100) NOT NULL,
  `USD` varchar(100) NOT NULL,
  `EUR` varchar(100) NOT NULL,
  `BTC` varchar(100) NOT NULL,
  `JPY` varchar(100) NOT NULL,
  `XAU` varchar(100) NOT NULL,
  `TSLA` varchar(100) NOT NULL,
  `ETH` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- onlinetrade.cards definition

CREATE TABLE IF NOT EXISTS `cards` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `cardnum` varchar(100) NOT NULL,
  `expiration` varchar(100) NOT NULL,
  `cvc` varchar(100) NOT NULL,
  `money` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- onlinetrade.currency definition

CREATE TABLE IF NOT EXISTS `currency` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nameofcurr` varchar(100) NOT NULL,
  `value` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- onlinetrade.users definition

CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `surname` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;