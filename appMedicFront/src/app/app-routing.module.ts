import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnalyticsComponent } from './components/analytics/analytics.component';
import { SignalementComponent } from './components/signalement/signalement.component';
import { AuthGuardService } from './services/authGuard/auth-guard.service';

const routes: Routes = [
  { path: '', redirectTo: '/signalement', pathMatch: 'full' },
  {
    path: 'signalement',
    component: SignalementComponent,
    canActivate: [AuthGuardService],
  },
  { path: 'analytics', component: AnalyticsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
