import random
from tech_fusion.src.data_generator.company_generator import CompanyGenerator

# Based on the project description
SECTOR_MULTIPLIERS = {
    'AI': (20, 35), # Average 25.8x
    'Cybersecurity': (18, 30), # Average 22.3x
    'SaaS': (10, 20),
    'Infrastructure': (12, 22),
    'Marketing Tech': (8, 15),
    'Computer Vision': (10, 18),
    'Large Language Model': (30, 45),
    'Data Intelligence': (20, 28)
}

GROWTH_MULTIPLIER_ADJUSTMENT = {
    'high_growth': (1.1, 1.3), # >20%
    'medium_growth': (0.9, 1.1), # 10-20%
    'low_growth': (0.7, 0.9) # <10%
}

class Valuation:
    """Calculates the valuation of a target company."""

    def get_base_multiplier(self, sector):
        """Get the base revenue multiplier for a given sector."""
        multipliers = SECTOR_MULTIPLIERS.get(sector, (5, 12)) # Default for other sectors
        return random.uniform(*multipliers)

    def get_growth_adjustment(self, growth_rate):
        """Get the valuation adjustment factor based on growth rate."""
        if growth_rate > 0.20:
            adj_range = GROWTH_MULTIPLIER_ADJUSTMENT['high_growth']
        elif 0.10 <= growth_rate <= 0.20:
            adj_range = GROWTH_MULTIPLIER_ADJUSTMENT['medium_growth']
        else:
            adj_range = GROWTH_MULTIPLIER_ADJUSTMENT['low_growth']
        return random.uniform(*adj_range)

    def calculate_valuation(self, company, market_environment):
        """Calculates the valuation of a company based on its metrics and the market environment."""
        arr = company['financials']['arr']
        sector = company['sector']
        growth_rate = company['financials']['growth_rate']

        base_multiplier = self.get_base_multiplier(sector)
        growth_adjustment = self.get_growth_adjustment(growth_rate)

        # Talent acquisition premium for AI/ML experts
        ai_talent_premium = 0
        if company['team']['ai_ml_experts'] > 100: # Arbitrary threshold
            ai_talent_premium = random.uniform(0.1, 0.3) # 10-30% premium

        sentiment_multiplier = market_environment.get_sentiment_multiplier()

        final_multiplier = base_multiplier * growth_adjustment * sentiment_multiplier
        valuation = arr * final_multiplier
        valuation *= (1 + ai_talent_premium)

        return {
            "valuation": round(valuation, 2),
            "base_multiplier": round(base_multiplier, 2),
            "growth_adjustment": round(growth_adjustment, 2),
            "sentiment_adjustment": sentiment_multiplier,
            "ai_talent_premium": round(ai_talent_premium, 2),
            "final_multiplier": round(final_multiplier * (1 + ai_talent_premium), 2)
        }

if __name__ == '__main__':
    from tech_fusion.src.market.environment import MarketEnvironment
    company_gen = CompanyGenerator()
    valuation_engine = Valuation()
    market_env = MarketEnvironment()

    print("--- Sample Company Valuations (with Market Environment) ---")
    market_env.market_sentiment = 'bull' # Force a bull market for demonstration
    print(f"Market Sentiment: {market_env.market_sentiment.upper()}")
    
    for _ in range(2):
        company = company_gen.generate_company()
        valuation_details = valuation_engine.calculate_valuation(company, market_env)

        print(f"\nCompany: {company['name']} ({company['sector']})")
        print(f"  Valuation: ${valuation_details['valuation']:,}")
        print(f"  Details: Final Multiplier={valuation_details['final_multiplier']:.2f}x (Sentiment Adj: {valuation_details['sentiment_adjustment']:.2f}x)")
