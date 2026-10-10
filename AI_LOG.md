# AI Usage Log

Replace this template with your own entries. Add one entry per significant use of an AI tool.

## 1. <Asked AI to help write me the inference script to be runned on folder of images>

**What I asked:**
'Help me write an inference script in accordance with these guidelines {pasted Part1: Core Task number 4}

**What I kept vs. rewrote, and why:**

I had to alter the confidence threshold best optimized for my data. After analyzing the models evaluation visualizations I decided to make the confidence threshold set to the maximum F1 score threshold of .47 in the visualization graph. I chose to use the best metric from the F-1 scores because it tests both precision and recall, which are both crucial in enviroments/challenges where missing or misidentifying an object is detrimental in a competition (like URC). Also had to change typical placeholder names to specific folders//files used for this project.

**What the AI got wrong that I had to catch:**

The AI used placeholer names and values such as a confidence theshold of .25 which if kept would lower the overall performance of the model.

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**

Verified the script by ensuring output matched the 0-1 values for coordinates and class ids as the dataset labels do.

## 2. <next use>

**What I asked:**

**What I kept vs. rewrote, and why:**

**What the AI got wrong that I had to catch:**

**How I verified it (for example, checked the metric by hand, ran it on data it hadn't seen):**
