import { Injectable } from "@angular/core";
import { environment } from "../../../environments/environment";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Analyse } from "../../models/analyse";

@Injectable({
  providedIn: "root",
})
export class AnalyticsService {
  private apiUrl = environment.apiUrl;
  constructor(private http: HttpClient) {}

  getDailySignalements(): Observable<Analyse[]> {
    return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/daily`);
  }

  getWeeklySignalements(): Observable<Analyse[]> {
    return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/weekly`);
  }

  getMonthlySignalements(): Observable<Analyse[]> {
    return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/monthly`);
  }

  getYearlySignalements(): Observable<Analyse[]> {
    return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/yearly`);
  }
}
