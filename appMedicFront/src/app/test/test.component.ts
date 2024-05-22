import { Component } from '@angular/core';
import { SignalementService } from '../services/Signalement/signalement.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrl: './test.component.css'
})
export class TestComponent {
  onlyNumber(event: any):boolean {
    var charCode = (event.which) ? event.which : event.keyCode;
    // Only Numbers 0-9
    if ((charCode < 48 || charCode > 57)) {
      event.preventDefault();
      return false;
    } else {
      return true;
    }
  }

  
}
