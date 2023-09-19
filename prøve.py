# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:57:25 2023

@author: Evenf
"""

# Task 1: Leser tekstfilen

# Task 2: Laster opp filen og leser av filen i tabell
import csv
import matplotlib.pyplot as plt

# Create a dictionary to store the total votes for each party
party_votes = {}

# Open the CSV file and read its contents
with open("C:/Users/Evenf/OneDrive - Norwegian University of Life Sciences/Geomatikk 3. år/Inf201/Øving 2/2021-09-14_party distribution_1_st_2021.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        try:
            district = row[0]  # Use the index for the district
            party = row[6]     # Use the index for the party
            votes = int(row[12])  # Use the index for the total votes

            # Update the total votes for the party
            if party in party_votes:
                party_votes[party] += votes
            else:
                party_votes[party] = votes
        except IndexError:
            # Handle rows with insufficient columns (if any)
            pass

# Print the party votes as a table
for party, votes in party_votes.items():
    print(f"Party: {party}, Total Votes: {votes}")


# Sort the party_votes dictionary by total votes in descending order
sorted_party_votes = sorted(party_votes.items(), key=lambda x: x[1], reverse=True)

# Create lists for party names and total votes in the sorted order
parties = [party for party, _ in sorted_party_votes]
total_votes = [votes for _, votes in sorted_party_votes]

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.barh(parties, total_votes, color='skyblue')  # Horizontal bar chart
plt.xlabel('Total Votes')
plt.ylabel('Party')
plt.title('Total Votes by Party')
plt.gca().invert_yaxis()  # Invert the y-axis to start with the most votes at the top
plt.tight_layout()

# Display the chart
plt.show()
