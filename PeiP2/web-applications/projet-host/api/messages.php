<?php
include "../utils.php";
default_header();

$post = json_decode(file_get_contents("php://input"), true);
$missing = check_args($post, "user_id", "chatroom_id");
if (!empty($missing)) {
    exit_with_error($missing, $post);
}

echo json_encode(read_messages($post["user_id"], $post["chatroom_id"]));
