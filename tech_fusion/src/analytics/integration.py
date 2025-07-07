import random

class IntegrationComplexity:
    """Calculates a score representing the difficulty of integrating a target company."""

    def __init__(self):
        # Weights for different factors
        self.weights = {
            'tech_stack': 0.5,
            'team_culture': 0.3,
            'product_architecture': 0.2
        }

    def _score_tech_stack(self, acquirer_stack, target_stack):
        """Scores based on the percentage of overlapping technologies."""
        overlap = len(set(acquirer_stack) & set(target_stack))
        total_unique = len(set(acquirer_stack) | set(target_stack))
        similarity = overlap / total_unique if total_unique > 0 else 1
        return (1 - similarity) * 100 # Lower similarity = higher complexity

    def _score_team_culture(self, acquirer_culture, target_culture):
        """Scores based on cultural compatibility. Lower is better."""
        if acquirer_culture == target_culture:
            return 0
        # Define some arbitrary incompatibility scores
        clashes = {('agile', 'hierarchical'): 80, ('remote-first', 'sales-driven'): 50}
        key = tuple(sorted((acquirer_culture, target_culture)))
        return clashes.get(key, 30) # Default clash score

    def _score_product_architecture(self, acquirer_arch, target_arch):
        """Scores based on architecture compatibility."""
        if acquirer_arch == target_arch:
            return 0
        if 'microservices' in [acquirer_arch, target_arch] and 'monolith' in [acquirer_arch, target_arch]:
            return 90 # High complexity to merge monolith and microservices
        return 40 # Default for other mismatches

    def calculate_score(self, acquirer, target):
        """Calculates the overall integration complexity score (0-100)."""
        acquirer_factors = acquirer.integration_factors
        target_factors = target['integration_factors']

        tech_score = self._score_tech_stack(acquirer_factors['tech_stack'], target_factors['tech_stack'])
        culture_score = self._score_team_culture(acquirer_factors['team_culture'], target_factors['team_culture'])
        arch_score = self._score_product_architecture(acquirer_factors['product_architecture'], target_factors['product_architecture'])

        weighted_score = (
            tech_score * self.weights['tech_stack'] +
            culture_score * self.weights['team_culture'] +
            arch_score * self.weights['product_architecture']
        )

        return round(weighted_score, 2)

if __name__ == '__main__':
    from tech_fusion.src.market.participants import get_sample_participants
    from tech_fusion.src.data_generator.company_generator import CompanyGenerator

    analyzer = IntegrationComplexity()
    company_gen = CompanyGenerator()
    acquirers, _, _ = get_sample_participants()

    acquirer = acquirers[0] # TechCorp
    target = company_gen.generate_company()

    score = analyzer.calculate_score(acquirer, target)

    print(f"--- Integration Complexity Analysis ---")
    print(f"Acquirer: {acquirer.name}")
    print(f"  -> Tech: {acquirer.integration_factors['tech_stack']}")
    print(f"  -> Culture: {acquirer.integration_factors['team_culture']}")

    print(f"\nTarget: {target['name']}")
    print(f"  -> Tech: {target['integration_factors']['tech_stack']}")
    print(f"  -> Culture: {target['integration_factors']['team_culture']}")

    print(f"\nIntegration Complexity Score: {score} / 100")
    if score > 60:
        print("Result: High complexity - significant integration challenges expected.")
    elif score > 30:
        print("Result: Medium complexity - integration will require effort.")
    else:
        print("Result: Low complexity - smooth integration likely.")
