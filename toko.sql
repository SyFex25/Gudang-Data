-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2023 at 04:44 PM
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
-- Database: `toko`
--

-- --------------------------------------------------------

--
-- Table structure for table `cashier_dimension`
--

CREATE TABLE `cashier_dimension` (
  `cashier_key` varchar(10) NOT NULL,
  `cashier_employee_id` varchar(10) DEFAULT NULL,
  `cashier_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cashier_dimension`
--

INSERT INTO `cashier_dimension` (`cashier_key`, `cashier_employee_id`, `cashier_name`) VALUES
('CASHIER103', '212100163', 'Floyd'),
('CASHIER115', '212100165', 'Alex'),
('CASHIER167', '212100159', 'John Doe'),
('CASHIER177', '212100162', 'Dustin'),
('CASHIER208', '212100164', 'Charles'),
('CASHIER222', '212100160', 'Justin'),
('CASHIER262', '212100161', 'Michael'),
('CASHIER317', '212100166', 'Leon');

-- --------------------------------------------------------

--
-- Table structure for table `date_dimension`
--

CREATE TABLE `date_dimension` (
  `date_key` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `full_date_desc` varchar(255) DEFAULT NULL,
  `day_of_week` varchar(255) DEFAULT NULL,
  `calendar_month` varchar(255) DEFAULT NULL,
  `calendar_quarter` varchar(255) DEFAULT NULL,
  `calendar_year` int(11) DEFAULT NULL,
  `fiscal_year_month` varchar(255) DEFAULT NULL,
  `holiday_indicator` varchar(255) DEFAULT NULL,
  `weekday_indicator` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `date_dimension`
--

INSERT INTO `date_dimension` (`date_key`, `date`, `full_date_desc`, `day_of_week`, `calendar_month`, `calendar_quarter`, `calendar_year`, `fiscal_year_month`, `holiday_indicator`, `weekday_indicator`) VALUES
(20230101, '2023-01-01', 'January 01, 2023', 'Sunday', 'January', 'Q1', 2023, 'F2023-01', 'Holiday', 'Weekend'),
(20230102, '2023-01-02', 'January 02, 2023', 'Monday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230103, '2023-01-03', 'January 03, 2023', 'Tuesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230104, '2023-01-04', 'January 04, 2023', 'Wednesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230105, '2023-01-05', 'January 05, 2023', 'Thursday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230106, '2023-01-06', 'January 06, 2023', 'Friday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230107, '2023-01-07', 'January 07, 2023', 'Saturday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230108, '2023-01-08', 'January 08, 2023', 'Sunday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230109, '2023-01-09', 'January 09, 2023', 'Monday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230110, '2023-01-10', 'January 10, 2023', 'Tuesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230111, '2023-01-11', 'January 11, 2023', 'Wednesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230112, '2023-01-12', 'January 12, 2023', 'Thursday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230113, '2023-01-13', 'January 13, 2023', 'Friday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230114, '2023-01-14', 'January 14, 2023', 'Saturday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230115, '2023-01-15', 'January 15, 2023', 'Sunday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230116, '2023-01-16', 'January 16, 2023', 'Monday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230117, '2023-01-17', 'January 17, 2023', 'Tuesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230118, '2023-01-18', 'January 18, 2023', 'Wednesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230119, '2023-01-19', 'January 19, 2023', 'Thursday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230120, '2023-01-20', 'January 20, 2023', 'Friday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230121, '2023-01-21', 'January 21, 2023', 'Saturday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230122, '2023-01-22', 'January 22, 2023', 'Sunday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230123, '2023-01-23', 'January 23, 2023', 'Monday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230124, '2023-01-24', 'January 24, 2023', 'Tuesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230125, '2023-01-25', 'January 25, 2023', 'Wednesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230126, '2023-01-26', 'January 26, 2023', 'Thursday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230127, '2023-01-27', 'January 27, 2023', 'Friday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230128, '2023-01-28', 'January 28, 2023', 'Saturday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230129, '2023-01-29', 'January 29, 2023', 'Sunday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekend'),
(20230130, '2023-01-30', 'January 30, 2023', 'Monday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230131, '2023-01-31', 'January 31, 2023', 'Tuesday', 'January', 'Q1', 2023, 'F2023-01', 'Non-Holiday', 'Weekday'),
(20230201, '2023-02-01', 'February 01, 2023', 'Wednesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230202, '2023-02-02', 'February 02, 2023', 'Thursday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230203, '2023-02-03', 'February 03, 2023', 'Friday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230204, '2023-02-04', 'February 04, 2023', 'Saturday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230205, '2023-02-05', 'February 05, 2023', 'Sunday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230206, '2023-02-06', 'February 06, 2023', 'Monday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230207, '2023-02-07', 'February 07, 2023', 'Tuesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230208, '2023-02-08', 'February 08, 2023', 'Wednesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230209, '2023-02-09', 'February 09, 2023', 'Thursday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230210, '2023-02-10', 'February 10, 2023', 'Friday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230211, '2023-02-11', 'February 11, 2023', 'Saturday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230212, '2023-02-12', 'February 12, 2023', 'Sunday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230213, '2023-02-13', 'February 13, 2023', 'Monday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230214, '2023-02-14', 'February 14, 2023', 'Tuesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230215, '2023-02-15', 'February 15, 2023', 'Wednesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230216, '2023-02-16', 'February 16, 2023', 'Thursday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230217, '2023-02-17', 'February 17, 2023', 'Friday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230218, '2023-02-18', 'February 18, 2023', 'Saturday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230219, '2023-02-19', 'February 19, 2023', 'Sunday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230220, '2023-02-20', 'February 20, 2023', 'Monday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230221, '2023-02-21', 'February 21, 2023', 'Tuesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230222, '2023-02-22', 'February 22, 2023', 'Wednesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230223, '2023-02-23', 'February 23, 2023', 'Thursday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230224, '2023-02-24', 'February 24, 2023', 'Friday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230225, '2023-02-25', 'February 25, 2023', 'Saturday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230226, '2023-02-26', 'February 26, 2023', 'Sunday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekend'),
(20230227, '2023-02-27', 'February 27, 2023', 'Monday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230228, '2023-02-28', 'February 28, 2023', 'Tuesday', 'February', 'Q1', 2023, 'F2023-02', 'Non-Holiday', 'Weekday'),
(20230301, '2023-03-01', 'March 01, 2023', 'Wednesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230302, '2023-03-02', 'March 02, 2023', 'Thursday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230303, '2023-03-03', 'March 03, 2023', 'Friday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230304, '2023-03-04', 'March 04, 2023', 'Saturday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230305, '2023-03-05', 'March 05, 2023', 'Sunday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230306, '2023-03-06', 'March 06, 2023', 'Monday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230307, '2023-03-07', 'March 07, 2023', 'Tuesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230308, '2023-03-08', 'March 08, 2023', 'Wednesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230309, '2023-03-09', 'March 09, 2023', 'Thursday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230310, '2023-03-10', 'March 10, 2023', 'Friday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230311, '2023-03-11', 'March 11, 2023', 'Saturday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230312, '2023-03-12', 'March 12, 2023', 'Sunday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230313, '2023-03-13', 'March 13, 2023', 'Monday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230314, '2023-03-14', 'March 14, 2023', 'Tuesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230315, '2023-03-15', 'March 15, 2023', 'Wednesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230316, '2023-03-16', 'March 16, 2023', 'Thursday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230317, '2023-03-17', 'March 17, 2023', 'Friday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230318, '2023-03-18', 'March 18, 2023', 'Saturday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230319, '2023-03-19', 'March 19, 2023', 'Sunday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230320, '2023-03-20', 'March 20, 2023', 'Monday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230321, '2023-03-21', 'March 21, 2023', 'Tuesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230322, '2023-03-22', 'March 22, 2023', 'Wednesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230323, '2023-03-23', 'March 23, 2023', 'Thursday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230324, '2023-03-24', 'March 24, 2023', 'Friday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230325, '2023-03-25', 'March 25, 2023', 'Saturday', 'March', 'Q1', 2023, 'F2023-03', 'Holiday', 'Weekend'),
(20230326, '2023-03-26', 'March 26, 2023', 'Sunday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekend'),
(20230327, '2023-03-27', 'March 27, 2023', 'Monday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230328, '2023-03-28', 'March 28, 2023', 'Tuesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230329, '2023-03-29', 'March 29, 2023', 'Wednesday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230330, '2023-03-30', 'March 30, 2023', 'Thursday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230331, '2023-03-31', 'March 31, 2023', 'Friday', 'March', 'Q1', 2023, 'F2023-03', 'Non-Holiday', 'Weekday'),
(20230401, '2023-04-01', 'April 01, 2023', 'Saturday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230402, '2023-04-02', 'April 02, 2023', 'Sunday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230403, '2023-04-03', 'April 03, 2023', 'Monday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230404, '2023-04-04', 'April 04, 2023', 'Tuesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230405, '2023-04-05', 'April 05, 2023', 'Wednesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230406, '2023-04-06', 'April 06, 2023', 'Thursday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230407, '2023-04-07', 'April 07, 2023', 'Friday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230408, '2023-04-08', 'April 08, 2023', 'Saturday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230409, '2023-04-09', 'April 09, 2023', 'Sunday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230410, '2023-04-10', 'April 10, 2023', 'Monday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230411, '2023-04-11', 'April 11, 2023', 'Tuesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230412, '2023-04-12', 'April 12, 2023', 'Wednesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230413, '2023-04-13', 'April 13, 2023', 'Thursday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230414, '2023-04-14', 'April 14, 2023', 'Friday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230415, '2023-04-15', 'April 15, 2023', 'Saturday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230416, '2023-04-16', 'April 16, 2023', 'Sunday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230417, '2023-04-17', 'April 17, 2023', 'Monday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230418, '2023-04-18', 'April 18, 2023', 'Tuesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230419, '2023-04-19', 'April 19, 2023', 'Wednesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230420, '2023-04-20', 'April 20, 2023', 'Thursday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekday'),
(20230421, '2023-04-21', 'April 21, 2023', 'Friday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekday'),
(20230422, '2023-04-22', 'April 22, 2023', 'Saturday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekend'),
(20230423, '2023-04-23', 'April 23, 2023', 'Sunday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekend'),
(20230424, '2023-04-24', 'April 24, 2023', 'Monday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekday'),
(20230425, '2023-04-25', 'April 25, 2023', 'Tuesday', 'April', 'Q2', 2023, 'F2023-04', 'Holiday', 'Weekday'),
(20230426, '2023-04-26', 'April 26, 2023', 'Wednesday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230427, '2023-04-27', 'April 27, 2023', 'Thursday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230428, '2023-04-28', 'April 28, 2023', 'Friday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekday'),
(20230429, '2023-04-29', 'April 29, 2023', 'Saturday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230430, '2023-04-30', 'April 30, 2023', 'Sunday', 'April', 'Q2', 2023, 'F2023-04', 'Non-Holiday', 'Weekend'),
(20230501, '2023-05-01', 'May 01, 2023', 'Monday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230502, '2023-05-02', 'May 02, 2023', 'Tuesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230503, '2023-05-03', 'May 03, 2023', 'Wednesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230504, '2023-05-04', 'May 04, 2023', 'Thursday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230505, '2023-05-05', 'May 05, 2023', 'Friday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230506, '2023-05-06', 'May 06, 2023', 'Saturday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230507, '2023-05-07', 'May 07, 2023', 'Sunday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230508, '2023-05-08', 'May 08, 2023', 'Monday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230509, '2023-05-09', 'May 09, 2023', 'Tuesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230510, '2023-05-10', 'May 10, 2023', 'Wednesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230511, '2023-05-11', 'May 11, 2023', 'Thursday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230512, '2023-05-12', 'May 12, 2023', 'Friday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230513, '2023-05-13', 'May 13, 2023', 'Saturday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230514, '2023-05-14', 'May 14, 2023', 'Sunday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230515, '2023-05-15', 'May 15, 2023', 'Monday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230516, '2023-05-16', 'May 16, 2023', 'Tuesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230517, '2023-05-17', 'May 17, 2023', 'Wednesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230518, '2023-05-18', 'May 18, 2023', 'Thursday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230519, '2023-05-19', 'May 19, 2023', 'Friday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230520, '2023-05-20', 'May 20, 2023', 'Saturday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230521, '2023-05-21', 'May 21, 2023', 'Sunday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230522, '2023-05-22', 'May 22, 2023', 'Monday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230523, '2023-05-23', 'May 23, 2023', 'Tuesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230524, '2023-05-24', 'May 24, 2023', 'Wednesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230525, '2023-05-25', 'May 25, 2023', 'Thursday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230526, '2023-05-26', 'May 26, 2023', 'Friday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230527, '2023-05-27', 'May 27, 2023', 'Saturday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230528, '2023-05-28', 'May 28, 2023', 'Sunday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekend'),
(20230529, '2023-05-29', 'May 29, 2023', 'Monday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230530, '2023-05-30', 'May 30, 2023', 'Tuesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230531, '2023-05-31', 'May 31, 2023', 'Wednesday', 'May', 'Q2', 2023, 'F2023-05', 'Non-Holiday', 'Weekday'),
(20230601, '2023-06-01', 'June 01, 2023', 'Thursday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230602, '2023-06-02', 'June 02, 2023', 'Friday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230603, '2023-06-03', 'June 03, 2023', 'Saturday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230604, '2023-06-04', 'June 04, 2023', 'Sunday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230605, '2023-06-05', 'June 05, 2023', 'Monday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230606, '2023-06-06', 'June 06, 2023', 'Tuesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230607, '2023-06-07', 'June 07, 2023', 'Wednesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230608, '2023-06-08', 'June 08, 2023', 'Thursday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230609, '2023-06-09', 'June 09, 2023', 'Friday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230610, '2023-06-10', 'June 10, 2023', 'Saturday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230611, '2023-06-11', 'June 11, 2023', 'Sunday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230612, '2023-06-12', 'June 12, 2023', 'Monday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230613, '2023-06-13', 'June 13, 2023', 'Tuesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230614, '2023-06-14', 'June 14, 2023', 'Wednesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230615, '2023-06-15', 'June 15, 2023', 'Thursday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230616, '2023-06-16', 'June 16, 2023', 'Friday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230617, '2023-06-17', 'June 17, 2023', 'Saturday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230618, '2023-06-18', 'June 18, 2023', 'Sunday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230619, '2023-06-19', 'June 19, 2023', 'Monday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230620, '2023-06-20', 'June 20, 2023', 'Tuesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230621, '2023-06-21', 'June 21, 2023', 'Wednesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230622, '2023-06-22', 'June 22, 2023', 'Thursday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230623, '2023-06-23', 'June 23, 2023', 'Friday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230624, '2023-06-24', 'June 24, 2023', 'Saturday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230625, '2023-06-25', 'June 25, 2023', 'Sunday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekend'),
(20230626, '2023-06-26', 'June 26, 2023', 'Monday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230627, '2023-06-27', 'June 27, 2023', 'Tuesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230628, '2023-06-28', 'June 28, 2023', 'Wednesday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230629, '2023-06-29', 'June 29, 2023', 'Thursday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230630, '2023-06-30', 'June 30, 2023', 'Friday', 'June', 'Q2', 2023, 'F2023-06', 'Non-Holiday', 'Weekday'),
(20230701, '2023-07-01', 'July 01, 2023', 'Saturday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230702, '2023-07-02', 'July 02, 2023', 'Sunday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230703, '2023-07-03', 'July 03, 2023', 'Monday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230704, '2023-07-04', 'July 04, 2023', 'Tuesday', 'July', 'Q3', 2023, 'F2023-07', 'Holiday', 'Weekday'),
(20230705, '2023-07-05', 'July 05, 2023', 'Wednesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230706, '2023-07-06', 'July 06, 2023', 'Thursday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230707, '2023-07-07', 'July 07, 2023', 'Friday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230708, '2023-07-08', 'July 08, 2023', 'Saturday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230709, '2023-07-09', 'July 09, 2023', 'Sunday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230710, '2023-07-10', 'July 10, 2023', 'Monday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230711, '2023-07-11', 'July 11, 2023', 'Tuesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230712, '2023-07-12', 'July 12, 2023', 'Wednesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230713, '2023-07-13', 'July 13, 2023', 'Thursday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230714, '2023-07-14', 'July 14, 2023', 'Friday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230715, '2023-07-15', 'July 15, 2023', 'Saturday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230716, '2023-07-16', 'July 16, 2023', 'Sunday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230717, '2023-07-17', 'July 17, 2023', 'Monday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230718, '2023-07-18', 'July 18, 2023', 'Tuesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230719, '2023-07-19', 'July 19, 2023', 'Wednesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230720, '2023-07-20', 'July 20, 2023', 'Thursday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230721, '2023-07-21', 'July 21, 2023', 'Friday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230722, '2023-07-22', 'July 22, 2023', 'Saturday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230723, '2023-07-23', 'July 23, 2023', 'Sunday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230724, '2023-07-24', 'July 24, 2023', 'Monday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230725, '2023-07-25', 'July 25, 2023', 'Tuesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230726, '2023-07-26', 'July 26, 2023', 'Wednesday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230727, '2023-07-27', 'July 27, 2023', 'Thursday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230728, '2023-07-28', 'July 28, 2023', 'Friday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230729, '2023-07-29', 'July 29, 2023', 'Saturday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230730, '2023-07-30', 'July 30, 2023', 'Sunday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekend'),
(20230731, '2023-07-31', 'July 31, 2023', 'Monday', 'July', 'Q3', 2023, 'F2023-07', 'Non-Holiday', 'Weekday'),
(20230801, '2023-08-01', 'August 01, 2023', 'Tuesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230802, '2023-08-02', 'August 02, 2023', 'Wednesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230803, '2023-08-03', 'August 03, 2023', 'Thursday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230804, '2023-08-04', 'August 04, 2023', 'Friday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230805, '2023-08-05', 'August 05, 2023', 'Saturday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230806, '2023-08-06', 'August 06, 2023', 'Sunday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230807, '2023-08-07', 'August 07, 2023', 'Monday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230808, '2023-08-08', 'August 08, 2023', 'Tuesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230809, '2023-08-09', 'August 09, 2023', 'Wednesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230810, '2023-08-10', 'August 10, 2023', 'Thursday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230811, '2023-08-11', 'August 11, 2023', 'Friday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230812, '2023-08-12', 'August 12, 2023', 'Saturday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230813, '2023-08-13', 'August 13, 2023', 'Sunday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230814, '2023-08-14', 'August 14, 2023', 'Monday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230815, '2023-08-15', 'August 15, 2023', 'Tuesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230816, '2023-08-16', 'August 16, 2023', 'Wednesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230817, '2023-08-17', 'August 17, 2023', 'Thursday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230818, '2023-08-18', 'August 18, 2023', 'Friday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230819, '2023-08-19', 'August 19, 2023', 'Saturday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230820, '2023-08-20', 'August 20, 2023', 'Sunday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230821, '2023-08-21', 'August 21, 2023', 'Monday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230822, '2023-08-22', 'August 22, 2023', 'Tuesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230823, '2023-08-23', 'August 23, 2023', 'Wednesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230824, '2023-08-24', 'August 24, 2023', 'Thursday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230825, '2023-08-25', 'August 25, 2023', 'Friday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230826, '2023-08-26', 'August 26, 2023', 'Saturday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230827, '2023-08-27', 'August 27, 2023', 'Sunday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekend'),
(20230828, '2023-08-28', 'August 28, 2023', 'Monday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230829, '2023-08-29', 'August 29, 2023', 'Tuesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230830, '2023-08-30', 'August 30, 2023', 'Wednesday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230831, '2023-08-31', 'August 31, 2023', 'Thursday', 'August', 'Q3', 2023, 'F2023-08', 'Non-Holiday', 'Weekday'),
(20230901, '2023-09-01', 'September 01, 2023', 'Friday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230902, '2023-09-02', 'September 02, 2023', 'Saturday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230903, '2023-09-03', 'September 03, 2023', 'Sunday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230904, '2023-09-04', 'September 04, 2023', 'Monday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230905, '2023-09-05', 'September 05, 2023', 'Tuesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230906, '2023-09-06', 'September 06, 2023', 'Wednesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230907, '2023-09-07', 'September 07, 2023', 'Thursday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230908, '2023-09-08', 'September 08, 2023', 'Friday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230909, '2023-09-09', 'September 09, 2023', 'Saturday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230910, '2023-09-10', 'September 10, 2023', 'Sunday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230911, '2023-09-11', 'September 11, 2023', 'Monday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230912, '2023-09-12', 'September 12, 2023', 'Tuesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230913, '2023-09-13', 'September 13, 2023', 'Wednesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230914, '2023-09-14', 'September 14, 2023', 'Thursday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230915, '2023-09-15', 'September 15, 2023', 'Friday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230916, '2023-09-16', 'September 16, 2023', 'Saturday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230917, '2023-09-17', 'September 17, 2023', 'Sunday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230918, '2023-09-18', 'September 18, 2023', 'Monday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230919, '2023-09-19', 'September 19, 2023', 'Tuesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230920, '2023-09-20', 'September 20, 2023', 'Wednesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230921, '2023-09-21', 'September 21, 2023', 'Thursday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230922, '2023-09-22', 'September 22, 2023', 'Friday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230923, '2023-09-23', 'September 23, 2023', 'Saturday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230924, '2023-09-24', 'September 24, 2023', 'Sunday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20230925, '2023-09-25', 'September 25, 2023', 'Monday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230926, '2023-09-26', 'September 26, 2023', 'Tuesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230927, '2023-09-27', 'September 27, 2023', 'Wednesday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230928, '2023-09-28', 'September 28, 2023', 'Thursday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230929, '2023-09-29', 'September 29, 2023', 'Friday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekday'),
(20230930, '2023-09-30', 'September 30, 2023', 'Saturday', 'September', 'Q3', 2023, 'F2023-09', 'Non-Holiday', 'Weekend'),
(20231001, '2023-10-01', 'October 01, 2023', 'Sunday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231002, '2023-10-02', 'October 02, 2023', 'Monday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231003, '2023-10-03', 'October 03, 2023', 'Tuesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231004, '2023-10-04', 'October 04, 2023', 'Wednesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231005, '2023-10-05', 'October 05, 2023', 'Thursday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231006, '2023-10-06', 'October 06, 2023', 'Friday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231007, '2023-10-07', 'October 07, 2023', 'Saturday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231008, '2023-10-08', 'October 08, 2023', 'Sunday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231009, '2023-10-09', 'October 09, 2023', 'Monday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231010, '2023-10-10', 'October 10, 2023', 'Tuesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231011, '2023-10-11', 'October 11, 2023', 'Wednesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231012, '2023-10-12', 'October 12, 2023', 'Thursday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231013, '2023-10-13', 'October 13, 2023', 'Friday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231014, '2023-10-14', 'October 14, 2023', 'Saturday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231015, '2023-10-15', 'October 15, 2023', 'Sunday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231016, '2023-10-16', 'October 16, 2023', 'Monday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231017, '2023-10-17', 'October 17, 2023', 'Tuesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231018, '2023-10-18', 'October 18, 2023', 'Wednesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231019, '2023-10-19', 'October 19, 2023', 'Thursday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231020, '2023-10-20', 'October 20, 2023', 'Friday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231021, '2023-10-21', 'October 21, 2023', 'Saturday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231022, '2023-10-22', 'October 22, 2023', 'Sunday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231023, '2023-10-23', 'October 23, 2023', 'Monday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231024, '2023-10-24', 'October 24, 2023', 'Tuesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231025, '2023-10-25', 'October 25, 2023', 'Wednesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231026, '2023-10-26', 'October 26, 2023', 'Thursday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231027, '2023-10-27', 'October 27, 2023', 'Friday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231028, '2023-10-28', 'October 28, 2023', 'Saturday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231029, '2023-10-29', 'October 29, 2023', 'Sunday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekend'),
(20231030, '2023-10-30', 'October 30, 2023', 'Monday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231031, '2023-10-31', 'October 31, 2023', 'Tuesday', 'October', 'Q4', 2023, 'F2023-10', 'Non-Holiday', 'Weekday'),
(20231101, '2023-11-01', 'November 01, 2023', 'Wednesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231102, '2023-11-02', 'November 02, 2023', 'Thursday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231103, '2023-11-03', 'November 03, 2023', 'Friday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231104, '2023-11-04', 'November 04, 2023', 'Saturday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231105, '2023-11-05', 'November 05, 2023', 'Sunday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231106, '2023-11-06', 'November 06, 2023', 'Monday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231107, '2023-11-07', 'November 07, 2023', 'Tuesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231108, '2023-11-08', 'November 08, 2023', 'Wednesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231109, '2023-11-09', 'November 09, 2023', 'Thursday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231110, '2023-11-10', 'November 10, 2023', 'Friday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231111, '2023-11-11', 'November 11, 2023', 'Saturday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231112, '2023-11-12', 'November 12, 2023', 'Sunday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231113, '2023-11-13', 'November 13, 2023', 'Monday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231114, '2023-11-14', 'November 14, 2023', 'Tuesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231115, '2023-11-15', 'November 15, 2023', 'Wednesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231116, '2023-11-16', 'November 16, 2023', 'Thursday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231117, '2023-11-17', 'November 17, 2023', 'Friday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231118, '2023-11-18', 'November 18, 2023', 'Saturday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231119, '2023-11-19', 'November 19, 2023', 'Sunday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231120, '2023-11-20', 'November 20, 2023', 'Monday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231121, '2023-11-21', 'November 21, 2023', 'Tuesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231122, '2023-11-22', 'November 22, 2023', 'Wednesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231123, '2023-11-23', 'November 23, 2023', 'Thursday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231124, '2023-11-24', 'November 24, 2023', 'Friday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231125, '2023-11-25', 'November 25, 2023', 'Saturday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231126, '2023-11-26', 'November 26, 2023', 'Sunday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekend'),
(20231127, '2023-11-27', 'November 27, 2023', 'Monday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231128, '2023-11-28', 'November 28, 2023', 'Tuesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231129, '2023-11-29', 'November 29, 2023', 'Wednesday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231130, '2023-11-30', 'November 30, 2023', 'Thursday', 'November', 'Q4', 2023, 'F2023-11', 'Non-Holiday', 'Weekday'),
(20231201, '2023-12-01', 'December 01, 2023', 'Friday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231202, '2023-12-02', 'December 02, 2023', 'Saturday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231203, '2023-12-03', 'December 03, 2023', 'Sunday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231204, '2023-12-04', 'December 04, 2023', 'Monday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231205, '2023-12-05', 'December 05, 2023', 'Tuesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231206, '2023-12-06', 'December 06, 2023', 'Wednesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231207, '2023-12-07', 'December 07, 2023', 'Thursday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231208, '2023-12-08', 'December 08, 2023', 'Friday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231209, '2023-12-09', 'December 09, 2023', 'Saturday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231210, '2023-12-10', 'December 10, 2023', 'Sunday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231211, '2023-12-11', 'December 11, 2023', 'Monday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231212, '2023-12-12', 'December 12, 2023', 'Tuesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231213, '2023-12-13', 'December 13, 2023', 'Wednesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231214, '2023-12-14', 'December 14, 2023', 'Thursday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231215, '2023-12-15', 'December 15, 2023', 'Friday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231216, '2023-12-16', 'December 16, 2023', 'Saturday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231217, '2023-12-17', 'December 17, 2023', 'Sunday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231218, '2023-12-18', 'December 18, 2023', 'Monday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231219, '2023-12-19', 'December 19, 2023', 'Tuesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231220, '2023-12-20', 'December 20, 2023', 'Wednesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231221, '2023-12-21', 'December 21, 2023', 'Thursday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231222, '2023-12-22', 'December 22, 2023', 'Friday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231223, '2023-12-23', 'December 23, 2023', 'Saturday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231224, '2023-12-24', 'December 24, 2023', 'Sunday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231225, '2023-12-25', 'December 25, 2023', 'Monday', 'December', 'Q4', 2023, 'F2023-12', 'Holiday', 'Weekday'),
(20231226, '2023-12-26', 'December 26, 2023', 'Tuesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231227, '2023-12-27', 'December 27, 2023', 'Wednesday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231228, '2023-12-28', 'December 28, 2023', 'Thursday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231229, '2023-12-29', 'December 29, 2023', 'Friday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekday'),
(20231230, '2023-12-30', 'December 30, 2023', 'Saturday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend'),
(20231231, '2023-12-31', 'December 31, 2023', 'Sunday', 'December', 'Q4', 2023, 'F2023-12', 'Non-Holiday', 'Weekend');

-- --------------------------------------------------------

--
-- Table structure for table `historic_retail_inventory_snapshot_fact`
--

CREATE TABLE `historic_retail_inventory_snapshot_fact` (
  `snapshot_key` int(11) NOT NULL,
  `date_key` int(11) DEFAULT NULL,
  `product_key` varchar(5) DEFAULT NULL,
  `store_key` varchar(5) DEFAULT NULL,
  `quantity_on_hand` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `historic_retail_inventory_snapshot_fact`
--

INSERT INTO `historic_retail_inventory_snapshot_fact` (`snapshot_key`, `date_key`, `product_key`, `store_key`, `quantity_on_hand`) VALUES
(1, 20230327, '10354', '2123', 59),
(2, 20230327, '10796', '2123', 72),
(3, 20230327, '11718', '2123', 99),
(4, 20230327, '12341', '2123', 95),
(5, 20230327, '14205', '2123', 60),
(6, 20230327, '10354', '2124', 57),
(7, 20230327, '10796', '2124', 90),
(8, 20230327, '11718', '2124', 63),
(9, 20230327, '12341', '2124', 53),
(10, 20230327, '14205', '2124', 95),
(11, 20230327, '10354', '2125', 75),
(12, 20230327, '10796', '2125', 94),
(13, 20230327, '11718', '2125', 77),
(14, 20230327, '12341', '2125', 58),
(15, 20230327, '14205', '2125', 83),
(16, 20230327, '10354', '2126', 78),
(17, 20230327, '10796', '2126', 75),
(18, 20230327, '11718', '2126', 61),
(19, 20230327, '12341', '2126', 55),
(20, 20230327, '14205', '2126', 91),
(21, 20230327, '10354', '2127', 99),
(22, 20230327, '10796', '2127', 53),
(23, 20230327, '11718', '2127', 59),
(24, 20230327, '12341', '2127', 58),
(25, 20230327, '14205', '2127', 81),
(26, 20230328, '10354', '2123', 66),
(27, 20230328, '10796', '2123', 71),
(28, 20230328, '11718', '2123', 77),
(29, 20230328, '12341', '2123', 88),
(30, 20230328, '14205', '2123', 71),
(31, 20230328, '10354', '2124', 56),
(32, 20230328, '10796', '2124', 56),
(33, 20230328, '11718', '2124', 60),
(34, 20230328, '12341', '2124', 56),
(35, 20230328, '14205', '2124', 82),
(36, 20230328, '10354', '2125', 75),
(37, 20230328, '10796', '2125', 54),
(38, 20230328, '11718', '2125', 87),
(39, 20230328, '12341', '2125', 77),
(40, 20230328, '14205', '2125', 54),
(41, 20230328, '10354', '2126', 59),
(42, 20230328, '10796', '2126', 74),
(43, 20230328, '11718', '2126', 86),
(44, 20230328, '12341', '2126', 59),
(45, 20230328, '14205', '2126', 74),
(46, 20230328, '10354', '2127', 72),
(47, 20230328, '10796', '2127', 53),
(48, 20230328, '11718', '2127', 72),
(49, 20230328, '12341', '2127', 50),
(50, 20230328, '14205', '2127', 80),
(51, 20230329, '10354', '2123', 83),
(52, 20230329, '10796', '2123', 78),
(53, 20230329, '11718', '2123', 99),
(54, 20230329, '12341', '2123', 93),
(55, 20230329, '14205', '2123', 98),
(56, 20230329, '10354', '2124', 79),
(57, 20230329, '10796', '2124', 85),
(58, 20230329, '11718', '2124', 56),
(59, 20230329, '12341', '2124', 50),
(60, 20230329, '14205', '2124', 99),
(61, 20230329, '10354', '2125', 99),
(62, 20230329, '10796', '2125', 94),
(63, 20230329, '11718', '2125', 67),
(64, 20230329, '12341', '2125', 89),
(65, 20230329, '14205', '2125', 79),
(66, 20230329, '10354', '2126', 75),
(67, 20230329, '10796', '2126', 56),
(68, 20230329, '11718', '2126', 92),
(69, 20230329, '12341', '2126', 80),
(70, 20230329, '14205', '2126', 86),
(71, 20230329, '10354', '2127', 98),
(72, 20230329, '10796', '2127', 62),
(73, 20230329, '11718', '2127', 54),
(74, 20230329, '12341', '2127', 62),
(75, 20230329, '14205', '2127', 76),
(76, 20230330, '10354', '2123', 75),
(77, 20230330, '10796', '2123', 81),
(78, 20230330, '11718', '2123', 92),
(79, 20230330, '12341', '2123', 80),
(80, 20230330, '14205', '2123', 51),
(81, 20230330, '10354', '2124', 54),
(82, 20230330, '10796', '2124', 54),
(83, 20230330, '11718', '2124', 66),
(84, 20230330, '12341', '2124', 66),
(85, 20230330, '14205', '2124', 56),
(86, 20230330, '10354', '2125', 87),
(87, 20230330, '10796', '2125', 50),
(88, 20230330, '11718', '2125', 98),
(89, 20230330, '12341', '2125', 62),
(90, 20230330, '14205', '2125', 62),
(91, 20230330, '10354', '2126', 69),
(92, 20230330, '10796', '2126', 85),
(93, 20230330, '11718', '2126', 63),
(94, 20230330, '12341', '2126', 74),
(95, 20230330, '14205', '2126', 71),
(96, 20230330, '10354', '2127', 74),
(97, 20230330, '10796', '2127', 51),
(98, 20230330, '11718', '2127', 83),
(99, 20230330, '12341', '2127', 93),
(100, 20230330, '14205', '2127', 100),
(101, 20230331, '10354', '2123', 53),
(102, 20230331, '10796', '2123', 76),
(103, 20230331, '11718', '2123', 57),
(104, 20230331, '12341', '2123', 63),
(105, 20230331, '14205', '2123', 97),
(106, 20230331, '10354', '2124', 97),
(107, 20230331, '10796', '2124', 50),
(108, 20230331, '11718', '2124', 63),
(109, 20230331, '12341', '2124', 99),
(110, 20230331, '14205', '2124', 66),
(111, 20230331, '10354', '2125', 53),
(112, 20230331, '10796', '2125', 84),
(113, 20230331, '11718', '2125', 79),
(114, 20230331, '12341', '2125', 60),
(115, 20230331, '14205', '2125', 58),
(116, 20230331, '10354', '2126', 68),
(117, 20230331, '10796', '2126', 86),
(118, 20230331, '11718', '2126', 93),
(119, 20230331, '12341', '2126', 55),
(120, 20230331, '14205', '2126', 86),
(121, 20230331, '10354', '2127', 80),
(122, 20230331, '10796', '2127', 50),
(123, 20230331, '11718', '2127', 65),
(124, 20230331, '12341', '2127', 57),
(125, 20230331, '14205', '2127', 62);

-- --------------------------------------------------------

--
-- Table structure for table `inventory_receipt_accumulating_fact`
--

CREATE TABLE `inventory_receipt_accumulating_fact` (
  `product_lot_receipt_number` int(11) NOT NULL,
  `date_received_key` int(11) DEFAULT NULL,
  `date_inspected_key` int(11) DEFAULT NULL,
  `date_bin_placement_key` int(11) DEFAULT NULL,
  `date_initial_shipment_key` int(11) DEFAULT NULL,
  `date_last_shipment_key` int(11) DEFAULT NULL,
  `product_key` varchar(5) DEFAULT NULL,
  `warehouse_key` int(11) DEFAULT NULL,
  `vendor_key` int(11) DEFAULT NULL,
  `quantity_received` int(11) DEFAULT NULL,
  `quantity_inspected` int(11) DEFAULT NULL,
  `quantity_returned_to_vendor` int(11) DEFAULT NULL,
  `quantity_placed_in_bin` int(11) DEFAULT NULL,
  `quantity_shipped_to_customer` int(11) DEFAULT NULL,
  `quantity_returned_by_customer` int(11) DEFAULT NULL,
  `quantity_returned_to_inventory` int(11) DEFAULT NULL,
  `quantity_damaged` int(11) DEFAULT NULL,
  `receipt_to_inspected_lag` int(11) DEFAULT NULL,
  `receipt_to_bin_placement_lag` int(11) DEFAULT NULL,
  `receipt_to_initial_shipment_lag` int(11) DEFAULT NULL,
  `initial_to_last_shipment_lag` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory_receipt_accumulating_fact`
--

INSERT INTO `inventory_receipt_accumulating_fact` (`product_lot_receipt_number`, `date_received_key`, `date_inspected_key`, `date_bin_placement_key`, `date_initial_shipment_key`, `date_last_shipment_key`, `product_key`, `warehouse_key`, `vendor_key`, `quantity_received`, `quantity_inspected`, `quantity_returned_to_vendor`, `quantity_placed_in_bin`, `quantity_shipped_to_customer`, `quantity_returned_by_customer`, `quantity_returned_to_inventory`, `quantity_damaged`, `receipt_to_inspected_lag`, `receipt_to_bin_placement_lag`, `receipt_to_initial_shipment_lag`, `initial_to_last_shipment_lag`) VALUES
(101, 20231121, 0, 0, 0, 0, '10354', 111, 101, 10, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL),
(102, 20231121, 0, 0, 0, 0, '10354', 112, 102, 10, 0, 0, 0, 0, 0, 0, 0, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `payment_method_dimension`
--

CREATE TABLE `payment_method_dimension` (
  `payment_method_key` varchar(5) NOT NULL,
  `payment_method_description` varchar(255) DEFAULT NULL,
  `payment_method_group` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment_method_dimension`
--

INSERT INTO `payment_method_dimension` (`payment_method_key`, `payment_method_description`, `payment_method_group`) VALUES
('19321', 'GoPay', 'Online'),
('24974', 'Kartu ', 'Debit'),
('29238', 'Cash', 'Cash'),
('78462', 'Kartu', 'Kredit');

-- --------------------------------------------------------

--
-- Table structure for table `product_dimension`
--

CREATE TABLE `product_dimension` (
  `product_key` varchar(5) NOT NULL,
  `SKU_number` varchar(8) DEFAULT NULL,
  `product_description` varchar(255) DEFAULT NULL,
  `brand_description` varchar(255) DEFAULT NULL,
  `category_description` varchar(255) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_dimension`
--

INSERT INTO `product_dimension` (`product_key`, `SKU_number`, `product_description`, `brand_description`, `category_description`, `price`, `cost`) VALUES
('10354', 'SKU-1035', 'Susu', 'Frisian Flag', 'Susu Anak', 21000, 16000),
('10796', 'SKU-1079', 'Minyak Goreng Bimoli', 'Bimoli', 'Minyak Goreng', 36500, 31500),
('11718', 'SKU-1171', 'Lifebuoy Lemon', 'Lifebuoy', 'Sabun Mandi', 25000, 20000),
('12341', 'SKU-1234', 'Indomie Mi Goreng', 'Indomie', 'Mi Instan', 3000, 2700),
('14205', 'SKU-1420', 'Rexona Women', 'Rexona', 'Deodorant', 17500, 12500);

-- --------------------------------------------------------

--
-- Table structure for table `promotion_dimension`
--

CREATE TABLE `promotion_dimension` (
  `promotion_key` varchar(5) NOT NULL,
  `promotion_code` varchar(25) DEFAULT NULL,
  `promotion_name` varchar(25) DEFAULT NULL,
  `promotion_media_type` varchar(25) DEFAULT NULL,
  `promotion_begin_date` date DEFAULT NULL,
  `promotion_end_date` date DEFAULT NULL,
  `promotion_percentage` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `promotion_dimension`
--

INSERT INTO `promotion_dimension` (`promotion_key`, `promotion_code`, `promotion_name`, `promotion_media_type`, `promotion_begin_date`, `promotion_end_date`, `promotion_percentage`) VALUES
('12719', 'Pe66dc5c1-5ea2-4726-ad97-', 'Tahun Baru', 'Online', '2023-01-01', '2023-01-08', 10),
('12936', 'Pecd4973b-b72b-4cc4-966d-', 'Valentine', 'Online', '2023-02-13', '2023-02-14', 15),
('28971', 'P4edf06e5-1d6d-427b-b36a-', 'No Promotion', 'Offline', '2023-01-01', '2023-12-31', 0),
('33121', 'P9609c413-d9bd-4f93-b355-', 'Hari Kemerdekaan', 'Offline', '2023-08-14', '2023-08-20', 20),
('38737', 'P528f85f1-2940-4152-bba0-', 'Halloween', 'Online', '2023-10-24', '2023-10-31', 25),
('80140', 'Pf9b7633c-cf1a-4cdc-8313-', 'Hari Buruh', 'Offline', '2023-05-01', '2023-05-08', 18);

-- --------------------------------------------------------

--
-- Table structure for table `retail_inventory_snapshot_facts`
--

CREATE TABLE `retail_inventory_snapshot_facts` (
  `snapshot_key` int(10) NOT NULL,
  `date_key` int(11) NOT NULL,
  `product_key` varchar(5) NOT NULL,
  `store_key` varchar(5) DEFAULT NULL,
  `quantity_on_hand` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `retail_sales_facts`
--

CREATE TABLE `retail_sales_facts` (
  `retail_id` int(11) NOT NULL,
  `date_key` int(11) DEFAULT NULL,
  `product_key` varchar(5) DEFAULT NULL,
  `store_key` varchar(5) DEFAULT NULL,
  `promotion_key` varchar(5) DEFAULT NULL,
  `cashier_key` varchar(10) DEFAULT NULL,
  `payment_method_key` varchar(50) DEFAULT NULL,
  `pos_transaction` varchar(255) DEFAULT NULL,
  `sales_quantity` int(11) DEFAULT NULL,
  `regular_unit_price` decimal(10,2) DEFAULT NULL,
  `discount_unit_price` decimal(10,2) DEFAULT NULL,
  `net_unit_price` decimal(10,2) DEFAULT NULL,
  `extended_discount_dollar_amount` decimal(10,2) DEFAULT NULL,
  `extended_sales_dollar_amount` decimal(10,2) DEFAULT NULL,
  `extended_cost_dollar_amount` decimal(10,2) DEFAULT NULL,
  `extended_gross_profit_dollar_amount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `retail_sales_facts`
--

INSERT INTO `retail_sales_facts` (`retail_id`, `date_key`, `product_key`, `store_key`, `promotion_key`, `cashier_key`, `payment_method_key`, `pos_transaction`, `sales_quantity`, `regular_unit_price`, `discount_unit_price`, `net_unit_price`, `extended_discount_dollar_amount`, `extended_sales_dollar_amount`, `extended_cost_dollar_amount`, `extended_gross_profit_dollar_amount`) VALUES
(142, 20230118, '12341', '2124', '28971', 'CASHIER317', '29238', 'offline', 1, 3000.00, 0.00, 3000.00, 0.00, 3000.00, 2700.00, 300.00),
(143, 20231008, '10354', '2123', '28971', 'CASHIER262', '19321', 'offline', 10, 21000.00, 0.00, 21000.00, 0.00, 210000.00, 160000.00, 50000.00),
(144, 20231206, '10796', '2123', '28971', 'CASHIER177', '19321', 'offline', 7, 36500.00, 0.00, 36500.00, 0.00, 255500.00, 220500.00, 35000.00),
(145, 20230217, '11718', '2124', '28971', 'CASHIER262', '19321', 'offline', 2, 25000.00, 0.00, 25000.00, 0.00, 50000.00, 40000.00, 10000.00),
(146, 20230615, '10354', '2123', '28971', 'CASHIER208', '29238', 'offline', 2, 21000.00, 0.00, 21000.00, 0.00, 42000.00, 32000.00, 10000.00),
(147, 20230603, '11718', '2125', '28971', 'CASHIER115', '29238', 'offline', 5, 25000.00, 0.00, 25000.00, 0.00, 125000.00, 100000.00, 25000.00),
(148, 20230503, '12341', '2127', '28971', 'CASHIER167', '78462', 'offline', 9, 3000.00, 0.00, 3000.00, 0.00, 27000.00, 24300.00, 2700.00),
(149, 20230921, '10796', '2126', '28971', 'CASHIER115', '29238', 'offline', 7, 36500.00, 0.00, 36500.00, 0.00, 255500.00, 220500.00, 35000.00),
(150, 20230320, '11718', '2127', '28971', 'CASHIER262', '78462', 'offline', 2, 25000.00, 0.00, 25000.00, 0.00, 50000.00, 40000.00, 10000.00),
(151, 20231024, '10354', '2124', '28971', 'CASHIER167', '29238', 'offline', 6, 21000.00, 0.00, 21000.00, 0.00, 126000.00, 96000.00, 30000.00),
(152, 20231010, '10354', '2124', '28971', 'CASHIER167', '19321', 'offline', 2, 21000.00, 0.00, 21000.00, 0.00, 42000.00, 32000.00, 10000.00),
(153, 20230201, '10354', '2127', '28971', 'CASHIER115', '24974', 'offline', 10, 21000.00, 0.00, 21000.00, 0.00, 210000.00, 160000.00, 50000.00),
(154, 20230529, '10354', '2123', '28971', 'CASHIER262', '78462', 'offline', 3, 21000.00, 0.00, 21000.00, 0.00, 63000.00, 48000.00, 15000.00),
(155, 20230511, '10354', '2124', '28971', 'CASHIER167', '24974', 'offline', 1, 21000.00, 0.00, 21000.00, 0.00, 21000.00, 16000.00, 5000.00),
(156, 20230322, '10354', '2124', '28971', 'CASHIER208', '29238', 'offline', 6, 21000.00, 0.00, 21000.00, 0.00, 126000.00, 96000.00, 30000.00),
(157, 20230722, '12341', '2127', '28971', 'CASHIER167', '78462', 'offline', 4, 3000.00, 0.00, 3000.00, 0.00, 12000.00, 10800.00, 1200.00),
(158, 20230720, '14205', '2124', '28971', 'CASHIER115', '29238', 'offline', 2, 17500.00, 0.00, 17500.00, 0.00, 35000.00, 25000.00, 10000.00),
(159, 20230727, '11718', '2126', '28971', 'CASHIER115', '78462', 'offline', 7, 25000.00, 0.00, 25000.00, 0.00, 175000.00, 140000.00, 35000.00),
(160, 20230908, '12341', '2124', '28971', 'CASHIER115', '29238', 'offline', 8, 3000.00, 0.00, 3000.00, 0.00, 24000.00, 21600.00, 2400.00),
(161, 20230629, '14205', '2124', '28971', 'CASHIER317', '29238', 'offline', 3, 17500.00, 0.00, 17500.00, 0.00, 52500.00, 37500.00, 15000.00),
(162, 20230601, '12341', '2124', '28971', 'CASHIER115', '24974', 'offline', 6, 3000.00, 0.00, 3000.00, 0.00, 18000.00, 16200.00, 1800.00),
(163, 20230627, '14205', '2126', '28971', 'CASHIER103', '29238', 'offline', 6, 17500.00, 0.00, 17500.00, 0.00, 105000.00, 75000.00, 30000.00),
(164, 20230527, '11718', '2125', '28971', 'CASHIER103', '78462', 'offline', 9, 25000.00, 0.00, 25000.00, 0.00, 225000.00, 180000.00, 45000.00),
(165, 20230406, '14205', '2125', '28971', 'CASHIER208', '78462', 'offline', 5, 17500.00, 0.00, 17500.00, 0.00, 87500.00, 62500.00, 25000.00),
(166, 20230911, '10796', '2125', '28971', 'CASHIER208', '24974', 'offline', 6, 36500.00, 0.00, 36500.00, 0.00, 219000.00, 189000.00, 30000.00),
(167, 20230518, '10354', '2125', '28971', 'CASHIER167', '78462', 'offline', 2, 21000.00, 0.00, 21000.00, 0.00, 42000.00, 32000.00, 10000.00),
(168, 20230526, '12341', '2123', '28971', 'CASHIER262', '29238', 'offline', 7, 3000.00, 0.00, 3000.00, 0.00, 21000.00, 18900.00, 2100.00),
(169, 20231224, '14205', '2126', '28971', 'CASHIER103', '78462', 'offline', 2, 17500.00, 0.00, 17500.00, 0.00, 35000.00, 25000.00, 10000.00),
(170, 20231107, '14205', '2123', '28971', 'CASHIER222', '19321', 'offline', 9, 17500.00, 0.00, 17500.00, 0.00, 157500.00, 112500.00, 45000.00),
(171, 20230409, '11718', '2126', '28971', 'CASHIER115', '24974', 'offline', 3, 25000.00, 0.00, 25000.00, 0.00, 75000.00, 60000.00, 15000.00),
(172, 20230210, '10354', '2125', '28971', 'CASHIER115', '24974', 'offline', 7, 21000.00, 0.00, 21000.00, 0.00, 147000.00, 112000.00, 35000.00),
(173, 20230518, '14205', '2125', '28971', 'CASHIER262', '78462', 'offline', 7, 17500.00, 0.00, 17500.00, 0.00, 122500.00, 87500.00, 35000.00),
(174, 20231128, '10796', '2125', '28971', 'CASHIER103', '29238', 'offline', 3, 36500.00, 0.00, 36500.00, 0.00, 109500.00, 94500.00, 15000.00),
(175, 20230806, '14205', '2126', '28971', 'CASHIER115', '29238', 'offline', 1, 17500.00, 0.00, 17500.00, 0.00, 17500.00, 12500.00, 5000.00),
(176, 20230113, '10354', '2123', '28971', 'CASHIER167', '19321', 'offline', 6, 21000.00, 0.00, 21000.00, 0.00, 126000.00, 96000.00, 30000.00),
(177, 20230323, '14205', '2125', '28971', 'CASHIER115', '19321', 'offline', 9, 17500.00, 0.00, 17500.00, 0.00, 157500.00, 112500.00, 45000.00),
(178, 20230519, '10354', '2126', '28971', 'CASHIER262', '29238', 'offline', 5, 21000.00, 0.00, 21000.00, 0.00, 105000.00, 80000.00, 25000.00),
(179, 20230121, '11718', '2126', '28971', 'CASHIER222', '19321', 'offline', 3, 25000.00, 0.00, 25000.00, 0.00, 75000.00, 60000.00, 15000.00),
(180, 20230214, '12341', '2125', '12936', 'CASHIER115', '78462', 'offline', 6, 3000.00, 450.00, 2550.00, 2700.00, 15300.00, 16200.00, -900.00),
(181, 20230101, '11718', '2124', '12719', 'CASHIER222', '19321', 'offline', 5, 25000.00, 2500.00, 22500.00, 12500.00, 112500.00, 100000.00, 12500.00),
(182, 20230214, '10796', '2126', '12936', 'CASHIER317', '19321', 'offline', 8, 36500.00, 5475.00, 31025.00, 43800.00, 248200.00, 252000.00, -3800.00),
(183, 20230101, '10354', '2126', '12719', 'CASHIER167', '78462', 'offline', 5, 21000.00, 2100.00, 18900.00, 10500.00, 94500.00, 80000.00, 14500.00),
(184, 20230214, '11718', '2125', '12936', 'CASHIER177', '19321', 'offline', 2, 25000.00, 3750.00, 21250.00, 7500.00, 42500.00, 40000.00, 2500.00),
(185, 20230214, '14205', '2126', '12936', 'CASHIER103', '78462', 'offline', 4, 17500.00, 2625.00, 14875.00, 10500.00, 59500.00, 50000.00, 9500.00),
(186, 20230214, '10354', '2127', '12936', 'CASHIER177', '78462', 'offline', 10, 21000.00, 3150.00, 17850.00, 31500.00, 178500.00, 160000.00, 18500.00),
(187, 20230214, '14205', '2124', '12936', 'CASHIER317', '78462', 'offline', 8, 17500.00, 2625.00, 14875.00, 21000.00, 119000.00, 100000.00, 19000.00),
(188, 20230214, '10796', '2123', '12936', 'CASHIER167', '29238', 'offline', 8, 36500.00, 5475.00, 31025.00, 43800.00, 248200.00, 252000.00, -3800.00);

-- --------------------------------------------------------

--
-- Table structure for table `store_dimension`
--

CREATE TABLE `store_dimension` (
  `store_key` varchar(5) NOT NULL,
  `store_number` varchar(3) DEFAULT NULL,
  `store_name` varchar(255) DEFAULT NULL,
  `store_district` varchar(255) DEFAULT NULL,
  `store_region` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_dimension`
--

INSERT INTO `store_dimension` (`store_key`, `store_number`, `store_name`, `store_district`, `store_region`) VALUES
('2123', '123', 'Toko A', 'Jakarta Pusat', 'Jakarta'),
('2124', '123', 'Toko B', 'Pontianak ', 'Kalimantan'),
('2125', '124', 'Toko C', 'Jakarta Barat', 'Jakarta'),
('2126', '125', 'Toko D', 'Jakarta Timur', 'Jakarta'),
('2127', '126', 'Toko E', 'Jakarta Pusat', 'Jakarta');

-- --------------------------------------------------------

--
-- Table structure for table `traveller_shopper_dimension`
--

CREATE TABLE `traveller_shopper_dimension` (
  `traveller_id` varchar(10) NOT NULL,
  `traveller_type` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `traveller_shopper_dimension`
--

INSERT INTO `traveller_shopper_dimension` (`traveller_id`, `traveller_type`) VALUES
('Buyer_000', 'Unidentified'),
('Buyer_001', 'Daily_Buyer'),
('Buyer_002', 'Weekly_Buyer'),
('Buyer_003', 'Monthly_Buyer'),
('Buyer_004', 'Annual_Buyer');

-- --------------------------------------------------------

--
-- Table structure for table `vendor_dimension`
--

CREATE TABLE `vendor_dimension` (
  `vendor_key` int(11) NOT NULL,
  `vendor_name` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `product_category` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vendor_dimension`
--

INSERT INTO `vendor_dimension` (`vendor_key`, `vendor_name`, `contact`, `product_category`, `address`) VALUES
(101, 'Vendor A', 'Contact A', 'Snacks', 'Address A'),
(102, 'Vendor B', 'Contact B', 'Deodorant', 'Address B'),
(103, 'Vendor C', 'Contact C', 'Susu Anak', 'Address C');

-- --------------------------------------------------------

--
-- Table structure for table `warehouse_dimension`
--

CREATE TABLE `warehouse_dimension` (
  `warehouse_key` int(11) NOT NULL,
  `warehouse_number` varchar(255) NOT NULL,
  `warehouse_name` varchar(255) NOT NULL,
  `warehouse_address` varchar(255) NOT NULL,
  `warehouse_city` varchar(255) NOT NULL,
  `warehouse_city_state` varchar(255) NOT NULL,
  `warehouse_state` varchar(255) NOT NULL,
  `warehouse_zip` varchar(255) NOT NULL,
  `warehouse_zone` varchar(255) NOT NULL,
  `warehouse_total_square_footage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `warehouse_dimension`
--

INSERT INTO `warehouse_dimension` (`warehouse_key`, `warehouse_number`, `warehouse_name`, `warehouse_address`, `warehouse_city`, `warehouse_city_state`, `warehouse_state`, `warehouse_zip`, `warehouse_zone`, `warehouse_total_square_footage`) VALUES
(111, '123', 'Warehouse A', 'Address A', 'City A', 'City State A', 'State A', 'Zip A', 'Zone A', 500),
(112, '124', 'Warehouse B', 'Address B', 'City B', 'City State B', 'State B', 'Zip B', 'Zone B', 500),
(113, '125', 'Warehouse C', 'Address C', 'City C', 'City State C', 'State C', 'Zip C', 'Zone C', 500);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cashier_dimension`
--
ALTER TABLE `cashier_dimension`
  ADD PRIMARY KEY (`cashier_key`);

--
-- Indexes for table `date_dimension`
--
ALTER TABLE `date_dimension`
  ADD PRIMARY KEY (`date_key`);

--
-- Indexes for table `historic_retail_inventory_snapshot_fact`
--
ALTER TABLE `historic_retail_inventory_snapshot_fact`
  ADD PRIMARY KEY (`snapshot_key`),
  ADD KEY `date_key` (`date_key`),
  ADD KEY `product_key` (`product_key`),
  ADD KEY `store_key` (`store_key`);

--
-- Indexes for table `inventory_receipt_accumulating_fact`
--
ALTER TABLE `inventory_receipt_accumulating_fact`
  ADD PRIMARY KEY (`product_lot_receipt_number`),
  ADD KEY `date_received_key` (`date_received_key`),
  ADD KEY `date_inspected_key` (`date_inspected_key`),
  ADD KEY `date_bin_placement_key` (`date_bin_placement_key`),
  ADD KEY `date_initial_shipment_key` (`date_initial_shipment_key`),
  ADD KEY `date_last_shipment_key` (`date_last_shipment_key`),
  ADD KEY `product_key` (`product_key`),
  ADD KEY `warehouse_key` (`warehouse_key`),
  ADD KEY `vendor_key` (`vendor_key`);

--
-- Indexes for table `payment_method_dimension`
--
ALTER TABLE `payment_method_dimension`
  ADD PRIMARY KEY (`payment_method_key`);

--
-- Indexes for table `product_dimension`
--
ALTER TABLE `product_dimension`
  ADD PRIMARY KEY (`product_key`),
  ADD UNIQUE KEY `product_key` (`product_key`);

--
-- Indexes for table `promotion_dimension`
--
ALTER TABLE `promotion_dimension`
  ADD PRIMARY KEY (`promotion_key`);

--
-- Indexes for table `retail_inventory_snapshot_facts`
--
ALTER TABLE `retail_inventory_snapshot_facts`
  ADD PRIMARY KEY (`snapshot_key`),
  ADD KEY `date_key` (`date_key`),
  ADD KEY `product_key` (`product_key`),
  ADD KEY `store_key` (`store_key`);

--
-- Indexes for table `retail_sales_facts`
--
ALTER TABLE `retail_sales_facts`
  ADD PRIMARY KEY (`retail_id`),
  ADD KEY `date_key` (`date_key`),
  ADD KEY `product_key` (`product_key`),
  ADD KEY `store_key` (`store_key`),
  ADD KEY `promotion_key` (`promotion_key`),
  ADD KEY `cashier_key` (`cashier_key`),
  ADD KEY `payment_method_key` (`payment_method_key`);

--
-- Indexes for table `store_dimension`
--
ALTER TABLE `store_dimension`
  ADD PRIMARY KEY (`store_key`);

--
-- Indexes for table `traveller_shopper_dimension`
--
ALTER TABLE `traveller_shopper_dimension`
  ADD PRIMARY KEY (`traveller_id`);

--
-- Indexes for table `vendor_dimension`
--
ALTER TABLE `vendor_dimension`
  ADD PRIMARY KEY (`vendor_key`);

--
-- Indexes for table `warehouse_dimension`
--
ALTER TABLE `warehouse_dimension`
  ADD PRIMARY KEY (`warehouse_key`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `historic_retail_inventory_snapshot_fact`
--
ALTER TABLE `historic_retail_inventory_snapshot_fact`
  MODIFY `snapshot_key` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=126;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `historic_retail_inventory_snapshot_fact`
--
ALTER TABLE `historic_retail_inventory_snapshot_fact`
  ADD CONSTRAINT `historic_retail_inventory_snapshot_fact_ibfk_1` FOREIGN KEY (`date_key`) REFERENCES `date_dimension` (`date_key`),
  ADD CONSTRAINT `historic_retail_inventory_snapshot_fact_ibfk_2` FOREIGN KEY (`product_key`) REFERENCES `product_dimension` (`product_key`),
  ADD CONSTRAINT `historic_retail_inventory_snapshot_fact_ibfk_3` FOREIGN KEY (`store_key`) REFERENCES `store_dimension` (`store_key`);

--
-- Constraints for table `inventory_receipt_accumulating_fact`
--
ALTER TABLE `inventory_receipt_accumulating_fact`
  ADD CONSTRAINT `inventory_receipt_accumulating_fact_ibfk_6` FOREIGN KEY (`product_key`) REFERENCES `product_dimension` (`product_key`),
  ADD CONSTRAINT `inventory_receipt_accumulating_fact_ibfk_7` FOREIGN KEY (`warehouse_key`) REFERENCES `warehouse_dimension` (`warehouse_key`),
  ADD CONSTRAINT `inventory_receipt_accumulating_fact_ibfk_8` FOREIGN KEY (`vendor_key`) REFERENCES `vendor_dimension` (`vendor_key`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
