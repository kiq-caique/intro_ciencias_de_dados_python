-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: mariadb-169650-db.mariadb-169650:10054
-- Generation Time: Apr 18, 2024 at 03:48 AM
-- Server version: 11.1.2-MariaDB-1:11.1.2+maria~ubu2004
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `viagens`
--

-- --------------------------------------------------------

--
-- Table structure for table `destinos`
--

CREATE TABLE `destinos` (
  `id` int(11) DEFAULT NULL,
  `nome` varchar(255) NOT NULL COMMENT 'Nome do destino',
  `descricao` varchar(255) NOT NULL COMMENT 'Descrição do destino'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reservas`
--

CREATE TABLE `reservas` (
  `id` int(11) DEFAULT NULL COMMENT 'identificador único da reserva',
  `id_usuario` int(11) DEFAULT NULL COMMENT 'Referência ao ID do usuário',
  `id_destino` int(11) DEFAULT NULL COMMENT 'Referência ao destino da reserva',
  `data` date DEFAULT NULL COMMENT 'Data da reserva',
  `status` varchar(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confimado, pendente, cancelada, etc...)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) DEFAULT NULL,
  `nome` varchar(255) NOT NULL COMMENT 'Nome do usuário',
  `email` varchar(100) NOT NULL COMMENT 'E-mail do usuário',
  `endereco` varchar(100) NOT NULL COMMENT 'Endereço do usuário',
  `data_nascimento` date NOT NULL COMMENT 'Data de nascimento do usuário'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destinos`
--
ALTER TABLE `destinos`
  ADD UNIQUE KEY `descricao` (`descricao`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD UNIQUE KEY `email` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
