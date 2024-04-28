import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalyticsComponent } from './components/analytics/analytics.component';
import { SignalementComponent } from './components/signalement/signalement.component';

const routes: Routes = [
  { path: '', redirectTo: '/signalement', pathMatch: 'full' },
  { path: 'signalement', component: SignalementComponent },
  { path: 'analytics', component: AnalyticsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
