import RiotConsts as consts
import requests


class GetSummoner(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_summoner'].format(
                region=self.region,
                url=api_url,
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_summoner_by_name(self, var):
        api_url = consts.URL['summoner_by_name'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var
        )
        return self._request(api_url)


class Getmatchlist(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_matchlist'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_summoner_account(self, var):
        api_url = consts.URL['match_list'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var
        )
        return self._request(api_url)


class GetmatchStats(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_match'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_match_stats(self, var):
        api_url = consts.URL['match_stats'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var
        )
        return self._request(api_url)


class GetmatchPerChamp(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_matchPerChamp'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_summoner_accountPerChamp(self, var, champ):
        api_url = consts.URL['matchPerChamp'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var,
            champion=champ
        )
        return self._request(api_url)

class GetmatchPerqueue(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_matchPerqueue'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_summoner_accountPerqueue(self, var, queue):
        api_url = consts.URL['matchPerqueue'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var,
            queue=queue
        )
        return self._request(api_url)

class GetTierbysummoner(object):

    def __init__(self, api_key, region=consts.REGION['brazil']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            consts.URL['base_tier'].format(
                region=self.region,
                url=api_url
                ),
            params=args
            )
        # print(response.url)
        return response.json()

    def get_summonerTier_by_id(self, var):
        api_url = consts.URL['tier'].format(
            version=consts.API_VERSIONS['summoner'],
            vars=var
        )
        return self._request(api_url)
