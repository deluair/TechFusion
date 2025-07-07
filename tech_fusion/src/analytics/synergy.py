import random

class Synergy:
    """Calculates the synergy between an acquirer and a target."""

    def calculate_synergy(self, acquirer, target):
        """
        Calculates a synergy score and potential premium based on strategic fit.

        Returns:
            dict: A dictionary containing the synergy score (0-1) and the premium (0-1).
        """
        if acquirer.type != 'Strategic':
            return {'score': 0, 'premium': 0}

        needs = set(acquirer.strategic_needs)
        assets = set(target['technology']['assets'])
        
        matches = needs.intersection(assets)
        
        if not matches:
            return {'score': 0, 'premium': 0}

        # Score is based on how many of the acquirer's needs are met
        score = len(matches) / len(needs)
        
        # Premium is a function of the synergy score
        # A perfect score might justify up to a 40% premium
        premium = score * random.uniform(0.2, 0.4)
        
        return {
            'score': round(score, 2),
            'premium': round(premium, 2),
            'matched_assets': list(matches)
        }
