"""Aprendendo a extrair dados da API da RIOT."""

# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

URL = {
    'base_summoner': 'https://{region}.api.riotgames.com/lol/summoner/{url}',
    'base_matchlist': 'https://{region}.api.riotgames.com/lol/match/{url}',
    'base_matchPerChamp': 'https://{region}.api.riotgames.com/lol/match/{url}',
    'base_match': 'https://{region}.api.riotgames.com/lol/match/{url}',
    'base_matchPerqueue': 'https://{region}.api.riotgames.com/lol/match/{url}',
    'base_tier': 'https://{region}.api.riotgames.com/lol/league/{url}',
    'summoner_by_name': 'v{version}/summoners/by-name/{vars}',
    'match_list': 'v{version}/matchlists/by-account/{vars}',
    'matchPerChamp': 'v{version}/matchlists/by-account/{vars}?champion={champion}',
    'matchPerqueue': 'v{version}/matchlists/by-account/{vars}?queue={queue}',
    'match_stats': 'v{version}/matches/{vars}',
    'tier': 'v{version}/entries/by-summoner/{vars}'}

API_VERSIONS = {
    'summoner': '4'
}

REGION = {
    'brazil': 'br1'
}
