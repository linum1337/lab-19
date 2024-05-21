import json
import argparse
from pathlib import Path


def save_scores_to_file(scores_info, filename):
    file_path = Path.home() / filename
    with open(file_path, 'w') as file:
        json.dump(scores_info, file, indent=4)


def load_scores_from_file(filename):
    file_path = Path.home() / filename
    with open(file_path, 'r') as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(description="Team Scores CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    save_parser = subparsers.add_parser('save', help="Save team scores to a JSON file")
    save_parser.add_argument('filename', type=str, help="The filename to save the scores")

    load_parser = subparsers.add_parser('load', help="Load team scores from a JSON file")
    load_parser.add_argument('filename', type=str, help="The filename to load the scores from")

    check_parser = subparsers.add_parser('check', help="Check team positions")
    check_parser.add_argument('filename', type=str, help="The filename to load the scores from")

    args = parser.parse_args()

    if args.command == "save":
        scores_info = {
            "First Team": 100,
            "Second Team": 90,
            "Third Team": 80,
            "Fourth Team": 50,
            "Fifth Team": 30,
        }
        save_scores_to_file(scores_info, args.filename)
        print(f"Scores saved to {Path.home() / args.filename}")

    elif args.command == "load":
        try:
            scores_info = load_scores_from_file(args.filename)
            print(f"Scores loaded from {Path.home() / args.filename}: {scores_info}")
        except FileNotFoundError:
            print(f"File {Path.home() / args.filename} not found")

    elif args.command == "check":
        try:
            scores_info = load_scores_from_file(args.filename)
        except FileNotFoundError:
            print(f"File {Path.home() / args.filename} not found")
            return

        team_list = [
            input(f"{i + 1}. Enter team name (First Team, Second Team, Third Team, Fourth Team, Fifth Team): \n")
            for i in range(5)
        ]

        if position_checker(scores_info, team_list):
            print("Team positions correct!")
        else:
            print("Team positions incorrect!")


def position_checker(scores_info: dict, team_list: list) -> bool:
    sorted_teams = sorted(scores_info.keys(), key=lambda x: scores_info[x], reverse=True)
    return sorted_teams == team_list


if __name__ == '__main__':
    main()
