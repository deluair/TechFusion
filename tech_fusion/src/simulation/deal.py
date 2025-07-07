import random

from tech_fusion.src.analytics.synergy import Synergy

class Deal:
    """Represents an M&A transaction."""
    def __init__(self, acquirer, target):
        self.acquirer = acquirer
        self.target = target
        self.base_valuation = target['valuation_details']['valuation']
        self.synergy_details = Synergy().calculate_synergy(acquirer, target)
        self.structure = self._determine_deal_structure()
        self.status = "proposed"  # proposed, accepted, failed, closed
        self.negotiated_premium = self._negotiate_premium()
        self.synergy_premium = self.synergy_details['premium']
        self.final_price = self.base_valuation * (1 + self.negotiated_premium + self.synergy_premium)

    def _determine_deal_structure(self):
        """Determines the deal structure (cash, stock, hybrid)."""
        roll = random.random()
        if roll < 0.5:
            return "All-Cash"
        elif roll < 0.8:
            return "All-Stock"
        else:
            return "Hybrid"

    def _negotiate_premium(self):
        """Simulates a negotiation to determine the final premium."""
        # Financial buyers might offer lower premiums, strategics might offer higher
        if self.acquirer.type == 'Financial':
            return random.uniform(0.10, 0.25)
        else: # Strategic
            return random.uniform(0.15, 0.30)

    def __repr__(self):
        return (f"Deal({self.acquirer.name} -> {self.target['name']}, "
                f"Price: ${self.final_price:,.2f}, Status: {self.status})")
