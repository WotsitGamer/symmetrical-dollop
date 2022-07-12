```python
import requests
import json
class X0AM:
    def get_life(self):
        res = requests.get("https://life.com/api/v12/relationships/jsonresp.json").text
        self.bitches = json.loads(res)["bitches"] # more than you
        self.parents = json.loads(res)["parents"]
        self.age = json.loads(res)["age"]
        return self.bitches, self.parents, self.age
    def get_jobs(self):
        res = requests.get("https://life.com/api/v12/jobs/jsonresp.json").text
        self.jobs = [json.loads(res)["job"], json.loads(res)["partime"]]
        return self.jobs
    def socials(self):
        res = requests.get("https://life.com/api/v12/socials/jsonresp.json").text
        self.insta = json.loads(res)["instagram"]
        self.discord = json.loads(res)["discord"]
        return self.insta, self.discord

    def __init__(self):
        print(self.get_life())
        >>> 834568
        >>> s**** and g*****
        >>> 12
        print(self.get_jobs())
        >>> ["actor", "programmer"]
        print(self.socials())
        >>> @xoamified
        >>> 𝕏𝟘𝔸𝕄𝕀𝔽𝕀𝔼𝔻#9999
me = X0AM()
```
[![X0AMS GitHub stats](https://github-readme-stats.vercel.app/api?username=X0AM&theme=gruvbox)](https://github.com/X0AM/github-readme-stats)
