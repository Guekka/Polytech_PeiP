import { Component, Input, OnInit } from '@angular/core';
import { UserMessage } from 'src/app/core/models/UserMessageModel';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.scss']
})
export class MessageComponent implements OnInit {
  @Input() userMsg !: UserMessage;
  constructor() { }

  ngOnInit(): void {
  }

}
