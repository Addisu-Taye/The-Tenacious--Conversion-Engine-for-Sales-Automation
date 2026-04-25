## τ²-Bench Baseline

Configuration:
- Domain: retail
- Trials: 2
- Tasks: 5
- Model: gpt-4o-mini

Results:
- Success Rate: 0.20
- Average Reward: 0.20
- Confidence Interval (95%): [0.08, 0.32]
- Avg Cost per Conversation: $0.0099

Observations:
- Agent handles simple tasks but struggles with multi-step reasoning.
- Read actions moderately accurate (63.8%).
- Write actions low accuracy (20%).
- DB matching limited (22.2%).

Engineering Note:
Initial runs using GPT-4.1 failed due to rate limiting. Evaluation was recalibrated using gpt-4o-mini for stable and reproducible results.