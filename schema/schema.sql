CREATE TABLE `blog` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(250) NULL,
  `text` VARCHAR(4000) NULL,
    PRIMARY KEY (`id`));


CREATE TABLE `brand` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(250) NULL,
    PRIMARY KEY (`id`));


CREATE TABLE `cars` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(100) NULL,
  `km` int NULL,
  `comment` VARCHAR(250) NULL,
  `brand_id` int not NULL,
  INDEX car_brand_idx (brand_id),
  FOREIGN KEY (brand_id)
  REFERENCES brand(id)
  ON DELETE CASCADE,
   PRIMARY KEY (id));

