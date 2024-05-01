import { Component, OnInit } from '@angular/core';
import { AnalyticsService } from '../../services/Analytics/analytics.service';
import { Analyse } from '../../models/analyse';

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css'],
})
export class AnalyticsComponent {
  constructor(private analyticsService: AnalyticsService) {}
}
