import {ISong} from "./songs";
export interface ISongPaginator {
  count: number;
  next: string;
  previous: string;
  results: ISong
}
