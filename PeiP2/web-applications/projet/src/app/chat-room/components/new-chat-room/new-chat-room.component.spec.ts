import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewChatRoomComponent } from './new-chat-room.component';

describe('NewChatRoomComponent', () => {
  let component: NewChatRoomComponent;
  let fixture: ComponentFixture<NewChatRoomComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewChatRoomComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NewChatRoomComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
