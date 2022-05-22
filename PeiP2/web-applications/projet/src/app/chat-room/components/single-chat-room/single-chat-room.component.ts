import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { chatRoom } from 'src/app/core/models/chat-room.model';
import { message } from 'src/app/core/models/message.model';
import { user } from 'src/app/core/models/user.model';
import { chatRoomService } from 'src/app/core/services/chat-room.service';
import { messageService } from 'src/app/core/services/message.service';
import { userService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-single-chat-room',
  templateUrl: './single-chat-room.component.html',
  styleUrls: ['./single-chat-room.component.scss']
})
export class SingleChatRoomComponent implements OnInit {

  messages !: [user, message][];
  chatroom !: chatRoom;
  content: string = '';

  constructor(private route: ActivatedRoute,
    private messageService: messageService,
    private userService: userService,
    private chatroomService: chatRoomService) { }

  ngOnInit(): void {
    const chatroomId = this.route.snapshot.params['id'];
    this.chatroom = this.chatroomService.getChatroomById(chatroomId);
    this.loadMessage(chatroomId);
  }

  loadMessage(chatroomId: string) {
    this.messages = this.messageService.getMessageByChatRoomID(chatroomId)
      .map((msg: message) => [this.userService.getUserById(msg.user_id), msg]);
  }

  onClickSend() {
    if (this.content !== '') {
      this.messageService.addMessage(this.chatroom.id, this.content, 'test');
      this.content = '';
    }
  }
}
