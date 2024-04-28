import { Component } from '@angular/core';
import { SignalementService } from "../../../services/Signalement/signalement.service";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";

@Component({
  selector: 'app-add-signalement',
  templateUrl: './add-signalement.component.html',
  styleUrls: ['./add-signalement.component.css']
})
export class AddSignalementComponent {
  signalementForm!: FormGroup;

  constructor(private signalementService: SignalementService, private formBuilder: FormBuilder) {
    this.initializeForm();
  }

  initializeForm(): void {
    this.signalementForm = this.formBuilder.group({
      pseudo: ['', Validators.required],
      code_cip: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.signalementForm.valid) {
      this.signalementService.createSignalement(this.signalementForm.value).subscribe({
        next: (res) => {
          console.log('Signalement créé', res);
          this.signalementForm.reset();
        },
        error: (err) => {
          console.log('form : ' + this.signalementForm.value)
          console.error('Erreur lors de la création du signalement', err);
          console.error('Détails de l\'erreur:', err.error);
          alert('Erreur lors de la création du signalement: ' + err.error.message);
        }
      });
    }
  }
}
