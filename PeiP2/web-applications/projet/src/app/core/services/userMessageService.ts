import { Injectable } from "@angular/core";
import { combineLatest, Observable, map } from "rxjs";
import { Messages } from "src/app/core/models/MessageModel";
import { User } from "src/app/core/models/UserModel";
import { messageService } from "src/app/core/services/messageService";
import { userService } from "src/app/core/services/userService";
import { UserMessage } from "../models/UserMessageModel";

type UserMap = Map<string, User>;

@Injectable({ providedIn: 'root' }) // Always 'root' unless you _know_ better!
export class UserMessageService {
  constructor(
    private readonly messagesService: messageService,
    private readonly usersService: userService,
  ) { }

  public getUserMessagesByRoomId(chatroomId: string): Observable<UserMessage[]> {
    return combineLatest([
      this.messagesService.getMessageByChatRoomID(chatroomId),
      this.usersService.getUserByChatroom(chatroomId).pipe(
        map((users: User[]): UserMap => {
          const ret: UserMap = new Map<string, User>();
          for (const usr of users) {
            ret.set(usr.id, usr);
          }
          return ret;
        }),
      ),
    ]).pipe(
      map(([messages, users]: [Messages[], UserMap]): UserMessage[] => {
        const ret: UserMessage[] = [];
        for (const message of messages) {
          const user: User | undefined = users.get(message.user_id);
          if (!user) {
            throw new Error(`Unknown User ID '${message.user_id}' for message ID '${message.chatroom_id /*message.id*/}' in chat room '${message.chatroom_id}'`); //TODO: create true id for message and replace message.chatroom_id by the content of the comment...
          }

          ret.push({ message, user });
        }
        return ret;
      }),
    );
  }
}
