<?php
include "../utils.php";
default_header();

$post = json_decode(file_get_contents("php://input"), true);
$missing = check_args($post, "user_id", "chatroom_name");
if (!empty($missing)) {
    exit_with_error($missing);
}

$chatrooms = read_chatrooms($post["user_id"]);
$id = count($chatrooms) + 1;
$chatrooms[$id] = [
    "name" => $post["chatroom_name"],
    "user_id" => [$post["user_id"]]
];
write_chatrooms($post["user_id"], $chatrooms);
