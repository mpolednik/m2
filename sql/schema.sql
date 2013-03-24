# ************************************************************
# Sequel Pro SQL dump
# Version 4004
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.5.29)
# Database: maturita
# Generation Time: 2013-03-24 16:48:14 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table category
# ------------------------------------------------------------

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL DEFAULT '',
  `text` text,
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table comment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_user` int(11) unsigned DEFAULT NULL,
  `id_father` int(11) unsigned DEFAULT NULL,
  `id_image` int(11) unsigned NOT NULL,
  `text` varchar(1000) NOT NULL DEFAULT '',
  `rating` int(11) NOT NULL DEFAULT '0',
  `state` int(11) NOT NULL DEFAULT '1',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_image` (`id_image`),
  KEY `id_father` (`id_father`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`id_image`) REFERENCES `image` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_3` FOREIGN KEY (`id_father`) REFERENCES `comment` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_4` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table comment_rating
# ------------------------------------------------------------

DROP TABLE IF EXISTS `comment_rating`;

CREATE TABLE `comment_rating` (
  `id_user` int(11) unsigned NOT NULL,
  `id_target` int(11) unsigned NOT NULL,
  `value` int(11) NOT NULL,
  UNIQUE KEY `id_user` (`id_user`,`id_target`),
  KEY `id_target` (`id_target`),
  CONSTRAINT `comment_rating_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_rating_ibfk_2` FOREIGN KEY (`id_target`) REFERENCES `comment` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table exif
# ------------------------------------------------------------

DROP TABLE IF EXISTS `exif`;

CREATE TABLE `exif` (
  `id_image` int(11) unsigned NOT NULL,
  `key` varchar(40) NOT NULL DEFAULT '',
  `value` varchar(200) NOT NULL DEFAULT '',
  KEY `id_image` (`id_image`),
  CONSTRAINT `exif_ibfk_1` FOREIGN KEY (`id_image`) REFERENCES `image` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table image
# ------------------------------------------------------------

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_category` int(11) unsigned DEFAULT NULL,
  `id_user` int(11) unsigned DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `text` varchar(1024) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `kind` varchar(4) DEFAULT NULL,
  `rating` int(11) NOT NULL DEFAULT '0',
  `score` float NOT NULL DEFAULT '0',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_category` (`id_category`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `image_ibfk_3` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`) ON DELETE SET NULL,
  CONSTRAINT `image_ibfk_4` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table image_rating
# ------------------------------------------------------------

DROP TABLE IF EXISTS `image_rating`;

CREATE TABLE `image_rating` (
  `id_user` int(11) unsigned NOT NULL,
  `id_target` int(11) unsigned NOT NULL,
  `value` int(11) NOT NULL,
  UNIQUE KEY `id_user` (`id_user`,`id_target`),
  KEY `id_target` (`id_target`),
  CONSTRAINT `image_rating_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `image_rating_ibfk_2` FOREIGN KEY (`id_target`) REFERENCES `image` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table moderator
# ------------------------------------------------------------

DROP TABLE IF EXISTS `moderator`;

CREATE TABLE `moderator` (
  `id_user` int(11) unsigned NOT NULL,
  `id_category` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_user`,`id_category`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `moderator_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `moderator_ibfk_2` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table request
# ------------------------------------------------------------

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `id_user` int(11) unsigned DEFAULT NULL,
  `id_category` int(11) unsigned DEFAULT NULL,
  `type` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `text` varchar(1024) DEFAULT '',
  `state` int(11) NOT NULL DEFAULT '0',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `request_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE SET NULL,
  CONSTRAINT `request_ibfk_2` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `session`;

CREATE TABLE `session` (
  `key` varchar(128) NOT NULL DEFAULT '0',
  `value` blob NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `mail` varchar(255) NOT NULL DEFAULT '',
  `password` char(128) NOT NULL DEFAULT '',
  `phone` varchar(16) DEFAULT NULL,
  `rating_image` int(11) NOT NULL DEFAULT '0',
  `rating_comment` int(11) NOT NULL DEFAULT '0',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `level` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `mail` (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
