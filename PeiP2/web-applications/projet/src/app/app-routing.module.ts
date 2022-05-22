import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { LandingPageComponent } from "./landing-page/components/landing-page/landing-page.component";

const routes: Routes = [
    { path: 'chatroom', loadChildren: () => import('./chat-room/chat-room.module').then(m => m.ChatRoomModule) },
    { path: '', component: LandingPageComponent }
]

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [
        RouterModule
    ]
})
export class AppRoutingModule { }