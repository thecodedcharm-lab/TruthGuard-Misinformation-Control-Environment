TruthGuard: Misinformation Control Environment

TruthGuard is an AI environment that simulates how online platforms control the spread of misinformation.

The environment models the decision-making process used by content moderation systems to detect and reduce fake news while maintaining user trust.

This project was created for the Scaler OpenEnv Hackathon.

---

Problem

Online platforms constantly face the challenge of stopping misinformation without harming legitimate content.

Moderation systems must balance:

- reducing misinformation spread
- maintaining user trust
- managing limited moderation resources

TruthGuard simulates this problem so AI agents can learn moderation strategies.

---

Environment Overview

The agent acts as a moderation system on a social platform.

It observes the current state of the platform and decides how to respond to suspicious posts.

Possible strategies include ignoring posts, flagging them, sending them for fact checking, or reducing their reach.

The goal is to minimize misinformation spread while preserving user trust.

---

State Space

Each environment state includes:

- suspicious_posts
- viral_spread
- user_trust
- moderation_budget
- fact_checkers

Example state:

{
"suspicious_posts": 6,
"viral_spread": 0.45,
"user_trust": 0.8,
"moderation_budget": 10,
"fact_checkers": 3
}

---

Action Space

The agent can perform the following actions:

0 → Ignore post
1 → Flag post
2 → Send for fact check
3 → Reduce post reach

---

Reward Function

The reward encourages accurate moderation.

Event| Reward
Correct moderation| +1
Fact-check success| +1.5
Reducing viral spread| +0.5
False moderation| -0.5
Viral misinformation| -1

---

Tasks

The environment includes three tasks.

Easy
Moderate 5 suspicious posts.

Medium
Moderate 10 suspicious posts.

Hard
Moderate 20 suspicious posts with limited moderation resources.

---

Project Structure

truthguard-openenv/

misinfo_env.py
grader.py
inference.py
openenv.yaml
requirements.txt
README.md

---

Running the Environment

Install dependencies:

pip install -r requirements.txt

Run the inference script:

python inference.py

---

Use Cases

This environment can help explore AI strategies for:

- content moderation
- misinformation detection
- platform governance

---

License

MIT License
