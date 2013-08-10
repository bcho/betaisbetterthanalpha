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
    if (strpos($raw, '打开') === 0) {
        $op = '打开';
        $obj = trim(explode($op, $raw)[1]);

        ard_op($op, $obj);
        return msg_op($op, $obj);
    }
    if (strpos($raw, '关闭') === 0) {
        $op = '关闭';
        $obj = trim(explode($op, $raw)[1]);

        ard_op($op, $obj);
        return msg_op($op, $obj);
    }

    return $raw . ' ' . msg_help();
}
