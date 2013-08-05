DROP TABLE IF EXISTS `jobs`;

/* jobs queue */
CREATE TABLE `jobs` (
    `id` integer PRIMARY KEY,
    `value` varchar(1024) NOT NULL,
    `consumed` TINYINT(1) DEFAULT 0,
    `created` timestamp DEFAULT CURRENT_TIMESTAMP
);
