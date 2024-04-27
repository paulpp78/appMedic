import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { HttpClientModule } from "@angular/common/http";
import { FooterComponent } from "./components/footer/footer.component";
import { NavComponent } from "./components/nav/nav.component";
import { ButtonModule } from "primeng/button";
import { SidebarModule } from "primeng/sidebar";
import { AnalyticsComponent } from "./components/analytics/analytics.component";
import { ChartModule } from "primeng/chart";

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    NavComponent,
    AnalyticsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ButtonModule,
    SidebarModule,
    ChartModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
