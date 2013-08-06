<?php

$config = parse_ini_file('config.ini',  1);
$DB = $config['db']['name'];

$cursor = new SQLite3($DB);

if (!$cursor) die('connect to db failed');
