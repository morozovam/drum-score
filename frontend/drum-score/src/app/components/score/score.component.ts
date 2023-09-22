import { Component, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ScoresService } from "../../services/scores.service";
import {ISong} from "../../Models/songs";
import {IScore} from "../../Models/Scores";


@Component({
  selector: 'app-score',
  templateUrl: './score.component.html',
  styleUrls: ['./score.component.scss']
})
export class ScoreComponent {
	@Input() name: any
  public scoreid: Number = 0
  scores: IScore[] = []


	constructor(public activeModal: NgbActiveModal,
              private scoreService: ScoresService) {}
  ngOnInit(): void {
    this.scoreService.getAll(this.scoreid).subscribe( scores => {
      this.scores = scores
      if (this.scores.length==0 ) {
        this.activeModal.close()
      }
    })
  }
  getSongName(song: ISong): String {
    if (song.performer == null) {
      return song.artist.artist_name + ' - ' + song.song_name
    }

    if (song.performer.id == song.artist.id)  {
      return song.artist.artist_name + ' - ' + song.song_name

    }
    else {
      return song.artist.artist_name + ' - ' + song.song_name + ' (cover by ' + song.performer.artist_name + ')'
    }
  }
}
