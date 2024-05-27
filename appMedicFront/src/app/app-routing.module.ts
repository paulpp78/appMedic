import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalyticsComponent } from './components/analytics/analytics.component';
import { SignalementComponent } from './components/signalement/signalement.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { AuthGuard } from './auth.gaurd'; // Importer le AuthGuard'

const routes: Routes = [
  { path: '', component: HomepageComponent },
  { path: 'signalement', component: SignalementComponent, canActivate: [AuthGuard] },
  { path: 'analytics', component: AnalyticsComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}