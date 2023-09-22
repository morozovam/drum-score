import {ISong} from "./songs";
export interface IScore{
  id: number;
  score: string;
  score_type: string;
  song: ISong;
}
