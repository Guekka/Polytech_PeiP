import { Component, Input, OnInit } from '@angular/core';
import { tap } from 'rxjs';
import { ChatRoom } from 'src/app/core/models/ChatRoomModel';
import { messageService } from 'src/app/core/services/messageService';

@Component({
  selector: 'app-message-input',
  templateUrl: './message-input.component.html',
  styleUrls: ['./message-input.component.scss']
})
export class MessageInputComponent implements OnInit {
  @Input() chatroom!: ChatRoom;

  content: string = '';

  constructor(private messageService: messageService) { }

  ngOnInit(): void {
  }

  onClickSend(): void {
    if (this.content !== "") {
      let a = this.messageService.addMessage(this.chatroom.id, this.content, '1').subscribe();
    }
    this.content = '';
  }
}
