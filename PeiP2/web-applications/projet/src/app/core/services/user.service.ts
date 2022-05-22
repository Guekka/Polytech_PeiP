import { Injectable } from "@angular/core";
import { user } from "../models/user.model";

@Injectable({
    providedIn: 'root'
})
export class userService {

    users: user[] = [{
        id: 'a',
        name: 'Axel',
        email: 'test@gmail.com',
        password: 'testpassword1'
    },
    {
        id: 'b',
        name: 'Edgar',
        email: 'test2@gmail.com',
        password: 'testpassword2'
    }];

    getAllUser(): user[] {
        return this.users;
    }

    getUserByKey(key: Function, value: string): user {
        let res = this.users.find(user => key(user) === value);
        if (res != undefined) {
            return res;
        }
        throw new Error('User not found !');
    }

    getUserById(userId: string): user {
        return this.getUserByKey((u: user) => u.id, userId);
    }

    getUserByName(userName: string): user {
        return this.getUserByKey((u: user) => u.name, userName);
    }
}