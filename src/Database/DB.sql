-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para flask_mvc
CREATE DATABASE IF NOT EXISTS `flask_mvc` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `flask_mvc`;

-- Volcando estructura para tabla flask_mvc.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `precio_venta` mediumtext NOT NULL,
  `precio_compra` text NOT NULL,
  `estado` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla flask_mvc.productos: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `descripcion`, `precio_venta`, `precio_compra`, `estado`) VALUES
	(1, 'Gaseosa', 'bebida', '1000', '600', 'Activo'),
	(2, 'Galleta', 'golosina', '500', '300', 'Activo'),
	(3, 'Leche', 'bebida', '1000', '800', 'Inactivo'),
	(4, 'Limpido', 'aseo', '1000', '800', 'Activo'),
	(5, 'Pepsi', 'bebida', '1500', '1000', 'Activo'),
	(6, 'Coca Cola', 'bebida', '2000', '1200', 'Inactivo'),
	(7, 'Jabon', 'aseo', '1000', '600', 'Activo'),
	(8, 'Cuaderno', 'Papeleria', '2000', '1200', 'Activo'),
	(9, 'Menta', 'Dulce', '200', '100', 'Activo');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
