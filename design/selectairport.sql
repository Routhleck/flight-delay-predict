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

 Date: 10/07/2022 22:40:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for selectairport
-- ----------------------------
DROP TABLE IF EXISTS `selectairport`;
CREATE TABLE `selectairport`  (
  `departureId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `arriveId` varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL,
  PRIMARY KEY (`departureId`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin COMMENT = '选中机场' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
