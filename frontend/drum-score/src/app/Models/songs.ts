import {IArtist} from "./atrist";
export interface ISong{
  id: number;
  song_name: string;
  artist: IArtist;
  performer?: IArtist | null;

}
