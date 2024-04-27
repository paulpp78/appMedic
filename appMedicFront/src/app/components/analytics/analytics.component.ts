import { Component, OnInit } from "@angular/core";
import { AnalyticsService } from "../../services/Analytics/analytics.service";

@Component({
  selector: "app-analytics",
  templateUrl: "./analytics.component.html",
  styleUrls: ["./analytics.component.css"],
})
export class AnalyticsComponent implements OnInit {
  data: any;
  options: any;

  constructor(private analyticsService: AnalyticsService) {}

  ngOnInit() {
    this.analyticsService.getDailySignalements().subscribe((result) => {
      this.data = {
        labels: result.map((r) => `${r._id.code_cip}`),
        datasets: [
          {
            data: result.map((r) => r.count),
            backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
            hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
          },
        ],
      };

      this.options = {
        title: {
          display: true,
          text: "Analyse des Signalements par Journée",
          fontSize: 16,
        },
        legend: {
          position: "bottom",
        },
      };
    });
  }
}
