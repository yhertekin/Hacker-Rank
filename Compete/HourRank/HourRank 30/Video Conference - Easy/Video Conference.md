# Video Conference #

Bob is making a video conference software. Whenever a new person joins the conference, Bob displays the person's name in the interface.
But displaying full name is boring and takes a lots of space. So he decided to display the shortest prefix which doesn't match with any prefix of any person who have joined earlier.
Let's suppose the first person to enter the conference is alvin .

![](https://s3.amazonaws.com/hr-assets/0/1515332893-646e16b636-Conference.png)

Now suppose next person to join is alice. The shortest prefix of alice that doesn't match with any prefix of alvin is ali.

![](https://s3.amazonaws.com/hr-assets/0/1515333247-8470db87c2-Conference1.png)

If the full name of a new person matches completely with the full name of any person who has joined earlier, he will display the full name and add a suffix which indicates how many times the same name has occurred in the list so far. For example, if another person name alvin joins, the list will look like this:

![](https://s3.amazonaws.com/hr-assets/0/1515333466-436385cc1b-Conference2.png)

You are given the list of the persons who have joined the call in the chronological order. Your task is to figure out how the final list looks like.

#### Input Format ####

The first line contains an integer n.

The subsequent n line contains a string si	denoting the name of the ith person to join the call.

#### Constraints ####

    1 <= n <= 10^5
    1 <= si <= 10

si will contain only lower-case english letters.

#### Subtask ####

    1 <= n <= 1000 for 60% of the maximum score

#### Output Format ####

Return a string array with n items, the ith line should contain the prefix of name of the ith person which doesn't match with any other person who has joined earlier.

#### Sample Input 0 ####
    3
    alvin
    alice
    alvin

#### Sample Output 0 ####
    a   
    ali
    alvin 2

#### Sample Input 1 ####

    6
    mary
    stacy
    sam
    samuel
    sam
    miguel

#### Sample Output 1 ####

    m
    s
    sa
    samu
    sam 2
    mi