import madlibs, seventeen_members, zombie
import random

if __name__ == "__main__":
    m = random.choice([madlibs, seventeen_members, zombie])
    m.madlib()