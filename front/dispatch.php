<?php

require_once('msg/help.php');
require_once('msg/op.php');

require_once('arduino/op.php');


/* patterns */

/* turn on/off */
$op_ = '/^(关闭|打开)(.*)/';


function dispatch($raw) {
    $raw = trim($raw);

    if ($raw === '帮助' || $raw === 'h' || $raw === 'help') {
        return msg_help();
    }

    /* turn on/off */
    preg_match($op_, $raw, $matches);
    if ($matches) {
        $op = $matches[1];
        $obj = $matches[2];

        ard_op($op, $obj);
        return msg_op($op, $obj);
    }

    return $raw . ' ' . msg_help();
}
