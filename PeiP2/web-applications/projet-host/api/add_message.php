<?php
include "../utils.php";
default_header();

$post = json_decode(file_get_contents("php://input"), true);
$missing = check_args($post, "user_id", "chatroom_id", "message_content", "message_date");
if (!empty($missing)) {
    exit_with_error($missing);
}

$messages = read_messages($post["user_id"], $post["chatroom_id"]);
$messages[] = [
    "chatroom_id" => $post["chatroom_id"],
    "content" => $post["message_content"],
    "user_id" => $post["user_id"],
    "data" => $post["message_date"]
];
write_messages($post["user_id"], $post["chatroom_id"], $messages);
