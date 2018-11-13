-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `e4b881e6a091e4baae`
--

DROP TABLE IF EXISTS `e4b881e6a091e4baae`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e4b881e6a091e4baae` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e4b881e6a091e4baae_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e4b881e6a091e4baae`
--

LOCK TABLES `e4b881e6a091e4baae` WRITE;
/*!40000 ALTER TABLE `e4b881e6a091e4baae` DISABLE KEYS */;
/*!40000 ALTER TABLE `e4b881e6a091e4baae` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e5ad99e5b9bfe7bfbc`
--

DROP TABLE IF EXISTS `e5ad99e5b9bfe7bfbc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e5ad99e5b9bfe7bfbc` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e5ad99e5b9bfe7bfbc_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e5ad99e5b9bfe7bfbc`
--

LOCK TABLES `e5ad99e5b9bfe7bfbc` WRITE;
/*!40000 ALTER TABLE `e5ad99e5b9bfe7bfbc` DISABLE KEYS */;
/*!40000 ALTER TABLE `e5ad99e5b9bfe7bfbc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e5ae89e685b0`
--

DROP TABLE IF EXISTS `e5ae89e685b0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e5ae89e685b0` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e5ae89e685b0_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e5ae89e685b0`
--

LOCK TABLES `e5ae89e685b0` WRITE;
/*!40000 ALTER TABLE `e5ae89e685b0` DISABLE KEYS */;
/*!40000 ALTER TABLE `e5ae89e685b0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e6bd98e784b1`
--

DROP TABLE IF EXISTS `e6bd98e784b1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e6bd98e784b1` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e6bd98e784b1_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e6bd98e784b1`
--

LOCK TABLES `e6bd98e784b1` WRITE;
/*!40000 ALTER TABLE `e6bd98e784b1` DISABLE KEYS */;
/*!40000 ALTER TABLE `e6bd98e784b1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e78e8be7bba7e5a881`
--

DROP TABLE IF EXISTS `e78e8be7bba7e5a881`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e78e8be7bba7e5a881` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e78e8be7bba7e5a881_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e78e8be7bba7e5a881`
--

LOCK TABLES `e78e8be7bba7e5a881` WRITE;
/*!40000 ALTER TABLE `e78e8be7bba7e5a881` DISABLE KEYS */;
/*!40000 ALTER TABLE `e78e8be7bba7e5a881` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e78e8be8be89`
--

DROP TABLE IF EXISTS `e78e8be8be89`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e78e8be8be89` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e78e8be8be89_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e78e8be8be89`
--

LOCK TABLES `e78e8be8be89` WRITE;
/*!40000 ALTER TABLE `e78e8be8be89` DISABLE KEYS */;
INSERT INTO `e78e8be8be89` VALUES ('www','gropu1',NULL);
/*!40000 ALTER TABLE `e78e8be8be89` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e79086e683b3`
--

DROP TABLE IF EXISTS `e79086e683b3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e79086e683b3` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e79086e683b3_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e79086e683b3`
--

LOCK TABLES `e79086e683b3` WRITE;
/*!40000 ALTER TABLE `e79086e683b3` DISABLE KEYS */;
/*!40000 ALTER TABLE `e79086e683b3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `e998bfe890a8`
--

DROP TABLE IF EXISTS `e998bfe890a8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e998bfe890a8` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `e998bfe890a8_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e998bfe890a8`
--

LOCK TABLES `e998bfe890a8` WRITE;
/*!40000 ALTER TABLE `e998bfe890a8` DISABLE KEYS */;
/*!40000 ALTER TABLE `e998bfe890a8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feng`
--

DROP TABLE IF EXISTS `feng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feng` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `feng_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feng`
--

LOCK TABLES `feng` WRITE;
/*!40000 ALTER TABLE `feng` DISABLE KEYS */;
/*!40000 ALTER TABLE `feng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hah`
--

DROP TABLE IF EXISTS `hah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hah` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `hah_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hah`
--

LOCK TABLES `hah` WRITE;
/*!40000 ALTER TABLE `hah` DISABLE KEYS */;
/*!40000 ALTER TABLE `hah` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `account` varchar(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  `addr` char(7) DEFAULT NULL,
  `friend` varchar(30) DEFAULT NULL,
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (NULL,'丁树亮','123',NULL,'e4b881e6a091e4baae'),(NULL,'孙广翼','123','55732','e5ad99e5b9bfe7bfbc'),(NULL,'王辉','123','58615','e78e8be8be89'),(NULL,'潘焱','123',NULL,'e6bd98e784b1'),(NULL,'王继威','123',NULL,'e78e8be7bba7e5a881'),(NULL,'hah','12',NULL,'hah'),(NULL,'wawa','waw',NULL,'wawa'),(NULL,'nihao ','12',NULL,''),(NULL,'www','11','63889','www'),(NULL,'xiao','1','60597','xiao'),(NULL,'feng','1','65314','feng'),(NULL,'理想','12','49361','e79086e683b3');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wawa`
--

DROP TABLE IF EXISTS `wawa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wawa` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `wawa_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wawa`
--

LOCK TABLES `wawa` WRITE;
/*!40000 ALTER TABLE `wawa` DISABLE KEYS */;
/*!40000 ALTER TABLE `wawa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `www`
--

DROP TABLE IF EXISTS `www`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `www` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `www`
--

LOCK TABLES `www` WRITE;
/*!40000 ALTER TABLE `www` DISABLE KEYS */;
INSERT INTO `www` VALUES ('孙光翼','group1',NULL),('攀岩',NULL,NULL),('王辉','gropu1',NULL),('丁术亮','gropu1',NULL);
/*!40000 ALTER TABLE `www` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xiao`
--

DROP TABLE IF EXISTS `xiao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xiao` (
  `name` varchar(30) NOT NULL,
  `user_group` varchar(30) DEFAULT NULL,
  `addr` varchar(6) DEFAULT NULL,
  KEY `name` (`name`),
  CONSTRAINT `xiao_ibfk_1` FOREIGN KEY (`name`) REFERENCES `user_info` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xiao`
--

LOCK TABLES `xiao` WRITE;
/*!40000 ALTER TABLE `xiao` DISABLE KEYS */;
/*!40000 ALTER TABLE `xiao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-29  9:09:43
