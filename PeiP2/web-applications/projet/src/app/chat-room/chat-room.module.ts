import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChatRoomComponent } from './components/chat-room/chat-room.component';
import { ChatRoomListComponent } from './components/chat-room-list/chat-room-list.component';
import { SingleChatRoomComponent } from './components/single-chat-room/single-chat-room.component';
import { NewChatRoomComponent } from './components/new-chat-room/new-chat-room.component';
import { ChatRoomRoutingModule } from './chat-room-routing.module';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    ChatRoomComponent,
    ChatRoomListComponent,
    SingleChatRoomComponent,
    NewChatRoomComponent
  ],
  imports: [
    CommonModule,
    ChatRoomRoutingModule,
    FormsModule
  ],
  exports: [
    ChatRoomComponent,
    ChatRoomListComponent,
    SingleChatRoomComponent
  ]
})
export class ChatRoomModule { }
