Problem Description
This project is to implement the stable matching algorithm to match online
advertisements with viewers. First, I decided on a ranking algorithm to rank viewers
and advertisements based on their preferences and viewers choices respectively.
Then I input the ranking outcomes into the stable matching algorithm to match
advertisements with viewers.
Required Task Elements
To rank the viewers for a particular advertisement, the attributes of viewers are: age,
daily internet usage, gender and income. The conditions applied to rank the viewers
are: if the age is between 25 to 40, score +1; if target daily internet usage is between
3 to 4, score +1; if target gender matches viewer’s gender, score +1; if target income
is between 40,000 to 75,000, score + 1. Based on the scores of each user, I get the
rankings for each advertisement. This algorithm measures how well the viewers
match the advertiser’s need.
To rank the advertisement preference of one viewer, the attributes of advertisement
are: target age, target travel, target gender, target car and target kid. The conditions
applied to rank the advertisements are: target age between 3 to 13, score + 1; targe
travel matches viewer’s travel, score + 1; targe gender matches viewer’s gender,
score +1; target car matches viewer’s car, score +1; target kid > = 2, score +1. Based
on the scores of each advertisement, I get the rankings for each reviewer. This
algorithm measures how well the advertisement matches the viewer’s preference.
The outputs of advertisement and viewer preferences are then used to match the
advertisements with viewers. I apply the stable matching algorithm. The goal of this
algorithm is to find a stable match between viewers and advertisements where no
two elements from these 2 sets prefer each other over their current match. To
initialize the matching process, all viewers and advertisements are initially free. The
matching process continues if there is an unmatched advertisement. Inside the loop,
the picked advertisement matches to viewers according to its preference list. If the
viewer is free, they are matched, and the advertisement is marked as not free. If the
viewer is not free, then the viewer’s preferences are checked. If the viewer prefers
the new advertisement over their current match, then the viewer breaks the current
match and matches to the new advertisement. The newly free advertisement
becomes free again. In the termination stage matching algorithm, all advertisement
are matched with viewers. We cannot find a viewer and an advertisement are not
matched to each other but prefer each other over their current match.
Pros and Cons
Both ranking algorithm of advertisement and viewers allows for a customized
approached to rank the objects based on their compatibility. It uses multiple criteria
(age, daily internet usage, gender, income, target age, target gender, target travel,
target card, target kid) to determine the objects’ compatibility. Both ranking is based
on a predefined scoring system, which may not accurately reflect the preference of
each viewer or the effectiveness of the advertisement on the viewer. It assumes
equal weight for all criteria, which may not be the case.
The stable matching algorithm guarantees that no viewer and advertisement who
would both rather be paired with each other than their current match. It is efficient
in terms of running time is reasonable even for large inputs. The result can be
different depending on who initialize the match first (viewer or advertisement). It
assumes that the preferences have no ties and all that matters is whether one
candidate is preferred to another, which may not the case in real world scenarios.
Modification and Improvement
I implement a machine learning model to predict whether an advertisement will be
clicked based on certain features. The “Clicked on Ad” column is assigned to variable
y, which is the target variable that the model predicts.
‘Daily Time Spent on Site’
,
‘Age’
,
‘Area Income’
,
‘Male’ (1 is male and 0 is female) are assigned to variable x.
These are the features that the model will use to make predictions. The data set is
attached at a separate CSV file Advertising.
Next the features and target variables are split into training and test sets. 20% of the
data is used for the test set and the rest is used for training set. The mean accuracy
of the model on the test set is 0.86 which means the model is correct 86% of the
time on the test data.
Why choose a Logistic Regression model? A Logistic Regression model is used and
trained using the training data (the target variable “Clicked on Ad” has binary
outcomes). The features like ‘Daily Time Spent on Site’, ‘Age’, ‘Area Income’, and
‘Daily Internet Usage’ have predictive power in determining whether a user will click
on an ad or not. The coefficients of the model represent the log odds of the
outcome. For example, a positive coefficient for ‘Daily Time Spent on Site’ means
that spending more time on the site is associated with higher odds of clicking on the
advertisement.
Reflection
The stable matching algorithm matches viewers and advertisement based on their
preferences, while the Logistic Regression model predicts whether a viewer will click
on an advertisement. The stable matching algorithm is applied in school admissions,
organ transplants and job market. The Logistic Regression Model is applied in
prediction problems such as healthcare (a patient having a disease), marketing,
finance (loan defaults). We should choose different algorithm and models based on
the problem we want to solve.
A reflection on my work this semester: I have practiced using flowchart to plan my
algorithm before starting to code. The projects include: generating random numbers
and matching them with user’s choice; guessing a number using the binary search
algorithm; guessing a word by manipulating lists; creating class and its objects and
methods to solve the ice cream carton problem; simulating the lottery play and
rewards distribution to analyze the wealth disparity problem; using recursion to
calculate Haruo Hosoya triangle’s number; and using stacks and queues to develop
bracket checking and ticket line applications.
Acknowledgements
Stable marriage problem: https://en.wikipedia.org/wiki/Stable_marriage_problem
https://www.geeksforgeeks.org/stable-marriage-problem/
Customer ad clicks prediction mode: https://www.youtube.com/watch?v=6NAmF-
rzf8k
Advertising data:
https://drive.google.com/file/d/1h9RDODHxETGcdLVRC96_PUSN88dK3MvA/view
