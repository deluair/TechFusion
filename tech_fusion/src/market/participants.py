import random

class Acquirer:
    """Base class for an acquirer."""
    def __init__(self, name, acquirer_type, investment_focus):
        self.name = name
        self.type = acquirer_type
        self.investment_focus = investment_focus

class StrategicAcquirer(Acquirer):
    """Represents a strategic acquirer, e.g., a tech giant."""
    def __init__(self, name, investment_focus, integration_factors, strategic_needs):
        super().__init__(name, "Strategic", investment_focus)
        self.synergy_potential = random.uniform(0.1, 0.5)
        self.integration_factors = integration_factors
        self.strategic_needs = strategic_needs

class FinancialBuyer(Acquirer):
    """Represents a financial buyer, e.g., a private equity firm."""
    def __init__(self, name, investment_focus):
        super().__init__(name, "Financial", investment_focus)
        self.dry_powder_b = random.uniform(1, 500) # in billions

class Advisor:
    """Represents an advisory firm."""
    def __init__(self, name, advisor_type, specialization):
        self.name = name
        self.type = advisor_type
        self.specialization = specialization


def get_sample_participants():
    """Returns a list of sample market participants."""
    strategic_acquirers = [
        StrategicAcquirer("TechCorp (Google-like)", ["AI", "Cloud", "Infrastructure"], 
                          {'tech_stack': ['Python', 'Go', 'GCP', 'Kubernetes'], 'team_culture': 'agile', 'product_architecture': 'microservices'},
                          strategic_needs=['Voice Recognition API', 'Predictive Analytics Suite']),
        StrategicAcquirer("Innovate Inc. (Microsoft-like)", ["SaaS", "Cybersecurity", "AI"], 
                          {'tech_stack': ['C#', 'Java', 'Azure', 'React'], 'team_culture': 'hierarchical', 'product_architecture': 'hybrid'},
                          strategic_needs=['Recommendation Engine', 'Fraud Detection System']),
        StrategicAcquirer("Global Solutions (Amazon-like)", ["Infrastructure", "Logistics", "AI"], 
                          {'tech_stack': ['Java', 'Python', 'AWS', 'Kubernetes'], 'team_culture': 'remote-first', 'product_architecture': 'microservices'},
                          strategic_needs=['Data-Intensive Cloud Platform', 'Autonomous Vehicle Tech'])
    ]

    financial_buyers = [
        FinancialBuyer("Vista Equity Partners-like", ["SaaS"]),
        FinancialBuyer("Thoma Bravo-like", ["Cybersecurity", "SaaS"]),
        FinancialBuyer("Sequoia Growth-like", ["High-Growth Tech"])
    ]

    advisors = [
        Advisor("Goldman Sachs-like", "Investment Bank", "Tech M&A"),
        Advisor("Kirkland & Ellis-like", "Legal Firm", "Private Equity Deals"),
        Advisor("Deloitte-like", "Accounting Firm", "Due Diligence")
    ]

    return strategic_acquirers, financial_buyers, advisors

if __name__ == '__main__':
    strategic, financial, advisors = get_sample_participants()
    
    print("--- Strategic Acquirers ---")
    for acq in strategic:
        print(f"{acq.name} (Focus: {', '.join(acq.investment_focus)})")

    print("\n--- Financial Buyers ---")
    for acq in financial:
        print(f"{acq.name} (Dry Powder: ${acq.dry_powder_b:.2f}B)")

    print("\n--- Advisors ---")
    for adv in advisors:
        print(f"{adv.name} ({adv.type} - {adv.specialization})")
