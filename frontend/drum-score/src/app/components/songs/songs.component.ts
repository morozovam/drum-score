import { Component, OnInit } from '@angular/core';
import {ISong} from "../../Models/songs";
import {SongsService} from "../../services/songs.service";
import {ScoresService} from "../../services/scores.service";
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import {ScoreComponent} from "../score/score.component";

@Component({
  selector: 'app-songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.scss']
})

export class SongsComponent implements OnInit {
  songs: ISong[] = []
  constructor(private songService: SongsService,
              private modalService: NgbModal) {
  }

  ngOnInit(): void {
    this.songService.getAll().subscribe(songs=> {
      this.songs = songs
    })
  }
  OpenScore(score_id: number) {
    const modalRef = this.modalService.open(ScoreComponent);
		modalRef.componentInstance.name = 'World';
    modalRef.componentInstance.scoreid = score_id
  }
  getSongName (song: ISong) {
    if (song.performer == null) {
      return song.song_name
    }
    if (song.performer.id == song.artist.id) {
      return song.song_name
    }
    else {
      return  song.song_name + ' (cover by ' + song.performer.artist_name + ')'
    }
  }

}
