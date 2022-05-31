import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ChatRoom } from 'src/app/core/models/ChatRoomModel';
import { chatRoomService } from 'src/app/core/services/chatRoomService';

@Component({
  selector: 'app-chat-room-list',
  templateUrl: './chat-room-list.component.html',
  styleUrls: ['./chat-room-list.component.scss']
})
export class ChatRoomListComponent implements OnInit {
  chatrooms$ !: Observable<ChatRoom[]>;

  constructor(private chatRoomService: chatRoomService) { }

  ngOnInit(): void {
    this.chatrooms$ = this.chatRoomService.getAllChatroom();
  }

}
