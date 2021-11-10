#Mustafa Eski
#ID: 2046388
#Reference: https://stackoverflow.com/questions/69474410/winning-team-classes
class Team:
    def __init__(team):
        team.team_name = "None"
        team.team_losses = 0
        team.team_wins = 0


    def get_win_percentage(team):
        return team.team_wins / (team.team_wins + team.team_losses)


if __name__ == "__main__":
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_losses = team_losses
    team.team_wins = team_wins


    if team.get_win_percentage() <= 0.5:
        print('Team', team.team_name, 'has a losing average.')
    else:
        print('Congratulations, Team', team.team_name, 'has a winning average!')

