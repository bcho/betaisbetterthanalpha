DROP TABLE IF EXISTS `jobs`;
DROP TABLE IF EXISTS `stats`;

/* jobs queue */
CREATE TABLE `jobs` (
    `id` integer PRIMARY KEY,
    /* command */
    `value` varchar(1024) NOT NULL,
    `consumed` TINYINT(1) DEFAULT 0,
    `created` timestamp DEFAULT CURRENT_TIMESTAMP
);

/* sensor stats collection */
CREATE TABLE `stats` (
    `id` integer PRIMARY KEY,
    /* sensor stats */
    `value` varchar(1024) NOT NULL,
    `consumed` TINYINT(1) DEFAULT 0,
    `created` timestamp DEFAULT CURRENT_TIMESTAMP
);
