import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SingleChatRoomComponent } from './single-chat-room.component';

describe('SingleChatRoomComponent', () => {
  let component: SingleChatRoomComponent;
  let fixture: ComponentFixture<SingleChatRoomComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SingleChatRoomComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SingleChatRoomComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
