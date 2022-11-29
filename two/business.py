import json
import random

class DomainTwo:

    def do(self):
        value = random.randint(0,100)
        return json.dumps({'data': value})

