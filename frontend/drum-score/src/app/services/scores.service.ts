import {Injectable} from "@angular/core";
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {catchError, Observable, throwError} from "rxjs";
import {IScore} from "../Models/Scores";
import {ErrorService} from "./error.service";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})

export class ScoresService {
  constructor(
    private http: HttpClient,
    private errorService: ErrorService) {
  }

  getAll(score_id: Number): Observable<IScore[]>{
    return this.http.get<IScore[]>(environment.API_SERVER_ADDRESS + '/api/v1/score/?song=' + score_id
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
