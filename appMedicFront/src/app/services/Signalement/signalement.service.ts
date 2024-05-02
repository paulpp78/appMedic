import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../../environments/environment";
import { Signalement } from "../../models/signalement";
import { Observable } from "rxjs";

@Injectable({
  providedIn: "root",
})
export class SignalementService {
  constructor(private http: HttpClient) {}
  //GET
  getSignalements(): Observable<Signalement[]> {
    return this.http.get<Signalement[]>(environment.apiUrl + "/signalement");
  }
  //GET
  getSignalementById(id: number): Observable<Signalement> {
    return this.http.get<Signalement>(
      environment.apiUrl + "/signalement/" + id,
    );
  }
  //POST
  createSignalement(signalement: Signalement): Observable<Signalement> {
    return this.http.post<Signalement>(
      environment.apiUrl + "/signalement",
      signalement,
    );
  }
  //DELETE
  deleteSignalement(id: number): Observable<Signalement> {
    return this.http.delete<Signalement>(
      environment.apiUrl + "/signalement/" + id,
    );
  }

  //UPDATE
  updateSignalement(signalement: Signalement): Observable<Signalement> {
    return this.http.put<Signalement>(
      environment.apiUrl + "/signalement",
      signalement,
    );
  }
}
