import {Injectable} from "@angular/core";
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {catchError, Observable, throwError} from "rxjs";
import {ISong} from "../Models/songs";
import {ErrorService} from "./error.service";
import {ISongPaginator} from "../Models/SongPaginator";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class SongsService {
  constructor(
    private http: HttpClient,
    private errorService: ErrorService) {
  }

  getAll(): Observable<ISong[]>{
    return this.http.get<ISong[]>(environment.API_SERVER_ADDRESS + '/api/v1/song/'
      ).pipe(
        catchError(this.errorHandler)
      )
  }
  private errorHandler(error: HttpErrorResponse) {
    this.errorService.handle(error.message)
    console.log(error.message)
    return throwError(() => error.message)
  }
}
