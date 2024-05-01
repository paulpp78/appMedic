import { platformBrowserDynamic } from "@angular/platform-browser-dynamic";
import { bootstrapApplication } from '@angular/platform-browser';
import { AppModule } from "./app/app.module";

// Import the AuthService type from the SDK
import { AuthService } from '@auth0/auth0-angular';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));




  