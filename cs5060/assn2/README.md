# How to run
```Python
    python3 explore_exploit.py
    python3 explore_exploit_thomson.py
```
# How to configure
Both explroe_exploit and thomson have paramaters that the user can set at the top of each file. 
The most important ones are:
1. drift: True run sim with drift, False run sim with out drift.
2. reset: This is a Thomson only, and it resets the Thomsons distrobution at time step 3000 if True. If False it does not. 

# Questions Anwsers:
Question 1: An espilon of 0.4 generally converges to the true avg of each machine faster, but explores a lot more so we end up lossing more money. Espilon 0.01 dosent explore enough to find useful information to exploite. Where as an espilon of 0.05, finds the correct machine relatively fast, but exploites it a lot more so we make money.Therefore espilon 0.05 converges the fastes. 

Question 2: Thomson sampling genral has better results. It is much more stable than greedy espilson. It does a much better job of balancing the explore exploit. As time goes on it almost always choose the machine with the best distrobution.

Question 3: In the case of a changing feild, greedy epsilon becomes much more intresting. It adpts to the feild a lot faster. Where as Thomson still belives the feild is how it was. This is a good example of why it is important to always maintian some degree of exploration. Why the feild change both algrothims had no idea, but by randomly choosing each time, it allows algrothims to map the new feild. 

Question 4: If we reset Thomson sampling at time 3000, it alwos for Thomson sampling to rediscover the feild. Basically we decided the past was no longer an accurate predictor of the futer, so we had to relearn the feild. This methood does allow for Thomson sampling to conver faster to the new feild, but incresses the over all convergance time. However this is desirable, because why would we want to converge to an old feild. 
