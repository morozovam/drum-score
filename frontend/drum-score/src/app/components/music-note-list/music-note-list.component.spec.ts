import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicNoteListComponent } from './music-note-list.component';

describe('MusicNoteListComponent', () => {
  let component: MusicNoteListComponent;
  let fixture: ComponentFixture<MusicNoteListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MusicNoteListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MusicNoteListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
