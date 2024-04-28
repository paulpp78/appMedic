/*import { bootstrapApplication } from '@angular/platform-browser';
import { provideAuth0 } from '@auth0/auth0-angular';
import { AppComponent } from './app.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideAuth0({
      domain: 'appmedic-for-you.eu.auth0.com',
      clientId: '{Rkm8I8JAXVBtgs2afBm2k0nmEq4dGsbg}',
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    }),
  ]
});

import { Component } from '@angular/core';

// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-auth-button',
  template: '<button (click)="auth.loginWithRedirect()">Log in</button>',
  standalone: true
})
export class AuthButtonComponent {
  // Inject the authentication service into your component through the constructor
  constructor(public auth: AuthService) {}
}

*/