import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { chatRoom } from 'src/app/core/models/chat-room.model';
import { user } from 'src/app/core/models/user.model';
import { userService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-chat-room',
  templateUrl: './chat-room.component.html',
  styleUrls: ['./chat-room.component.scss']
})
export class ChatRoomComponent implements OnInit {
  @Input() chatroom !: chatRoom;

  users: user[] = [];
  constructor(private router: Router,
    private userService: userService) { }

  ngOnInit(): void {
    this.loadUser();
  }

  loadUser(): void {
    this.users = this.chatroom.user_id.map(this.userService.getUserById.bind(this.userService));
  }

  onViewConversation(): void {
    this.router.navigateByUrl(`/chatroom/${this.chatroom.id}`);
  }
}
