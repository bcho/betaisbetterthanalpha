<?php

$DB = trim(file_get_contents('config/db'));

$cursor = new SQLite3($DB);

if (!$cursor) die('connect to db failed');
