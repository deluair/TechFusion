import faker
import random
import numpy as np

class CompanyGenerator:
    """Generates synthetic company data for M&A simulation."""

    def __init__(self):
        self.fake = faker.Faker()

    def _generate_financial_metrics(self, sector):
        """Generates financial metrics for a company."""
        arr = random.uniform(1_000_000, 500_000_000)
        growth_rate = random.uniform(-0.1, 0.5)
        ebitda_margin = random.uniform(-0.5, 0.3)
        burn_rate = abs(random.uniform(-500_000, -10_000)) if ebitda_margin < 0 else 0
        runway = (arr / 12 * ebitda_margin) / burn_rate if burn_rate > 0 else float('inf')

        # Sector specific adjustments
        if sector == 'AI':
            growth_rate *= 1.5
            ebitda_margin *= 0.8
        elif sector == 'Cybersecurity':
            growth_rate *= 1.2
            ebitda_margin *= 1.1

        return {
            "arr": round(arr, 2),
            "growth_rate": round(growth_rate, 2),
            "ebitda_margin": round(ebitda_margin, 2),
            "burn_rate": round(burn_rate, 2),
            "runway_months": round(runway, 1) if runway != float('inf') else 'infinite'
        }

    def _generate_technology_profile(self):
        """Generates a profile of the company's technology assets."""
        all_assets = [
            'Natural Language Processing', 'Computer Vision Model', 
            'Recommendation Engine', 'Predictive Analytics Suite',
            'Fraud Detection System', 'Autonomous Vehicle Tech',
            'Voice Recognition API', 'Data-Intensive Cloud Platform'
        ]
        return {
            "patents": random.randint(0, 500),
            "assets": random.sample(all_assets, k=random.randint(1, 3))
        }

    def _generate_market_position(self):
        """Generates market position details."""
        return {
            "customer_concentration": round(random.uniform(0.05, 0.4), 2),
            "churn_rate": round(random.uniform(0.02, 0.25), 2),
            "competitive_moat": random.choice(["Network Effects", "High Switching Costs", "Brand Equity", "Proprietary Tech", "Scale Advantage"])
        }

    def _generate_team_composition(self):
        """Generates team composition details."""
        total_employees = random.randint(50, 5000)
        engineering_ratio = random.uniform(0.3, 0.7)
        engineers = int(total_employees * engineering_ratio)
        ai_ml_expertise_ratio = random.uniform(0.1, 0.5)
        return {
            "total_employees": total_employees,
            "engineering_ratio": round(engineering_ratio, 2),
            "ai_ml_experts": int(engineers * ai_ml_expertise_ratio),
            "retention_rate": round(random.uniform(0.75, 0.98), 2)
        }

    def _generate_operational_metrics(self):
        """Generates operational metrics."""
        cac = random.uniform(500, 10000)
        ltv = cac * random.uniform(3, 10)
        return {
            "cloud_costs_per_month": round(random.uniform(100_000, 2_000_000), 2),
            "customer_acquisition_cost": round(cac, 2),
            "lifetime_value": round(ltv, 2)
        }

    def generate_company(self):
        """Generates a single synthetic company profile."""
        sector = random.choice(['AI', 'Cybersecurity', 'SaaS', 'Infrastructure', 'Marketing Tech', 'Computer Vision'])
        company_name = self.fake.company()
        
        financials = self._generate_financial_metrics(sector)
        
        company = {
            "name": company_name,
            "sector": sector,
            "year_founded": random.randint(2010, 2024),
            "location": self.fake.city(),
            "financials": financials,
            "technology": self._generate_technology_profile(),
            "market_position": self._generate_market_position(),
            "team": self._generate_team_composition(),
            "operations": self._generate_operational_metrics(),
            "integration_factors": {
                "tech_stack": random.sample(['Python', 'Java', 'Go', 'AWS', 'Azure', 'GCP', 'React', 'Vue', 'Kubernetes'], k=random.randint(2, 4)),
                "team_culture": random.choice(['agile', 'hierarchical', 'remote-first', 'sales-driven']),
                "product_architecture": random.choice(['monolith', 'microservices', 'hybrid'])
            }
        }
        return company

    def generate_companies(self, num_companies):
        """Generates a list of synthetic company profiles."""
        return [self.generate_company() for _ in range(num_companies)]

if __name__ == '__main__':
    generator = CompanyGenerator()
    companies = generator.generate_companies(5)
    import json
    print(json.dumps(companies, indent=2))
