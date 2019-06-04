# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
women_degrees = pd.read_csv(
    'Projects\Project4_Visualizing_Earnings_of_Majors\gender-earnings-by-major.csv')
plt.plot(women_degrees["Year"], women_degrees["Biology"])
plt.xlabel("Year")
plt.ylabel("Biology Degree")

# %%
plt.plot(women_degrees['Year'],
         women_degrees['Biology'], c='blue', label='Women')
plt.plot(women_degrees['Year'], 100 -
         women_degrees['Biology'], c='green', label='Men')
plt.legend(loc='upper right')
plt.title('Percentage of Biology Degrees Awarded By Gender')


# %%
# plot the line chart using ax(subplot) in a figure
fig, ax = plt.subplots()
ax.plot(women_degrees['Year'],
        women_degrees['Biology'], c='blue', label='Women')
ax.plot(women_degrees['Year'], 100 -
        women_degrees['Biology'], c='green', label='Men')
# removes the tick marks in the graph
ax.tick_params(bottom="off", top="off", left="off", right="off")
# removes all borders from the graph
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')


# %% [markdown]
# Creating multiple subplots for two line chart

# %%
major_cats = ['Biology', 'Computer Science',
              'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0, 4):
    ax = fig.add_subplot(2, 2, sp+1)
    ax.plot(women_degrees['Year'],
            women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100 -
            women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    # removes the tick marks in the graph
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    # removes all borders from the graph
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_title(major_cats[sp])

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')


# %% [markdown]

# # Conclusion
# It seems like that the gender gap in Computer Science and Engineering have big gender gaps while the gap in Biology/Math&Statistics is quite small. It seems like CS and Engineering is dominated by men.
