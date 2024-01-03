-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 05:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `meal_box`
--

-- --------------------------------------------------------

--
-- Table structure for table `meal_box`
--

CREATE TABLE `meal_box` (
  `User_First_Name` varchar(100) NOT NULL,
  `User_Last_Name` varchar(100) NOT NULL,
  `Box_Type` varchar(100) NOT NULL,
  `Total_Box` int(3) NOT NULL,
  `Price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meal_box`
--

INSERT INTO `meal_box` (`User_First_Name`, `User_Last_Name`, `Box_Type`, `Total_Box`, `Price`) VALUES
('Siti', 'Fatimah', 'Box A', 10, 150),
('Kamal', 'Zaidi', 'Box B', 20, 500),
('Laila', 'Majnun', 'Box C', 30, 840);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
