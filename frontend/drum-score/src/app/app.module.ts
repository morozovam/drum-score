import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SongsComponent } from './components/songs/songs.component';
import { HttpClientModule } from "@angular/common/http";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './components/navbar/navbar.component';
import { MainComponent } from './components/main/main.component';
import { ScoreComponent } from './components/score/score.component';
import { MusicNoteListComponent } from './components/music-note-list/music-note-list.component';

@NgModule({
  declarations: [
    AppComponent,
    SongsComponent,
    NavbarComponent,
    MainComponent,
    ScoreComponent,
    MusicNoteListComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
