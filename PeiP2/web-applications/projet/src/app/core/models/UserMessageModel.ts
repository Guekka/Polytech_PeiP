import { Messages } from "./MessageModel";
import { User } from "./UserModel";

export interface UserMessage { // What I called ChatMessage before
    message: Messages;
    user: User;
}