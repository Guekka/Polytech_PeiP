import { Injectable } from "@angular/core";
import { message } from "../models/message.model";

@Injectable({
    providedIn: 'root'
})
export class messageService {

    messages: message[] = [{
        chatroom_id: '1',
        content: 'Hey (de Axel) !',
        user_id: 'a',
        date: new Date()
    },
    {
        chatroom_id: '1',
        content: 'Hey (de Edgar) !',
        user_id: 'b',
        date: new Date()
    },
    {
        chatroom_id: '2',
        content: 'Hey (de Axel) !',
        user_id: 'a',
        date: new Date()
    },
    {
        chatroom_id: '2',
        content: 'Hey (de Edgar) !',
        user_id: 'b',
        date: new Date()
    },
    {
        chatroom_id: '3',
        content: 'Hey (de Axel) !',
        user_id: 'a',
        date: new Date()
    },
    {
        chatroom_id: '3',
        content: 'Hey (de Edgar) !',
        user_id: 'b',
        date: new Date()
    }];

    addMessage(chatroom_id: string, content: string, user_id: string): void {
        this.messages.push({
            chatroom_id: chatroom_id,
            content: content,
            user_id: user_id,
            date: new Date()
        });
        console.log({
            chatroom_id: chatroom_id,
            content: content,
            user_id: user_id,
            date: new Date()
        });
    }

    getAllMessage(): message[] {
        return this.messages;
    }

    getMessageByChatRoomID(chatroomId: string): message[] {
        return this.messages.filter((msg: message) => msg.chatroom_id === chatroomId);
    }
}