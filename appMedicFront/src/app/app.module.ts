import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { FooterComponent } from './components/footer/footer.component';
import { NavComponent } from './components/nav/nav.component';
import { ButtonModule } from 'primeng/button';
import { SidebarModule } from 'primeng/sidebar';
import { AnalyticsComponent } from './components/analytics/analytics.component';
import { ChartModule } from 'primeng/chart';
import { AddSignalementComponent } from './components/signalement/add-signalement/add-signalement.component';
import { GetListSignalementComponent } from './components/signalement/get-list-signalement/get-list-signalement.component';
import { SignalementComponent } from './components/signalement/signalement.component';
import { InputTextModule } from 'primeng/inputtext';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TableModule } from 'primeng/table';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AnalyticsByDayComponent } from './components/analytics/analytics-by-day/analytics-by-day.component';
import { AnalyticsByWeekComponent } from './components/analytics/analytics-by-week/analytics-by-week.component';
import { AnalyticsByMonthComponent } from './components/analytics/analytics-by-month/analytics-by-month.component';
import { AnalyticsByYearComponent } from './components/analytics/analytics-by-year/analytics-by-year.component';
import { environment } from '../environments/environment';

import { AuthModule } from '@auth0/auth0-angular';
import { HeaderComponent } from './components/layout/header/header.component';
import { HomepageComponent } from './components/homepage/homepage.component';




@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    NavComponent,
    AnalyticsComponent,
    AddSignalementComponent,
    GetListSignalementComponent,
    SignalementComponent,
    AnalyticsByDayComponent,
    AnalyticsByWeekComponent,
    AnalyticsByMonthComponent,
    AnalyticsByYearComponent,


    HeaderComponent, 
    HomepageComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ButtonModule,
    SidebarModule,
    ChartModule,
    InputTextModule,
    FormsModule,
    ReactiveFormsModule,
    TableModule,
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    AuthModule.forRoot({
      domain: environment.auth.domain,
      clientId: environment.auth.clientId,
      authorizationParams: {
        redirect_uri: environment.auth.redirectUri,
        audience: environment.auth.audience, // Audience ici
        scope: 'openid profile email' // Scopes nécessaires
      }
    }),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }