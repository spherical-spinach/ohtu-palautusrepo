from rich import print
from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    while True:
        print("NHL statistics by nationality")

        selected_season = input("Select season (or type 'exit') [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/]:")
        if selected_season == "exit":
            return
        print(f"you selected {selected_season}")

        url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season}/players"

        selected_nationality = input("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/]:")
        print(f"you selected {selected_nationality}")

        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(selected_nationality)

        print(f"Top scorers of {selected_nationality} season {selected_season}")

        table = Table()
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")

        for player in players:
            player_points = player.goals + player.assists
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player_points))

        console = Console()
        console.print(table)

if __name__ == "__main__":
    main()
