import { HttpClient, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs/internal/Observable";
import { Messages } from "../models/MessageModel";
import { baseURL } from "./constants";

@Injectable({
    providedIn: 'root'
})
export class messageService {

    constructor(private http: HttpClient) { }

    addMessage(chatroom_id: string, content: string, user_id: string): Observable<Messages> {
        return this.http.post<Messages>(baseURL + '/add_message.php', { "user_id": "1", "chatroom_id": "1", "message_content": content, "message_date": new Date().toJSON() });
    }


    getMessageByChatRoomID(chatroomId: string): Observable<Messages[]> {//That one is a GET
        return this.http.post<Messages[]>(baseURL + '/messages.php', { "chatroom_id": chatroomId, "user_id": 1 });
    }
}