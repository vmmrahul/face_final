-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 23, 2021 at 06:49 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `username`, `password`, `mobile`, `Name`, `type`) VALUES
('admin@gmail.com', 'admins', '1234', '6280995201', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `Attendance`
--

CREATE TABLE `Attendance` (
  `id` int(11) NOT NULL,
  `employ` int(11) NOT NULL,
  `dateOfAttendace` date NOT NULL,
  `timeOfRigister` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Attendance`
--

INSERT INTO `Attendance` (`id`, `employ`, `dateOfAttendace`, `timeOfRigister`) VALUES
(42, 2, '2021-05-17', '08:16:46'),
(43, 3, '2021-05-01', '09:22:07'),
(44, 2, '2021-05-17', '11:22:44');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `salary` float NOT NULL,
  `number_of_leave_allowed` int(11) NOT NULL,
  `deduction_leave` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`name`, `description`, `salary`, `number_of_leave_allowed`, `deduction_leave`) VALUES
('java', 'java developer', 7000, 18, 500);

-- --------------------------------------------------------

--
-- Table structure for table `dutyRoaster`
--

CREATE TABLE `dutyRoaster` (
  `id` int(11) NOT NULL,
  `dutyDate` date NOT NULL,
  `startTime` time NOT NULL,
  `EndTime` time NOT NULL,
  `employID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dutyRoaster`
--

INSERT INTO `dutyRoaster` (`id`, `dutyDate`, `startTime`, `EndTime`, `employID`) VALUES
(3, '2021-05-02', '09:00:00', '16:00:00', 2),
(4, '2021-05-03', '09:00:00', '16:00:00', 2),
(5, '2021-05-04', '09:00:00', '16:00:00', 2),
(6, '2021-05-05', '09:00:00', '16:00:00', 2),
(7, '2021-05-06', '09:00:00', '16:00:00', 2),
(8, '2021-05-07', '09:00:00', '16:00:00', 2),
(9, '2021-05-08', '09:00:00', '16:00:00', 2),
(10, '2021-05-09', '09:00:00', '16:00:00', 2),
(11, '2021-05-10', '09:00:00', '16:00:00', 2),
(12, '2021-05-11', '09:00:00', '16:00:00', 2),
(13, '2021-05-12', '09:00:00', '16:00:00', 2),
(14, '2021-05-13', '09:00:00', '16:00:00', 2),
(15, '2021-05-14', '09:00:00', '16:00:00', 2),
(16, '2021-05-15', '09:00:00', '16:00:00', 2),
(17, '2021-05-16', '09:00:00', '16:00:00', 2),
(18, '2021-05-17', '09:00:00', '16:00:00', 2),
(19, '2021-05-18', '09:00:00', '16:00:00', 2),
(20, '2021-05-19', '09:00:00', '16:00:00', 2),
(21, '2021-05-20', '09:00:00', '16:00:00', 2),
(22, '2021-05-21', '09:00:00', '16:00:00', 2),
(23, '2021-05-22', '09:00:00', '16:00:00', 2),
(24, '2021-05-23', '09:00:00', '16:00:00', 2),
(25, '2021-05-24', '09:00:00', '16:00:00', 2),
(26, '2021-05-25', '09:00:00', '16:00:00', 2),
(27, '2021-05-26', '09:00:00', '16:00:00', 2),
(28, '2021-05-27', '09:00:00', '16:00:00', 2),
(29, '2021-05-28', '09:00:00', '16:00:00', 2),
(30, '2021-05-29', '09:00:00', '16:00:00', 2),
(31, '2021-05-30', '09:00:00', '16:00:00', 2),
(32, '2021-05-31', '09:00:00', '16:00:00', 2),
(33, '2021-06-01', '09:00:00', '16:00:00', 2),
(34, '2021-06-02', '09:00:00', '16:00:00', 2),
(35, '2021-06-03', '09:00:00', '16:00:00', 2),
(36, '2021-06-04', '09:00:00', '16:00:00', 2),
(37, '2021-06-05', '09:00:00', '16:00:00', 2),
(38, '2021-06-06', '09:00:00', '16:00:00', 2),
(39, '2021-06-07', '09:00:00', '16:00:00', 2),
(40, '2021-06-08', '09:00:00', '16:00:00', 2),
(41, '2021-06-09', '09:00:00', '16:00:00', 2),
(42, '2021-06-10', '09:00:00', '16:00:00', 2),
(43, '2021-06-11', '09:00:00', '16:00:00', 2),
(44, '2021-06-12', '09:00:00', '16:00:00', 2),
(45, '2021-06-13', '09:00:00', '16:00:00', 2),
(46, '2021-06-14', '09:00:00', '16:00:00', 2),
(47, '2021-06-15', '09:00:00', '16:00:00', 2),
(48, '2021-06-16', '09:00:00', '16:00:00', 2),
(49, '2021-06-17', '09:00:00', '16:00:00', 2),
(50, '2021-06-18', '09:00:00', '16:00:00', 2),
(51, '2021-06-19', '09:00:00', '16:00:00', 2),
(52, '2021-06-20', '09:00:00', '16:00:00', 2),
(53, '2021-06-21', '09:00:00', '16:00:00', 2),
(54, '2021-06-22', '09:00:00', '16:00:00', 2),
(55, '2021-06-23', '09:00:00', '16:00:00', 2),
(56, '2021-06-24', '09:00:00', '16:00:00', 2),
(57, '2021-06-25', '09:00:00', '16:00:00', 2),
(58, '2021-06-26', '09:00:00', '16:00:00', 2),
(59, '2021-06-27', '09:00:00', '16:00:00', 2),
(60, '2021-06-28', '09:00:00', '16:00:00', 2),
(61, '2021-06-29', '09:00:00', '16:00:00', 2),
(62, '2021-06-30', '09:00:00', '16:00:00', 2),
(63, '2021-07-01', '09:00:00', '16:00:00', 2),
(64, '2021-07-02', '09:00:00', '16:00:00', 2),
(65, '2021-07-03', '09:00:00', '16:00:00', 2),
(66, '2021-07-04', '09:00:00', '16:00:00', 2),
(67, '2021-07-05', '09:00:00', '16:00:00', 2),
(68, '2021-07-06', '09:00:00', '16:00:00', 2),
(69, '2021-07-07', '09:00:00', '16:00:00', 2),
(70, '2021-07-08', '09:00:00', '16:00:00', 2),
(71, '2021-07-09', '09:00:00', '16:00:00', 2),
(72, '2021-07-10', '09:00:00', '16:00:00', 2),
(73, '2021-07-11', '09:00:00', '16:00:00', 2),
(74, '2021-07-12', '09:00:00', '16:00:00', 2),
(75, '2021-07-13', '09:00:00', '16:00:00', 2),
(76, '2021-07-14', '09:00:00', '16:00:00', 2),
(77, '2021-07-15', '09:00:00', '16:00:00', 2),
(78, '2021-07-16', '09:00:00', '16:00:00', 2),
(79, '2021-07-17', '09:00:00', '16:00:00', 2),
(80, '2021-07-18', '09:00:00', '16:00:00', 2),
(81, '2021-07-19', '09:00:00', '16:00:00', 2),
(82, '2021-07-20', '09:00:00', '16:00:00', 2),
(83, '2021-07-21', '09:00:00', '16:00:00', 2),
(84, '2021-07-22', '09:00:00', '16:00:00', 2),
(85, '2021-07-23', '09:00:00', '16:00:00', 2),
(86, '2021-07-24', '09:00:00', '16:00:00', 2),
(87, '2021-07-25', '09:00:00', '16:00:00', 2),
(88, '2021-07-26', '09:00:00', '16:00:00', 2),
(89, '2021-07-27', '09:00:00', '16:00:00', 2),
(90, '2021-07-28', '09:00:00', '16:00:00', 2),
(91, '2021-07-29', '09:00:00', '16:00:00', 2),
(92, '2021-07-30', '09:00:00', '16:00:00', 2),
(93, '2021-07-31', '09:00:00', '16:00:00', 2),
(94, '2021-08-01', '09:00:00', '16:00:00', 2),
(95, '2021-08-02', '09:00:00', '16:00:00', 2),
(96, '2021-08-03', '09:00:00', '16:00:00', 2),
(97, '2021-08-04', '09:00:00', '16:00:00', 2),
(98, '2021-08-05', '09:00:00', '16:00:00', 2),
(99, '2021-08-06', '09:00:00', '16:00:00', 2),
(100, '2021-08-07', '09:00:00', '16:00:00', 2),
(101, '2021-08-08', '09:00:00', '16:00:00', 2),
(102, '2021-08-09', '09:00:00', '16:00:00', 2),
(103, '2021-08-10', '09:00:00', '16:00:00', 2),
(104, '2021-08-11', '09:00:00', '16:00:00', 2),
(105, '2021-08-12', '09:00:00', '16:00:00', 2),
(106, '2021-08-13', '09:00:00', '16:00:00', 2),
(107, '2021-08-14', '09:00:00', '16:00:00', 2),
(108, '2021-08-15', '09:00:00', '16:00:00', 2),
(109, '2021-08-16', '09:00:00', '16:00:00', 2),
(110, '2021-08-17', '09:00:00', '16:00:00', 2),
(111, '2021-08-18', '09:00:00', '16:00:00', 2),
(112, '2021-08-19', '09:00:00', '16:00:00', 2),
(113, '2021-08-20', '09:00:00', '16:00:00', 2),
(114, '2021-08-21', '09:00:00', '16:00:00', 2),
(115, '2021-08-22', '09:00:00', '16:00:00', 2),
(116, '2021-08-23', '09:00:00', '16:00:00', 2),
(117, '2021-08-24', '09:00:00', '16:00:00', 2),
(118, '2021-08-25', '09:00:00', '16:00:00', 2),
(119, '2021-08-26', '09:00:00', '16:00:00', 2),
(120, '2021-08-27', '09:00:00', '16:00:00', 2),
(121, '2021-08-28', '09:00:00', '16:00:00', 2),
(122, '2021-08-29', '09:00:00', '16:00:00', 2),
(123, '2021-08-30', '09:00:00', '16:00:00', 2),
(124, '2021-08-31', '09:00:00', '16:00:00', 2),
(125, '2021-09-01', '09:00:00', '16:00:00', 2),
(126, '2021-09-02', '09:00:00', '16:00:00', 2),
(127, '2021-09-03', '09:00:00', '16:00:00', 2),
(128, '2021-09-04', '09:00:00', '16:00:00', 2),
(129, '2021-09-05', '09:00:00', '16:00:00', 2),
(130, '2021-09-06', '09:00:00', '16:00:00', 2),
(131, '2021-09-07', '09:00:00', '16:00:00', 2),
(132, '2021-09-08', '09:00:00', '16:00:00', 2),
(133, '2021-09-09', '09:00:00', '16:00:00', 2),
(134, '2021-09-10', '09:00:00', '16:00:00', 2),
(135, '2021-09-11', '09:00:00', '16:00:00', 2),
(136, '2021-09-12', '09:00:00', '16:00:00', 2),
(137, '2021-09-13', '09:00:00', '16:00:00', 2),
(138, '2021-09-14', '09:00:00', '16:00:00', 2),
(139, '2021-09-15', '09:00:00', '16:00:00', 2),
(140, '2021-09-16', '09:00:00', '16:00:00', 2),
(141, '2021-09-17', '09:00:00', '16:00:00', 2),
(142, '2021-09-18', '09:00:00', '16:00:00', 2),
(143, '2021-09-19', '09:00:00', '16:00:00', 2),
(144, '2021-09-20', '09:00:00', '16:00:00', 2),
(145, '2021-09-21', '09:00:00', '16:00:00', 2),
(146, '2021-09-22', '09:00:00', '16:00:00', 2),
(147, '2021-09-23', '09:00:00', '16:00:00', 2),
(148, '2021-09-24', '09:00:00', '16:00:00', 2),
(149, '2021-09-25', '09:00:00', '16:00:00', 2),
(150, '2021-09-26', '09:00:00', '16:00:00', 2),
(151, '2021-09-27', '09:00:00', '16:00:00', 2),
(152, '2021-09-28', '09:00:00', '16:00:00', 2),
(153, '2021-09-29', '09:00:00', '16:00:00', 2),
(154, '2021-09-30', '09:00:00', '16:00:00', 2),
(155, '2021-10-01', '09:00:00', '16:00:00', 2),
(157, '2021-05-02', '10:00:00', '17:00:00', 3),
(158, '2021-05-03', '10:00:00', '17:00:00', 3),
(159, '2021-05-04', '10:00:00', '17:00:00', 3),
(160, '2021-05-05', '10:00:00', '17:00:00', 3),
(161, '2021-05-06', '10:00:00', '17:00:00', 3),
(162, '2021-05-07', '10:00:00', '17:00:00', 3),
(163, '2021-05-08', '10:00:00', '17:00:00', 3),
(164, '2021-05-09', '10:00:00', '17:00:00', 3),
(165, '2021-05-10', '10:00:00', '17:00:00', 3),
(166, '2021-05-11', '10:00:00', '17:00:00', 3),
(167, '2021-05-12', '10:00:00', '17:00:00', 3),
(168, '2021-05-13', '10:00:00', '17:00:00', 3),
(169, '2021-05-14', '10:00:00', '17:00:00', 3),
(170, '2021-05-15', '10:00:00', '17:00:00', 3),
(171, '2021-05-16', '10:00:00', '17:00:00', 3),
(172, '2021-05-17', '10:00:00', '17:00:00', 3),
(173, '2021-05-18', '10:00:00', '17:00:00', 3),
(174, '2021-05-19', '10:00:00', '17:00:00', 3),
(175, '2021-05-20', '10:00:00', '17:00:00', 3),
(176, '2021-05-21', '10:00:00', '17:00:00', 3),
(177, '2021-05-22', '10:00:00', '17:00:00', 3),
(178, '2021-05-23', '10:00:00', '17:00:00', 3),
(179, '2021-05-24', '10:00:00', '17:00:00', 3),
(180, '2021-05-25', '10:00:00', '17:00:00', 3),
(181, '2021-05-26', '10:00:00', '17:00:00', 3),
(182, '2021-05-27', '10:00:00', '17:00:00', 3),
(183, '2021-05-28', '10:00:00', '17:00:00', 3),
(184, '2021-05-29', '10:00:00', '17:00:00', 3),
(185, '2021-05-30', '10:00:00', '17:00:00', 3),
(186, '2021-05-31', '10:00:00', '17:00:00', 3),
(187, '2021-06-01', '10:00:00', '17:00:00', 3),
(188, '2021-06-02', '10:00:00', '17:00:00', 3),
(189, '2021-06-03', '10:00:00', '17:00:00', 3),
(190, '2021-06-04', '10:00:00', '17:00:00', 3),
(191, '2021-06-05', '10:00:00', '17:00:00', 3),
(192, '2021-06-06', '10:00:00', '17:00:00', 3),
(193, '2021-06-07', '10:00:00', '17:00:00', 3),
(194, '2021-06-08', '10:00:00', '17:00:00', 3),
(195, '2021-06-09', '10:00:00', '17:00:00', 3),
(196, '2021-06-10', '10:00:00', '17:00:00', 3),
(197, '2021-06-11', '10:00:00', '17:00:00', 3),
(198, '2021-06-12', '10:00:00', '17:00:00', 3),
(199, '2021-06-13', '10:00:00', '17:00:00', 3),
(200, '2021-06-14', '10:00:00', '17:00:00', 3),
(201, '2021-06-15', '10:00:00', '17:00:00', 3),
(202, '2021-06-16', '10:00:00', '17:00:00', 3),
(203, '2021-06-17', '10:00:00', '17:00:00', 3),
(204, '2021-06-18', '10:00:00', '17:00:00', 3),
(205, '2021-06-19', '10:00:00', '17:00:00', 3),
(206, '2021-06-20', '10:00:00', '17:00:00', 3),
(207, '2021-06-21', '10:00:00', '17:00:00', 3),
(208, '2021-06-22', '10:00:00', '17:00:00', 3),
(209, '2021-06-23', '10:00:00', '17:00:00', 3),
(210, '2021-06-24', '10:00:00', '17:00:00', 3),
(211, '2021-06-25', '10:00:00', '17:00:00', 3),
(212, '2021-06-26', '10:00:00', '17:00:00', 3),
(213, '2021-06-27', '10:00:00', '17:00:00', 3),
(214, '2021-06-28', '10:00:00', '17:00:00', 3),
(215, '2021-06-29', '10:00:00', '17:00:00', 3),
(216, '2021-06-30', '10:00:00', '17:00:00', 3),
(217, '2021-07-01', '10:00:00', '17:00:00', 3),
(218, '2021-07-02', '10:00:00', '17:00:00', 3),
(219, '2021-07-03', '10:00:00', '17:00:00', 3),
(220, '2021-07-04', '10:00:00', '17:00:00', 3),
(221, '2021-07-05', '10:00:00', '17:00:00', 3),
(222, '2021-07-06', '10:00:00', '17:00:00', 3),
(223, '2021-07-07', '10:00:00', '17:00:00', 3),
(224, '2021-07-08', '10:00:00', '17:00:00', 3),
(225, '2021-07-09', '10:00:00', '17:00:00', 3),
(226, '2021-07-10', '10:00:00', '17:00:00', 3),
(227, '2021-07-11', '10:00:00', '17:00:00', 3),
(228, '2021-07-12', '10:00:00', '17:00:00', 3),
(229, '2021-07-13', '10:00:00', '17:00:00', 3),
(230, '2021-07-14', '10:00:00', '17:00:00', 3),
(231, '2021-07-15', '10:00:00', '17:00:00', 3),
(232, '2021-07-16', '10:00:00', '17:00:00', 3),
(233, '2021-07-17', '10:00:00', '17:00:00', 3),
(234, '2021-07-18', '10:00:00', '17:00:00', 3),
(235, '2021-07-19', '10:00:00', '17:00:00', 3),
(236, '2021-07-20', '10:00:00', '17:00:00', 3),
(237, '2021-07-21', '10:00:00', '17:00:00', 3),
(238, '2021-07-22', '10:00:00', '17:00:00', 3),
(239, '2021-07-23', '10:00:00', '17:00:00', 3),
(240, '2021-07-24', '10:00:00', '17:00:00', 3),
(241, '2021-07-25', '10:00:00', '17:00:00', 3),
(242, '2021-07-26', '10:00:00', '17:00:00', 3),
(243, '2021-07-27', '10:00:00', '17:00:00', 3),
(244, '2021-07-28', '10:00:00', '17:00:00', 3),
(245, '2021-07-29', '10:00:00', '17:00:00', 3),
(246, '2021-07-30', '10:00:00', '17:00:00', 3),
(247, '2021-07-31', '10:00:00', '17:00:00', 3),
(248, '2021-08-01', '10:00:00', '17:00:00', 3),
(249, '2021-08-02', '10:00:00', '17:00:00', 3),
(250, '2021-08-03', '10:00:00', '17:00:00', 3),
(251, '2021-08-04', '10:00:00', '17:00:00', 3),
(252, '2021-08-05', '10:00:00', '17:00:00', 3),
(253, '2021-08-06', '10:00:00', '17:00:00', 3),
(254, '2021-08-07', '10:00:00', '17:00:00', 3),
(255, '2021-08-08', '10:00:00', '17:00:00', 3),
(256, '2021-08-09', '10:00:00', '17:00:00', 3),
(257, '2021-08-10', '10:00:00', '17:00:00', 3),
(258, '2021-08-11', '10:00:00', '17:00:00', 3),
(259, '2021-08-12', '10:00:00', '17:00:00', 3),
(260, '2021-08-13', '10:00:00', '17:00:00', 3),
(261, '2021-08-14', '10:00:00', '17:00:00', 3),
(262, '2021-08-15', '10:00:00', '17:00:00', 3),
(263, '2021-08-16', '10:00:00', '17:00:00', 3),
(264, '2021-08-17', '10:00:00', '17:00:00', 3),
(265, '2021-08-18', '10:00:00', '17:00:00', 3),
(266, '2021-08-19', '10:00:00', '17:00:00', 3),
(267, '2021-08-20', '10:00:00', '17:00:00', 3),
(268, '2021-08-21', '10:00:00', '17:00:00', 3),
(269, '2021-08-22', '10:00:00', '17:00:00', 3),
(270, '2021-08-23', '10:00:00', '17:00:00', 3),
(271, '2021-08-24', '10:00:00', '17:00:00', 3),
(272, '2021-08-25', '10:00:00', '17:00:00', 3),
(273, '2021-08-26', '10:00:00', '17:00:00', 3),
(274, '2021-08-27', '10:00:00', '17:00:00', 3),
(275, '2021-08-28', '10:00:00', '17:00:00', 3),
(276, '2021-08-29', '10:00:00', '17:00:00', 3),
(277, '2021-08-30', '10:00:00', '17:00:00', 3),
(278, '2021-08-31', '10:00:00', '17:00:00', 3),
(279, '2021-09-01', '10:00:00', '17:00:00', 3),
(280, '2021-09-02', '10:00:00', '17:00:00', 3),
(281, '2021-09-03', '10:00:00', '17:00:00', 3),
(282, '2021-09-04', '10:00:00', '17:00:00', 3),
(283, '2021-09-05', '10:00:00', '17:00:00', 3),
(284, '2021-09-06', '10:00:00', '17:00:00', 3),
(285, '2021-09-07', '10:00:00', '17:00:00', 3),
(286, '2021-09-08', '10:00:00', '17:00:00', 3),
(287, '2021-09-09', '10:00:00', '17:00:00', 3),
(288, '2021-09-10', '10:00:00', '17:00:00', 3),
(289, '2021-09-11', '10:00:00', '17:00:00', 3),
(290, '2021-09-12', '10:00:00', '17:00:00', 3),
(291, '2021-09-13', '10:00:00', '17:00:00', 3),
(292, '2021-09-14', '10:00:00', '17:00:00', 3),
(293, '2021-09-15', '10:00:00', '17:00:00', 3),
(294, '2021-09-16', '10:00:00', '17:00:00', 3),
(295, '2021-09-17', '10:00:00', '17:00:00', 3),
(296, '2021-09-18', '10:00:00', '17:00:00', 3),
(297, '2021-09-19', '10:00:00', '17:00:00', 3),
(298, '2021-09-20', '10:00:00', '17:00:00', 3),
(299, '2021-09-21', '10:00:00', '17:00:00', 3),
(300, '2021-09-22', '10:00:00', '17:00:00', 3),
(301, '2021-09-23', '10:00:00', '17:00:00', 3),
(302, '2021-09-24', '10:00:00', '17:00:00', 3),
(303, '2021-09-25', '10:00:00', '17:00:00', 3),
(304, '2021-09-26', '10:00:00', '17:00:00', 3),
(305, '2021-09-27', '10:00:00', '17:00:00', 3),
(306, '2021-09-28', '10:00:00', '17:00:00', 3),
(307, '2021-09-29', '10:00:00', '17:00:00', 3),
(308, '2021-09-30', '10:00:00', '17:00:00', 3),
(309, '2021-10-01', '10:00:00', '17:00:00', 3);

-- --------------------------------------------------------

--
-- Table structure for table `employ`
--

CREATE TABLE `employ` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `catName` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `remarks` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employ`
--

INSERT INTO `employ` (`id`, `name`, `dob`, `catName`, `photo`, `email`, `mobile`, `remarks`) VALUES
(2, 'ram', '1995-01-02', 'java', 'Images/2.png', 'ram@gmail.com', '6280995201', 'demo'),
(3, 'sham', '1993-01-01', 'java', 'Images/3.png', 'sham@gmail.com', '6280995201', 'demo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `Attendance`
--
ALTER TABLE `Attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employ` (`employ`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `dutyRoaster`
--
ALTER TABLE `dutyRoaster`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employID` (`employID`);

--
-- Indexes for table `employ`
--
ALTER TABLE `employ`
  ADD PRIMARY KEY (`id`),
  ADD KEY `catName` (`catName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Attendance`
--
ALTER TABLE `Attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `dutyRoaster`
--
ALTER TABLE `dutyRoaster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=310;

--
-- AUTO_INCREMENT for table `employ`
--
ALTER TABLE `employ`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Attendance`
--
ALTER TABLE `Attendance`
  ADD CONSTRAINT `Attendance_ibfk_1` FOREIGN KEY (`employ`) REFERENCES `employ` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
