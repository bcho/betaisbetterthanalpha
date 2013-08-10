<?php

require_once('../dispatch.php');


$raw = '关闭电视';

if (preg_match($op_, $raw, $matches)) {
    var_dump($matches);
}
