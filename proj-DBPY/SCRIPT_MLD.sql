-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ProjPy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ProjPy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ProjPy` DEFAULT CHARACTER SET utf8 ;
USE `ProjPy` ;

-- -----------------------------------------------------
-- Table `ProjPy`.`exercices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`exercices` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`players` (
  `id` INT NOT NULL,
  `pseudo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjPy`.`exercices_has_played`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjPy`.`exercices_has_played` (
  `exercices_id` INT NOT NULL,
  `players_id` INT NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  `duration` VARCHAR(45) NOT NULL,
  `nbOk` VARCHAR(45) NOT NULL,
  `nbTotal` VARCHAR(45) NOT NULL,
  `dateAndHour` DATETIME NOT NULL,
  INDEX `fk_game_has_players_players1_idx` (`players_id` ASC) VISIBLE,
  INDEX `fk_game_has_players_game_idx` (`exercices_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_game_has_players_game`
    FOREIGN KEY (`exercices_id`)
    REFERENCES `ProjPy`.`exercices` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_game_has_players_players1`
    FOREIGN KEY (`players_id`)
    REFERENCES `ProjPy`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
