# Leet Code Algo 1688 Count of Matches in Tournament

def countOfMatchesInTournament(n):
    remTeams = n
    matches = 0
    while remTeams > 1:
        if remTeams % 2 == 0:
            matches += int(remTeams / 2)
            remTeams = int(remTeams / 2)
        else:
            matches += int((remTeams - 1) / 2)
            remTeams = int(remTeams / 2) + 1
    return matches

print(countOfMatchesInTournament(7))
print(countOfMatchesInTournament(14))
      