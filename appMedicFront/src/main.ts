import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";
import { bootstrapApplication } from '@angular/platform-browser';
import { provideAuth0 } from '@auth0/auth0-angular';
import { AppModule } from "./app/app.module";

// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));


  providers: [
    provideAuth0({
      domain: 'dev-s7edrnyyhek1aw2g.us.auth0.com',
      clientId: '{yourClientId}',
      authorizationParams: {
        redirect_uri: window.location.origin
      }
    }),
  ]

  