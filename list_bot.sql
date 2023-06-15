-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 15 2023 г., 19:59
-- Версия сервера: 10.4.28-MariaDB
-- Версия PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `list_bot`
--

-- --------------------------------------------------------

--
-- Структура таблицы `list_table`
--

CREATE TABLE `list_table` (
  `id` int(11) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `product_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `name_table`
--

CREATE TABLE `name_table` (
  `id` int(255) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `user_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `name_table`
--

INSERT INTO `name_table` (`id`, `user_id`, `user_name`) VALUES
(10, '974951192 ', 'Серёжа'),
(12, '511270281 ', 'Ксю'),
(13, '5187318518 ', 'Светлана'),
(14, '1081865782 ', 'Мария'),
(15, '1448971733 ', 'GIGACHAD');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `list_table`
--
ALTER TABLE `list_table`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `name_table`
--
ALTER TABLE `name_table`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `list_table`
--
ALTER TABLE `list_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT для таблицы `name_table`
--
ALTER TABLE `name_table`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
