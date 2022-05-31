import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { combineLatest, map, Observable, switchMap } from 'rxjs';
import { ChatRoom } from 'src/app/core/models/ChatRoomModel';
import { UserMessage } from 'src/app/core/models/UserMessageModel';
import { chatRoomService } from 'src/app/core/services/chatRoomService';
import { UserMessageService } from 'src/app/core/services/userMessageService';

interface ViewModel {
  chatroom: ChatRoom;
  messages: UserMessage[];
}

@Component({
  selector: 'app-single-chat-room',
  templateUrl: './single-chat-room.component.html',
  styleUrls: ['./single-chat-room.component.scss']
})
export class SingleChatRoomComponent implements OnInit {

  messages$ !: Observable<UserMessage[]>;
  chatroom$ !: Observable<ChatRoom>;
  content: string = '';
  viewmodel$: Observable<ViewModel>;

  constructor(private route: ActivatedRoute,
    private userMessageService: UserMessageService,
    private chatroomService: chatRoomService) {
    this.viewmodel$ = this.route.paramMap.pipe(
      map((params: ParamMap): string => {
        const maybeId: string | null = params.get('id');
        if (maybeId !== null) {
          return maybeId;
        }
        throw new Error("Id isn't appropriate please retry");
      }),
      // Switch from the this.route.paramMap Observable to a new Observable, map (transform) the emissions
      switchMap(
        // switch from this.route.paramMap to Observable<ViewModel>.
        // map chatroomId to ViewModel
        (chatroomId: string): Observable<ViewModel> =>
          // Take a mapping of Observables and combine them into a single Observable
          // Take the latest values from each Observable combined.
          combineLatest({
            chatroom: this.chatroomService.getChatroomById(chatroomId),
            messages: this.userMessageService.getUserMessagesByRoomId(chatroomId),
          }),
      ),
    );
  }

  ngOnInit(): void {
  }


  // onClickSend() { //currently not working comment it for test
  //   if (this.content !== '') {
  //     this.messageService.addMessage(this.chatroom$.get('id'), this.content, 'test'); //'test' will be replaced by id of logged user later...
  //     this.content = '';
  //   }
  // }
}
