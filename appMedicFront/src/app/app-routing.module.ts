import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignupComponent } from './components/signup/signup.component';
import { LoginComponent } from './components/login/login.component';
import { AnalyticsComponent } from './components/analytics/analytics.component';
import { SignalementComponent } from './components/signalement/signalement.component';


const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
   { path: '**', redirectTo: '/login', pathMatch: 'full' },
  { path: '', redirectTo: '/signalement', pathMatch: 'full' },
  { path: 'signalement', component: SignalementComponent },
  { path: 'analytics', component: AnalyticsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
/*const routes: Routes = [
  { path: 'login', component: LoginComponent },

  { path: 'signup', component: SignupComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' }, // Redirection vers la page de connexion par défaut
  { path: '**', redirectTo: '/login', pathMatch: 'full' }, // Gère les chemins non définis en les redirigeant également vers la page de connexion
  
  // Après la connexion, rediriger ici
  { path: 'signalement', component: SignalementComponent },
  { path: 'analytics', component: AnalyticsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
*/