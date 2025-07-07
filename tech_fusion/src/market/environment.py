import random

class MarketEnvironment:
    """Models the overall economic environment."""
    def __init__(self):
        self.interest_rate = random.uniform(0.01, 0.05) # 1% to 5%
        self.market_sentiment = 'neutral' # neutral, bull, bear
        self.sentiment_multipliers = {
            'bull': 1.2,
            'neutral': 1.0,
            'bear': 0.8
        }

    def update(self):
        """Simulates a change in the market environment for the next step."""
        # Fluctuate interest rates
        self.interest_rate *= random.uniform(0.95, 1.05)
        self.interest_rate = max(0.005, min(self.interest_rate, 0.08)) # Clamp between 0.5% and 8%

        # Change market sentiment
        roll = random.random()
        if roll < 0.1:
            self.market_sentiment = 'bull'
        elif roll < 0.2:
            self.market_sentiment = 'bear'
        else:
            self.market_sentiment = 'neutral'
            
        print(f"\n[Market Update] Sentiment: {self.market_sentiment.upper()} | Interest Rate: {self.interest_rate:.2%}")

    def get_sentiment_multiplier(self):
        """Returns the valuation multiplier for the current market sentiment."""
        return self.sentiment_multipliers[self.market_sentiment]

if __name__ == '__main__':
    env = MarketEnvironment()
    print("--- Initial State ---")
    print(f"Sentiment: {env.market_sentiment}, Rate: {env.interest_rate:.2%}")
    
    print("\n--- Simulating 5 Updates ---")
    for i in range(5):
        env.update()
