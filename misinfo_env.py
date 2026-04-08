import random

class MisinfoEnv:

    def __init__(self, posts=5):
        self.initial_posts = posts
        self.reset()

    def reset(self):
        self.suspicious_posts = self.initial_posts
        self.viral_spread = random.uniform(0.2,0.6)
        self.user_trust = 0.8
        self.moderation_budget = 10
        self.fact_checkers = 3
        return self.state()

    def state(self):
        return {
            "suspicious_posts": self.suspicious_posts,
            "viral_spread": round(self.viral_spread,2),
            "user_trust": round(self.user_trust,2),
            "moderation_budget": self.moderation_budget,
            "fact_checkers": self.fact_checkers
        }

    def step(self, action):

        reward = 0
        done = False

        if self.suspicious_posts <= 0:
            done = True
            return self.state(), reward, done

        if action == 0:  # ignore
            self.viral_spread += 0.1
            reward = -1

        elif action == 1:  # flag
            self.suspicious_posts -= 1
            self.moderation_budget -= 1
            reward = 1

        elif action == 2:  # fact check
            if self.fact_checkers > 0:
                self.suspicious_posts -= 1
                self.fact_checkers -= 1
                reward = 1.5

        elif action == 3:  # reduce reach
            self.viral_spread -= 0.1
            reward = 0.5

        if self.viral_spread > 1:
            reward -= 1

        if self.suspicious_posts <= 0:
            done = True
            reward += 2

        return self.state(), reward, done
