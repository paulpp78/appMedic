import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, from } from 'rxjs';
import { Analyse } from '../../models/analyse';
import { AuthService } from '@auth0/auth0-angular';
import { switchMap, map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class AnalyticsService {
  private apiUrl = environment.apiUrl;

  constructor(
    private http: HttpClient,
    private auth: AuthService,
  ) {}

  private createHeaders(): Observable<HttpHeaders> {
    return from(this.auth.getAccessTokenSilently()).pipe(
      map((token) => {
        return new HttpHeaders({
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        });
      }),
    );
  }

  getDailySignalements(): Observable<Analyse[]> {
    return this.createHeaders().pipe(
      switchMap((headers) => {
        return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/daily`, {
          headers,
        });
      }),
    );
  }

  getWeeklySignalements(): Observable<Analyse[]> {
    return this.createHeaders().pipe(
      switchMap((headers) => {
        return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/weekly`, {
          headers,
        });
      }),
    );
  }

  getMonthlySignalements(): Observable<Analyse[]> {
    return this.createHeaders().pipe(
      switchMap((headers) => {
        return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/monthly`, {
          headers,
        });
      }),
    );
  }

  getYearlySignalements(): Observable<Analyse[]> {
    return this.createHeaders().pipe(
      switchMap((headers) => {
        return this.http.get<Analyse[]>(`${this.apiUrl}/analytics/yearly`, {
          headers,
        });
      }),
    );
  }
}
