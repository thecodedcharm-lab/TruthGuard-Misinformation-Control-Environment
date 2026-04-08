import random
from misinfo_env import MisinfoEnv
from grader import grade_easy, grade_medium, grade_hard

def run_task(posts, grader):

    env = MisinfoEnv(posts)
    state = env.reset()

    done = False
    handled = 0

    while not done:

        action = random.randint(0,3)
        state, reward, done = env.step(action)

        if reward > 0:
            handled += 1

        print("STATE:", state)
        print("REWARD:", reward)

    score = grader(handled)
    print("Final Score:", score)

def main():

    print("Running Easy Task")
    run_task(5, grade_easy)

    print("Running Medium Task")
    run_task(10, grade_medium)

    print("Running Hard Task")
    run_task(20, grade_hard)

if __name__ == "__main__":
    main()
