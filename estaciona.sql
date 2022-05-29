-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-05-2022 a las 05:33:55
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `estacionamiento`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estaciona`
--

CREATE TABLE `estaciona` (
  `ticket` int(10) NOT NULL,
  `patente` varchar(8) NOT NULL,
  `fechaEntrada` datetime NOT NULL,
  `fechaSalida` datetime DEFAULT NULL,
  `total` int(10) DEFAULT NULL,
  `cerrado` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estaciona`
--

INSERT INTO `estaciona` (`ticket`, `patente`, `fechaEntrada`, `fechaSalida`, `total`, `cerrado`) VALUES
(1, 'RV4441', '2022-05-28 22:45:02', '2022-05-28 23:33:11', 193, 1),
(2, 'TJ3717', '2022-05-28 22:45:48', '2022-05-28 23:33:14', 190, 1),
(3, 'RR3776', '2022-05-28 22:46:01', '2022-05-28 23:33:40', 191, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estaciona`
--
ALTER TABLE `estaciona`
  ADD PRIMARY KEY (`ticket`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
