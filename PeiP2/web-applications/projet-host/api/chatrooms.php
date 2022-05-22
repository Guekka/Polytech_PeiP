<?php
include "../utils.php";
default_header();

$post = json_decode(file_get_contents("php://input"), true);
/*
print_r($post);
exit();*/

$missing = check_args($post, "user_id");
if (!empty($missing)) {
    exit_with_error($missing);
}

echo json_encode(read_chatrooms($post["user_id"]));
