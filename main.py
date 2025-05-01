
from source.logic import get_arbitrage_opportunities
import os
import argparse
from dotenv import load_dotenv
from rich import print
from source.logic import get_arbitrage_opportunities, compute_arbitrage_stakes



def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="Arbitrage Finder",
        description=__doc__
    )
    parser.add_argument(
        "-k", "--key",
        default=os.environ.get("f5d7b976a9cc1252a51661d07543cc54"),
        help="The API key from The Odds API. If left blank it will default to the value of $API_KEY."
    )
    parser.add_argument(
        "-r", "--region",
        choices=["eu", "us", "au", "uk"],
        default="eu",
        help="The region in which to look for arbitrage opportunities."
    )
    parser.add_argument(
        "-u", "--unformatted",
        action="store_true",
        help="If set, turn output into the json dump from the opportunities."
    )
    parser.add_argument(
        "-c", "--cutoff",
        type=float,
        default=0,
        help="The minimum profit margin required for an arb to be displayed. Inputted as a percentage."
    )
    parser.add_argument(
    "-b", "--budget",
    type=float,
    default=100,
    help="Total amount of money to allocate per arbitrage opportunity."
)

    args = parser.parse_args()

    cutoff = args.cutoff/100

    arbitrage_opportunities = get_arbitrage_opportunities(key="f5d7b976a9cc1252a51661d07543cc54", region=args.region, cutoff=cutoff)

    arbitrage_opportunities = list(arbitrage_opportunities)
    print(f"{len(arbitrage_opportunities)} arbitrage opportunities found {':money-mouth_face:' if len(arbitrage_opportunities) > 0 else ':man_shrugging:'}")

    for arb in arbitrage_opportunities:
        print(f"\n\t[italic]{arb['match_name']} in {arb['league']}[/italic]")
        print(f"\t\tTotal implied odds: {arb['total_implied_odds']:.5f} with these odds:")

        for outcome, (bookmaker, odd) in arb["best_outcome_odds"].items():
            print(f"\t\t[bold red]{outcome}[/bold red] with [green]{bookmaker}[/green] for {odd}")

        stake_info = compute_arbitrage_stakes(arb["best_outcome_odds"], args.budget)
        print(f"\n\t[bold]Suggested stake breakdown for ${args.budget}:[/bold]")
        for outcome, stake in stake_info["stakes"].items():
            print(f"\t\tBet ${stake} on [cyan]{outcome}[/cyan]")

        print(f"\tPayout: ${stake_info['payout']}, Profit: [bold green]${stake_info['profit']}[/bold green]")



if __name__ == '__main__':
    main()