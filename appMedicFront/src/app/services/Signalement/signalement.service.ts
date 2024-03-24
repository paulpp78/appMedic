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

  //UPDATE
  updateSignalement(signalement: Signalement): Observable<Object> {
    return this.http.put(
      environment.apiUrl + "/signalement/" + signalement.id,
      signalement,
    );
  }
}
