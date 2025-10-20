# Technical Assessment for BSCI SRSE Summer 2025
A technical assessment for SRSE candidates for the Behavioural Science group at WBS, focussing on fixing an oTree experiment.

Instructions for the assessment are as follows.

# The Task
The assessment comprises two parts:
  - Making changes to a codebase to address the issues described in the [Scenario](#scenario) section of this readme.
  - A written response to a [follow up question](#follow-up-question).

Your responses to this task are to be committed to this repository as detailed in the [Submission
Details](#submission-details) section of this readme.

## Scenario 
An early career researcher has requested your assistance in fixing an experiment that they have written in python and HTML
using the oTree experimental framework. They have provided you the code, along with an e-mail detailing what parts of it
aren’t working as intended.

### The e-mail from the Researcher
> Hi, 
>
> I’m having some trouble with my oTree experiment. I’m trying to make a repeated public goods game to run in the
> Behavioural Science Laboratory at WBS that shows a leaderboard of contributions each round, where participants are
> “stranger matched” (i.e. they interact with people that they haven’t interacted with before). I want sessions of 21 people to
> do 5 rounds each, where each round they’re matched into groups of 3. 
>
> At the moment I’m having problems with the following aspects:
> -	The leaderboard doesn’t display in order
> -	The leaderboard shows different things for different people, and often says “None” for contribution despite that
>   participant making a contribution. 
> -	Participants are sometimes being rematched with people they have interacted with before. 
>
> Could you please help address these issues in the code?
>
> Thanks for your help.

## Follow Up Question
***If this researcher wanted instead to run this online, recruiting participants from the Prolific research participation
pool, what additional considerations would you need to make in the code?***

Do not attempt to implement features to address this possibility, but provide a written response of a few paragraphs
suggesting what additional complications you would need to address, ideally suggesting what features within oTree, or more
general techniques, you could leverage to mitigate these issues.

## Submission Details
### Code Changes
Please update the code in this repository to address the issues raised in the researcher's e-mail. You should include
code comments alongside your changes to explain to the researcher what the problems were and how you have addressed them so
that they can learn from your updates.

### Follow Up Question Response
Your response to the follow up question should be included in the top level directory of this repository in a file named
"follow_up_response" (e.g. "follow_up_response.md", "follow_up_response.pdf").

### Deadline
Your responses to this task should be committed to this repository by **12:00 UTC on Monday the 15th of September**.

# Useful Resources
You can find the [oTree documentation](https://otree.readthedocs.io/en/latest/) on readthedocs.io, including a
[tutorial](https://otree.readthedocs.io/en/latest/tutorial/part2.html) on a (more basic) public goods game. 

# Development Environment
We recommend working in a python virtual environment, using with a python 3.11 interpreter for maximum compatibility with
the current version of oTree. The provided requirements.txt should install all required packages and dependencies.  (Note
building of the psycopg2 wheel requires python development files, on ubuntu 22.04 LTS, it specifically requires python3-dev
and libpq-dev). 
