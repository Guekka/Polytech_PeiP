import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { ChatRoomListComponent } from "./components/chat-room-list/chat-room-list.component";
import { NewChatRoomComponent } from "./components/new-chat-room/new-chat-room.component";
import { SingleChatRoomComponent } from "./components/single-chat-room/single-chat-room.component";
import { AuthGuard } from '../core/guards/auth.guard';

export const routes: Routes = [
    { path: '', component: ChatRoomListComponent, canActivate: [AuthGuard] },
    { path: 'create', component: NewChatRoomComponent, canActivate: [AuthGuard] },
    { path: ':id', component: SingleChatRoomComponent, canActivate: [AuthGuard] },
]

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChatRoomRoutingModule { }