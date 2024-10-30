import requests
from urllib.parse import urlencode
import base64
import webbrowser

CLIENT_ID = 'e20c25956b1e48228ddc9309f3e4d6b2'
CLIENT_SECRET = '27b5ee6d34d146e4b62ca13c9be25d42'
AUTOHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize'
REDIRECT_URL= "https://www.google.co.in/"
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private user-read-playback-state user-modify-playback-state"

auth_headers = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URL,
    "scope": SCOPE
}

#webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code = 'AQAr5bMgUOWTP7ccNRZg_KTrML5oxemFb0pop403fulTkIq1DsTKnq-mmWPC8WIKiE2YNeEp4wruJ0z5pmQIgHaI2uf3R3ADxb3joW9zTgvTIA6Vr0CeVhrNVS41904dBcc8MD3ZR3Zn0fFmgJYRpZsC7kf4PZYnm6SYDgFof3zyUefuInF2EC2f3KJbqzPmNi8YbYH_VD_OCFQr3ks48gFoQzJhb8El9f5AM_nT6mhHtw5qqeHLshDoWPwwNy73xDKfpno2Kswu-2qF9F_4INV2r4WtSLBWWdi6TYLVaz2Salo-svLj1SUjyzyi3_dBMVG09Dh-EJLD5IJ_YrHIUQlSCrTK37PxXfHLyP36XI9cXIWHBwE1JmdOie9zrux4CuakrsfgpBpCt1V3jcKqc2A5Nuh0-zkfGwKbrPzLHYsnmJ4bES_yYvPcq9B5sMKTRX5W3x5p86AsYuCcKypidgwEI-yo1P9-igsPcISexg3l_XfaYr37MxLeluRdc3JzTzk8RmEbIsPKezHm6I3nvhiQmTaTioExhz60CnFako93npw91rj2zqM'
encoded_credentials = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URL
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)
ACCESS_TOKEN = 'BQBW1HFdLeN0-R359DDmNBWh0gmEuuDkNYk5Qm1u20Vd6AQGNo9kSRVaeU48b8D3Ht0VYjxJkCpqHBe2Hy2p6jpDhoXMt7kPUfZLJoe6E_PTGl27IOYIY4qQSw9arZEXhQrHmxmBtEMECJ8hEaYWvNGQ41ANh1EMHFs0Bd6MB8Fl_599Wb71_jVjlSVRHYpSeTKiPd62dPTloh72wS8BtGB1f60xpRJw0rImJK1MfPsX5ShbR44thGgnWhppuhsBc39wcJT9pkgS_gyToBROMcH92JscXvEjLMlSV6amz4b_jfMgIHxv5n4zn6AGF6R3BID5'
print(ACCESS_TOKEN)


user_headers = {
    "Authorization": "Bearer " + ACCESS_TOKEN,
    "Content-Type": "application/json"
}

track_status = requests.get('https://api.spotify.com/v1/me/player', params={
    "market":"IN",
    "additional_types":"track",
}, headers=user_headers)

play_track = requests.put('https://api.spotify.com/v1/me/player/play', headers=user_headers)
next_track = requests.post("https://api.spotify.com/v1/me/player/next", headers=user_headers)

print(play_track.json())