import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, tap } from "rxjs";
import { chatRoom } from "../models/chat-room.model";
import { baseURL } from "./constants";

@Injectable({
    providedIn: 'root'
})
export class chatRoomService {
    chatrooms: chatRoom[] = [{
        name: 'chatroom 1',
        id: '1',
        user_id: ['a', 'b']
    },
    {
        name: 'chatroom 2',
        id: '2',
        user_id: ['a', 'b']
    },
    {
        name: 'chatroom 3',
        id: '3',
        user_id: ['a', 'b']
    }];

    constructor(private http: HttpClient) { }

    getAllChatroom(): Observable<chatRoom[]> {
        return this.http.post<chatRoom[]>(baseURL + '/chatrooms.php', { "user_id": 1 });
    }

    getChatroomById(chatroomId: string): chatRoom {
        let res = this.chatrooms.find((chatroom: chatRoom) => chatroom.id === chatroomId);
        if (res) {
            return res;
        }
        throw new Error('Chatroom not found !');
    }
}
