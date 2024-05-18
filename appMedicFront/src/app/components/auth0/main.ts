import { bootstrapApplication } from '@angular/platform-browser';
import { provideAuth0 } from '@auth0/auth0-angular';
import { AppComponent } from './app.component';

bootstrapApplication(AppComponent, {
  providers: [
    provideAuth0({
      domain: 'appmedic-for-you.eu.auth0.com',
      clientId: 'Rkm8I8JAXVBtgs2afBm2k0nmEq4dGsbg',
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    }),
  ]
});