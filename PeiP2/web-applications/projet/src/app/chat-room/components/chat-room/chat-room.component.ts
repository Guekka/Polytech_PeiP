import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ChatRoom } from 'src/app/core/models/ChatRoomModel';
import { User } from 'src/app/core/models/UserModel';
import { userService } from 'src/app/core/services/userService';

@Component({
  selector: 'app-chat-room',
  templateUrl: './chat-room.component.html',
  styleUrls: ['./chat-room.component.scss']
})
export class ChatRoomComponent implements OnInit {
  @Input() chatroom !: ChatRoom;
  users: User[] = [];
  constructor(private router: Router,
    private userService: userService) { }

  ngOnInit(): void {
    this.loadUser();
  }

  loadUser(): void {
    this.users = this.chatroom.user_id.map(this.userService.getUserById.bind(this.userService));
  }

  onViewConversation(): void {
    console.log(this.chatroom.id);
    this.router.navigateByUrl(`/chatroom/${this.chatroom.id}`);
  }
}
