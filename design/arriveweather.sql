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

 Date: 10/07/2022 22:39:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
  PRIMARY KEY (`date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '到达天气预测表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
