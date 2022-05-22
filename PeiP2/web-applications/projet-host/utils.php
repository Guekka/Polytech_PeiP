<?php
function default_header()
{
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Headers: *');
    header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
    header('Content-Type: application/json');
}

function check_args($post, string ...$args)
{
    $missing = [];
    foreach ($args as $arg) {
        if (!isset($post[$arg])) {
            $missing[] = $arg;
        }
    }
    return $missing;
}

function exit_with_error($missing)
{
    $error = [
        "error" => "Missing arguments: " . implode("; ", $missing)
    ];
    echo json_encode($error);
    exit();
}

const DB_PATH = "../db";

// Writes data as JSON
function _write_db($path, $data)
{
    file_put_contents(DB_PATH . "/$path", json_encode($data));
}

// Reads data as JSON
function _read_db($path)
{
    return json_decode(file_get_contents(DB_PATH . "/$path"), true);
}

function read_users()
{
    return _read_db("users.json");
}

function write_users($users)
{
    _write_db("users.json", $users);
}

function read_chatrooms($user_id)
{
    return _read_db("$user_id/chatrooms.json");
}

function write_chatrooms($user_id, $chatrooms)
{
    _write_db("$user_id/chatrooms.json", $chatrooms);
}

function read_messages($user_id, $chatroom_id)
{
    return _read_db("$user_id/messages/$chatroom_id.json");
}

function write_messages($user_id, $chatroom_id, $messages)
{
    // Create directory if it doesn't exist
    if (!file_exists(DB_PATH . "/$user_id/messages")) {
        mkdir(DB_PATH . "$user_id/messages");
    }
    _write_db("$user_id/messages/$chatroom_id.json", $messages);
}
