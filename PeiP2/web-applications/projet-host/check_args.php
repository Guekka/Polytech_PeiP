<?php
function check_args()
{
    $args = func_get_args();
    $missing = [];
    foreach ($args as $arg) {
        if (!isset($_POST[$arg])) {
            $missing[] = $arg;
        }
    }
    return $missing;
}
