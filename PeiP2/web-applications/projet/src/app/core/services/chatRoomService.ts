import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { filter, map, Observable, tap } from "rxjs";
import { ChatRoom } from "../models/ChatRoomModel";
import { baseURL } from "./constants";

@Injectable({
    providedIn: 'root'
})
export class chatRoomService {

    constructor(private http: HttpClient) { }

    getAllChatroom(): Observable<ChatRoom[]> { //That one is a GET...
        return this.http.post<ChatRoom[]>(baseURL + '/chatrooms.php', { "user_id": 1 });
    }

    getChatroomById(chatroomId: string): Observable<ChatRoom> {
        return this.getAllChatroom().pipe(
            map((value: ChatRoom[]) => {
                for (let i = 0; i < value.length; i++) {
                    if (value[i].id === chatroomId) {
                        return value[i]
                    }
                }
                throw new Error('Chatroom not found !');
            })
        );
    }
}
