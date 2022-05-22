import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { chatRoom } from 'src/app/core/models/chat-room.model';
import { chatRoomService } from 'src/app/core/services/chat-room.service';

@Component({
  selector: 'app-chat-room-list',
  templateUrl: './chat-room-list.component.html',
  styleUrls: ['./chat-room-list.component.scss']
})
export class ChatRoomListComponent implements OnInit {
  chatrooms$ !: Observable<chatRoom[]>;

  constructor(private chatRoomService: chatRoomService) { }

  ngOnInit(): void {
    this.chatrooms$ = this.chatRoomService.getAllChatroom();
  }

}
