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

 Date: 10/07/2022 22:39:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
  PRIMARY KEY (`airportId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '机场表单' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
