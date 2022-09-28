import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

import math;
import random;

path = input("Enter the path: ");
dataset = pd.read_csv(path);

iterations = int(input("Enter the number of iterations: "));
variables = len(dataset.iloc[1,:]);
selected_ads = [];
total_rewards = 0;
num_of_rewards_1 = [0] * variables;
num_of_rewards_0 = [0] * variables;
for i in range(0, iterations):
  max_random = 0;
  ad = 0;
  for j in range(0, variables):
    current_random = random.betavariate(num_of_rewards_1[j] + 1, num_of_rewards_0[j] + 1);
    if (current_random > max_random):
      max_random = current_random;
      ad = j;
  selected_ads.append(ad);
  reward = dataset.values[i,ad];
  if reward == 0:
    num_of_rewards_0[ad] += 1;
  else:
    num_of_rewards_1[ad] += 1;
  total_rewards += reward;


plt.hist(selected_ads)
plt.xlabel("Ads");
plt.ylabel("Number of selections");