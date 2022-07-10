/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50557
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50557
 File Encoding         : 65001

 Date: 10/07/2022 22:45:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for airline
-- ----------------------------
DROP TABLE IF EXISTS `airline`;
CREATE TABLE `airline`  (
  `airline` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`airline`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for airport
-- ----------------------------
DROP TABLE IF EXISTS `airport`;
CREATE TABLE `airport`  (
  `airportId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `airportName` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `weatherId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `longitude` float(10, 4) NOT NULL,
  `latitude` float(10, 4) NOT NULL,
  PRIMARY KEY (`airportId`) USING BTREE,
  INDEX `weatherId`(`weatherId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '机场表单' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for arriveweather
-- ----------------------------
DROP TABLE IF EXISTS `arriveweather`;
CREATE TABLE `arriveweather`  (
  `weatherId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `date` date NOT NULL,
  `avg_temp` float(10, 4) NOT NULL,
  `max_temp` float(10, 4) NOT NULL,
  `min_temp` float(10, 4) NOT NULL,
  `prec` float(10, 4) NOT NULL,
  `pressure` float(10, 4) NOT NULL,
  `wind_dir` float(10, 4) NOT NULL,
  `wind_sp` float(10, 4) NOT NULL,
  PRIMARY KEY (`date`) USING BTREE,
  INDEX `arriveWeather`(`weatherId`) USING BTREE,
  CONSTRAINT `arriveWeather` FOREIGN KEY (`weatherId`) REFERENCES `airport` (`weatherId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '到达天气预测表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for departureweather
-- ----------------------------
DROP TABLE IF EXISTS `departureweather`;
CREATE TABLE `departureweather`  (
  `weatherId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `avg_temp` float(10, 4) NOT NULL,
  `max_temp` float(10, 4) NOT NULL,
  `min_temp` float(10, 4) NOT NULL,
  `prec` float(10, 4) NOT NULL,
  `pressure` float(10, 4) NOT NULL,
  `wind_dir` float(10, 4) NOT NULL,
  `wind_sp` float(10, 4) NOT NULL,
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `normal_prob` float(6, 4) NULL DEFAULT NULL,
  `mild_prob` float(6, 4) NULL DEFAULT NULL,
  `moderate_prob` float(6, 4) NULL DEFAULT NULL,
  `serious_prob` float(6, 4) NULL DEFAULT NULL,
  INDEX `departureWeather`(`weatherId`) USING BTREE,
  CONSTRAINT `departureWeather` FOREIGN KEY (`weatherId`) REFERENCES `airport` (`weatherId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '出发天气预测表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for selectairport
-- ----------------------------
DROP TABLE IF EXISTS `selectairport`;
CREATE TABLE `selectairport`  (
  `departureId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `arriveId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`departureId`) USING BTREE,
  INDEX `ariAirport`(`arriveId`) USING BTREE,
  CONSTRAINT `depAirport` FOREIGN KEY (`departureId`) REFERENCES `airport` (`airportId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ariAirport` FOREIGN KEY (`arriveId`) REFERENCES `airport` (`airportId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '选中机场' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `userId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(18) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isAdmin` int(11) NOT NULL,
  PRIMARY KEY (`userId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '用户表' ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
