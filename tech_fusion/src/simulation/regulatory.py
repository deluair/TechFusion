import random

class RegulatoryEngine:
    """Simulates the regulatory review process for M&A deals."""

    def __init__(self, block_probability=0.15, review_threshold=5_000_000_000):
        """
        Initializes the regulatory engine.

        Args:
            block_probability (float): The base probability that a reviewed deal is blocked.
            review_threshold (int): The deal value threshold that triggers a regulatory review.
        """
        self.block_probability = block_probability
        self.review_threshold = review_threshold
        # Certain sectors might attract more scrutiny
        self.sensitive_sectors = ['AI', 'Infrastructure', 'Cybersecurity']

    def review_deal(self, deal):
        """
        Reviews a deal and determines its outcome (Approved or Blocked).

        Args:
            deal (Deal): The deal object to be reviewed.

        Returns:
            tuple: A tuple containing the status (str) and a reason (str).
        """
        is_sensitive = deal.target['sector'] in self.sensitive_sectors
        is_large = deal.final_price > self.review_threshold

        # Only large deals in sensitive sectors trigger a review
        if not (is_large and is_sensitive):
            return "Approved", "Deal did not meet criteria for regulatory review."

        print(f"   REGULATORY REVIEW for {deal.target['name']} (Value: ${deal.final_price:,.2f})")

        # Simulate the review outcome
        if random.random() < self.block_probability:
            reason = f"Blocked due to concerns over market concentration in the {deal.target['sector']} sector."
            return "Blocked", reason
        else:
            reason = "Approved after regulatory review."
            return "Approved", reason
