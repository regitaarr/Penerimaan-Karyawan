-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2024 at 02:54 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `penerimaan_karyawan`
--

-- --------------------------------------------------------

--
-- Table structure for table `daftar_karyawan_baru`
--

CREATE TABLE `daftar_karyawan_baru` (
  `no_daftar` int(4) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `nik` varchar(20) DEFAULT NULL,
  `jenis_kelamin` char(1) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `agama` varchar(10) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_hp` int(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `lulusan` varchar(20) DEFAULT NULL,
  `keahlian` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `daftar_karyawan_baru`
--

INSERT INTO `daftar_karyawan_baru` (`no_daftar`, `nama`, `nik`, `jenis_kelamin`, `tanggal_lahir`, `agama`, `alamat`, `no_hp`, `email`, `lulusan`, `keahlian`) VALUES
(5, 'Hamada Asahi', '32075220411366', 'L', '2001-09-14', 'Shinto', 'Bandung, Jawa Barat', 2147483647, 'hikun@gmail.com', 'S1 Teknik Mesin', 'Merakit Mesin');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `email` varchar(20) NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`email`, `password`) VALUES
('hikun@gmail.com', 'sahikun');

-- --------------------------------------------------------

--
-- Table structure for table `skor_test`
--

CREATE TABLE `skor_test` (
  `no_daftar` int(11) NOT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `skor` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `skor_test`
--

INSERT INTO `skor_test` (`no_daftar`, `nama`, `email`, `skor`) VALUES
(5, 'Hamada Asahi', 'hikun@gmail.com', 90);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `daftar_karyawan_baru`
--
ALTER TABLE `daftar_karyawan_baru`
  ADD PRIMARY KEY (`no_daftar`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
