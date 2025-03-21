## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[Answer here]
I assume the missing values or "NO DATA" in the dataset are due to the device failing to record the heart rate at that time. The causes of this could be a malfunction of the device or the device falling off. The risk of filtering these values includes making the dataset incomplete or invalid, which may result in a possibly false or unreliable outcome.
## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

[Answer here]
Phase 0 is when sleep occurs. This can be shown by the line chart of Phase 0, where, from left to right, the heart rate gradually lowers. Additionally, compared to other phases, Phase 0 has the lowest maximum heart rate, which is 93, while the others are 110, 117, and 99.


## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[Answer here]
Phase 2 is when the exercise occurred. Phase 2 has the highest maximum heart rate of 117, compared to the other phases, which have maximum heart rates of 93, 110, and 99.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[Answer here]
Phase 3 is when awake activity occurs, matching both features of a relatively lower average heart rate and a higher standard deviation. It has an average heart rate of 60.65, which is the lowest among 64.59, 87.3, and 85.18. For standard deviation, phase 3 has the highest among all other phases except for Phase 2.