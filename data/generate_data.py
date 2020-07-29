# Very naive utility to simulate random chunks of survey data
import json
import itertools
import random


from constants import *


for ans in range(1005):
    with open("chunk_%04d.jsonl" % ans, "w") as ansf:
        row = {"pk": "%d" % ans}
        for carvar in carvars:
            row[carvar] = random.choice(carbrands)
        for carvar in mrcarvars:
            for carbrand in carbrands:
                row["%s.%s" % (carvar, carbrand)] = random.choice(answers)
        for singvar in singervars:
            row[singvar] = random.choice(singers)
        for singvar in mrsingervars:
            for singer in singers:
                row["%s.%s" % (singvar, singer)] = random.choice(answers)
        json.dump(row, ansf)
