# python-challenge
Module 3 homework

The main.py in PyBank will open budget_data.csv and run a FOR loop. The FOR loop first adds up the total Profits/Losses and counts the total number of entries.

In the IF statement it makes sure not to subtract the first row from nothing. If it's the first row then it just sets the variable pre_row equal to the current value and then moves on to the next iteration through the loop. Otherwise, as it runs through the loop it subtracts the previous row's value from the current row, then stores that difference in the "changes" list. It also searches for and stores the maximum and minimum changes.




For PyPoll it first adds 1 to the total_votes count, then checks if the current candidate is already in the candidate_counts dictionary. If it is it adds one to the candidate count. If it's not it creates that candidate and sets it to 1. The smaller FOR loop at the bottom goes through each candidate in candidate_counts and calculates the percentage, then creates the string needed for each candidate "Candidate: percentage% (number of votes)". To figure out the winner I'm using the max function with lambda key x to check what the max value of the candidate's count value instead of the max of the candidate key.


For both files the results are save in their corresponding analysis folder as results.txt