import csv
import os
from datetime import datetime

class ReportGenerator:
    """Generates reports for the M&A simulation."""

    def __init__(self, report_dir='reports'):
        self.report_dir = report_dir
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def generate_deals_report(self, completed_deals):
        """Generates a CSV report of all completed deals."""
        if not completed_deals:
            print("No deals were completed, so no report will be generated.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.report_dir, f"simulation_report_{timestamp}.csv")

        headers = [
            'Acquirer', 'Target', 'Target Sector', 'Base Valuation',
            'Final Price', 'Deal Structure', 'Negotiated Premium (%)',
            'Synergy Premium (%)', 'Synergy Score', 'Matched Synergy Assets'
        ]

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            for deal in completed_deals:
                writer.writerow({
                    'Acquirer': deal.acquirer.name,
                    'Target': deal.target['name'],
                    'Target Sector': deal.target['sector'],
                    'Base Valuation': f"{deal.base_valuation:,.2f}",
                    'Final Price': f"{deal.final_price:,.2f}",
                    'Deal Structure': deal.structure,
                    'Negotiated Premium (%)': f"{deal.negotiated_premium:.2%}",
                    'Synergy Premium (%)': f"{deal.synergy_details.get('premium', 0):.2%}",
                    'Synergy Score': deal.synergy_details.get('score', 0),
                    'Matched Synergy Assets': ', '.join(deal.synergy_details.get('matched_assets', []))
                })
        
        print(f"\nSimulation report generated successfully: {filename}")
