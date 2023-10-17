-- Creates a table if it does not exist
-- Adds values

CREATE TABLE IF NOT EXISTS `second_table`(
        id INT,
        name VARCHAR(256),
        score INT
);

INSERT INTO `second_table` (`id`, `name`, `score`, `created_on`) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 18);
