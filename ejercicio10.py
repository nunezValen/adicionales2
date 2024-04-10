
def generate_player_stats(names,goals,goals_avoided,assist):
    player_stats=[]
    for i in range(len(names)):
        player={"name": names[i],"goals": goals[i],"goals_avoided": goals_avoided[i], "assist": assist[i]}
        player_stats.append(player)
    return player_stats


def find_goleador (players_stats):
    goleador=max(players_stats, key=lambda x: x['goals'])
    return goleador

'''
def most_influential(players_stats):
    puntaje_max=0
    player_most_influential=""
    for player in players_stats:
        puntaje = player["goals"]*1.5+player["goals_avoided"]*1.25+player["assist"]
        if puntaje>puntaje_max:
            puntaje_max=puntaje
            player_most_influential=player["name"]
    return player_most_influential
'''
#con lambda
def most_influential(players_stats):
    player= max(players_stats, key=lambda x: x["goals"]*1.5 + x["goals_avoided"]*1.25 + x["assist"])
    return player

def get_promedio(players_stats):
    total_goals= sum(player["goals"] for player in players_stats)
    return total_goals/25

def get_promedio_goleador(goals):
    return goals/25

names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
0]


players_stats=generate_player_stats(names.split(","),goals,goals_avoided,assists)
print(players_stats)

goleador=find_goleador(players_stats)
print(goleador)

player_most_influential=most_influential(players_stats)
print(player_most_influential["name"])

promedio=get_promedio(players_stats)
print(promedio)

promedio_goleador=get_promedio_goleador(goleador["goals"])
print(promedio_goleador)