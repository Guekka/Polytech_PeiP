import { HttpClient, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { map } from "rxjs";
import { Observable } from "rxjs/internal/Observable";
import { User } from "../models/UserModel";
import { ChatRoom } from "../models/ChatRoomModel";
import { baseURL } from "./constants";
import { chatRoomService } from "./chatRoomService";

@Injectable({
    providedIn: 'root'
})
export class userService {

    users: User[] = [{
        id: "1",
        name: 'Axel',
        email: 'test@gmail.com',
        password: 'testpassword1'
    },
    {
        id: "2",
        name: 'Edgar',
        email: 'test2@gmail.com',
        password: 'testpassword2'
    }];

    constructor(private http: HttpClient,
        private chatRoomService: chatRoomService) { }

    getAllUser(): User[] {
        return this.users;
    }

    getUserByKey(key: Function, value: string): User {
        let res = this.users.find(user => key(user) === value);
        if (res != undefined) {
            return res;
        }
        throw new Error('User not found !');
    }

    getUserById(userId: string): User /*Observable<user>*/ { //I'll potentially change this one later but not sure if it usefull or not because it work for the moment
        return this.getUserByKey((u: User) => u.id, userId);
    }

    getUserByName(userName: string): User {
        return this.getUserByKey((u: User) => u.name, userName);
    }

    getUserByChatroom(chatroomId: string): Observable<User[]> {
        return this.chatRoomService.getChatroomById(chatroomId).pipe(
            map((value: ChatRoom) => {
                let res: User[] = [];
                if (value.user_id !== undefined) {
                    for (let i = 0; i < value.user_id.length; i++) {
                        res.push(this.getUserById(value.user_id[i]));
                    }
                }
                return res;
            })
        );
    }
}