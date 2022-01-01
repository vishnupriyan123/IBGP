/*
SQLyog Ultimate v12.4.1 (64 bit)
MySQL - 5.5.9 : Database - ibgp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ibgp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ibgp`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `acctype` varchar(30) DEFAULT NULL,
  `accno` varchar(30) DEFAULT NULL,
  `bank` varchar(30) DEFAULT NULL,
  `branch` varchar(30) DEFAULT NULL,
  `balance` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `account` */

insert  into `account`(`id`,`uid`,`username`,`acctype`,`accno`,`bank`,`branch`,`balance`) values 
(1,NULL,NULL,NULL,'123456',NULL,NULL,NULL),
(2,NULL,NULL,NULL,'435',NULL,NULL,NULL),
(3,NULL,'vishnupriyan','sabjfkw','2167461278','bsdhbd','231','21312421');

/*Table structure for table `corporation` */

DROP TABLE IF EXISTS `corporation`;

CREATE TABLE `corporation` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `pin` varchar(10) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `corporation` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(30) DEFAULT NULL,
  `feedback` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`date`,`feedback`) values 
(12,'2020-01-23','qwerty qwerty qwe'),
(13,'2020-01-23','feeeeed baaaack'),
(14,'23/3/2020','gg');

/*Table structure for table `fund` */

DROP TABLE IF EXISTS `fund`;

CREATE TABLE `fund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(20) DEFAULT NULL,
  `issueDate` varchar(20) DEFAULT NULL,
  `validity` varchar(30) DEFAULT NULL,
  `amt` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fund` */

insert  into `fund`(`id`,`category`,`issueDate`,`validity`,`amt`) values 
(1,NULL,NULL,'351','13513');

/*Table structure for table `fundtouser` */

DROP TABLE IF EXISTS `fundtouser`;

CREATE TABLE `fundtouser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `accno` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fundtouser` */

insert  into `fundtouser`(`id`,`uid`,`username`,`accno`) values 
(1,NULL,'gdf','15335'),
(2,NULL,'ggf','');

/*Table structure for table `info` */

DROP TABLE IF EXISTS `info`;

CREATE TABLE `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `info` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `info` */

insert  into `info`(`id`,`info`) values 
(1,'tdtgfdghdfsfrgsdz');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'sdgsg','sasgas','admin'),
(2,'user','user','user');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `pin` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`uid`,`address`,`name`,`phone`,`pin`,`email`) values 
(1,'fsfsd','dfbsdh','2141','2311','csa'),
(4,'dfgfh','anu','3456','56','anu');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tof` varchar(30) DEFAULT NULL,
  `rid` varchar(30) DEFAULT NULL,
  `ruser` varchar(30) DEFAULT NULL,
  `amt` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`tof`,`rid`,`ruser`,`amt`,`status`) values 
(1,'sdg','ff','fse','fsg',NULL);

/*Table structure for table `transfer` */

DROP TABLE IF EXISTS `transfer`;

CREATE TABLE `transfer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tof` varchar(30) DEFAULT NULL,
  `amt` varchar(30) DEFAULT NULL,
  `tid` varchar(30) DEFAULT NULL,
  `accno` varchar(30) DEFAULT NULL,
  `bname` varchar(30) DEFAULT NULL,
  `branch` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `transfer` */

insert  into `transfer`(`id`,`tof`,`amt`,`tid`,`accno`,`bname`,`branch`) values 
(1,NULL,NULL,NULL,'1132',NULL,NULL),
(2,NULL,NULL,NULL,'541',NULL,NULL),
(3,'Housing','','','541','',''),
(4,'Housing','65646','4642','1354','sred','ngghf'),
(5,'Housing','161','2532534','34536543','dghdf','sgshfd');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `reqid` varchar(30) DEFAULT NULL,
  `user` varchar(30) DEFAULT NULL,
  `amt` varchar(30) DEFAULT NULL,
  `approve` varchar(30) DEFAULT NULL,
  `reject` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`uid`,`type`,`reqid`,`user`,`amt`,`approve`,`reject`) values 
(1,'256','sasa','sahsa','sh','hsg',NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
