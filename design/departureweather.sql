/*
 Navicat Premium Data Transfer

 Source Server         : 0707test
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : 8.141.236.100:3306
 Source Schema         : db01

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 10/07/2022 22:40:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
  `year` int NOT NULL,
  `month` int NOT NULL,
  `day` int NOT NULL,
  `normal_prob` float(6, 4) NULL DEFAULT NULL,
  `mild_prob` float(6, 4) NULL DEFAULT NULL,
  `moderate_prob` float(6, 4) NULL DEFAULT NULL,
  `serious_prob` float(6, 4) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '出发天气预测表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
