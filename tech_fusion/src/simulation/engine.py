import random
from tech_fusion.src.data_generator.company_generator import CompanyGenerator
from tech_fusion.src.market.participants import get_sample_participants
from tech_fusion.src.market.valuation import Valuation
from tech_fusion.src.simulation.deal import Deal
from tech_fusion.src.market.environment import MarketEnvironment
from tech_fusion.src.analytics.integration import IntegrationComplexity
from tech_fusion.src.simulation.regulatory import RegulatoryEngine
from tech_fusion.src.reporting.report_generator import ReportGenerator

class SimulationEngine:
    """Manages the M&A simulation process."""

    def __init__(self, num_companies=100):
        self.company_gen = CompanyGenerator()
        self.valuation_engine = Valuation()
        self.market_env = MarketEnvironment()
        self.integration_analyzer = IntegrationComplexity()
        self.regulatory_engine = RegulatoryEngine()
        self.report_generator = ReportGenerator(report_dir='tech_fusion/reports')
        self.completed_deals = []

        print("Initializing simulation environment...")
        self.target_companies = self.company_gen.generate_companies(num_companies)
        self.strategic_acquirers, self.financial_buyers, self.advisors = get_sample_participants()
        self.acquirers = self.strategic_acquirers + self.financial_buyers
        
        # Pre-calculate valuations for all target companies
        self.update_all_valuations()

        print(f"Generated {len(self.target_companies)} target companies.")
        print(f"Generated {len(self.acquirers)} potential acquirers.")

    def find_potential_target(self, acquirer):
        """Finds a potential target company for an acquirer."""
        potential_targets = []
        for company in self.target_companies:
            # Simple matching based on sector focus
            if any(focus in company['sector'] for focus in acquirer.investment_focus) or "High-Growth Tech" in acquirer.investment_focus:
                potential_targets.append(company)
        
        if not potential_targets:
            return None
        
        # Acquirer chooses one target randomly from potential matches
        return random.choice(potential_targets)

    def update_all_valuations(self):
        """Recalculates valuations for all companies based on the current market environment."""
        for company in self.target_companies:
            company['valuation_details'] = self.valuation_engine.calculate_valuation(company, self.market_env)

    def run_simulation_step(self):
        """Runs a single step of the simulation."""
        print("\n--- Running Simulation Step ---")
        
        for acquirer in self.acquirers:
            if not self.target_companies:
                break
            
            target = self.find_potential_target(acquirer)
            
            if target:
                print(f"-> {acquirer.name} ({acquirer.type}) is evaluating {target['name']} ({target['sector']}).")
                
                propose_deal = False
                pass_reason = ""

                # Financial buyers are more sensitive to interest rates
                if acquirer.type == "Financial":
                    if target['financials']['ebitda_margin'] > 0 and self.market_env.interest_rate < 0.04:
                        propose_deal = True
                    else:
                        pass_reason = "Target does not meet financial criteria"

                elif acquirer.type == "Strategic":
                    integration_score = self.integration_analyzer.calculate_score(acquirer, target)
                    print(f"   Integration Complexity Score: {integration_score:.2f}")
                    if integration_score < 65: # Threshold for acceptable complexity
                        propose_deal = True
                    else:
                        pass_reason = f"Integration complexity ({integration_score:.2f}) is too high"

                if propose_deal:
                    deal = Deal(acquirer, target)
                    # Regulatory review
                    status, reason = self.regulatory_engine.review_deal(deal)

                    if status == "Approved":
                        print(f"   DEAL CLOSED: {acquirer.name} acquired {target['name']}.")
                        print(f"   Price: ${deal.final_price:,.2f} ({deal.structure})")
                        if deal.synergy_details['score'] > 0:
                            print(f"   Synergy Premium: +{deal.synergy_details['premium']:.2%} (Assets: {deal.synergy_details['matched_assets']})")
                        self.completed_deals.append(deal)
                        self.target_companies.remove(target)
                    else: # Blocked by regulators
                        print(f"   DEAL BLOCKED: Acquisition of {target['name']} by {acquirer.name}. Reason: {reason}")
                else:
                    if pass_reason:
                        print(f"   Decision: Passed on {target['name']} ({pass_reason}).")
                    else:
                        print(f"   Decision: Passed on {target['name']}.")
            else:
                print(f"-> {acquirer.name} found no suitable targets in this step.")

    def run_full_simulation(self, num_steps=5):
        """Runs the full simulation for a number of steps."""
        print(f"\n=== Starting Full M&A Simulation ({num_steps} steps) ===")
        for i in range(num_steps):
            if not self.target_companies:
                print("\nNo more target companies available. Ending simulation.")
                break
            
            self.market_env.update()
            self.update_all_valuations()
            self.run_simulation_step()
            
            print(f"--- End of Step {i+1} ---")
            print(f"Remaining target companies: {len(self.target_companies)}")
        print("\n=== Simulation Finished ===")
        self.summarize_deals()
        self.report_generator.generate_deals_report(self.completed_deals)
    
    def summarize_deals(self):
        """Prints a summary of all completed deals."""
        print("\n--- Completed Deals Summary ---")
        if not self.completed_deals:
            print("No deals were completed in this simulation.")
            return
            
        for deal in self.completed_deals:
            print(f"- Acquirer: {deal.acquirer.name}")
            print(f"  Target: {deal.target['name']} ({deal.target['sector']})")
            print(f"  Price: ${deal.final_price:,.2f}")
            print(f"  Structure: {deal.structure}")
        print(f"\nTotal deals completed: {len(self.completed_deals)}")

if __name__ == '__main__':
    simulation = SimulationEngine(num_companies=50)
    simulation.run_full_simulation(num_steps=3)

