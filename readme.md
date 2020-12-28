My solutions to advent of code 2020, in Python

Some of the cool problems with a reasonnably clean solutions, and/or where I have learnt something are:
 - 1 using a hand rolled algo vs using itertools
 - 2 using a PEG − Parsing expression grammar. Thanks [Fasterthanlime](https://fasterthanli.me/series/advent-of-code-2020/part-2)
 - 7 The counting part was fun, it involves graph traversal using BFS and DFS
 - 8a (parsing and running a simple programming language). The first part is straightforward, the 2nd part does not add much
 - 10b dynamic programming (10b2 has some notes)
 - 13b (solved with chinese remainder theorem, which requires extended gcd)
 - 14b (generating every possible bit combinations)
 - Turns out 15 is the [Van Eck Sequence](https://rosettacode.org/wiki/Van_Eck_sequence). Many went for a brute force solution, which is OK on todays machines (<20s in python).
 - 18 involved evaluating a math expression. There are [many ways](https://www.reddit.com/r/adventofcode/comments/kfor25/2020_day_18_how_many_different_approaches_can_you/) to do so. I implemented 2 solutions: one that patched operators then ran eval, and another with the Shunting-yard algorithm (with the expected precedences) in order to convert the infix expression into RPN, then evaluate the RPN stack.
 - 19 involved the CYK algorithm, but it was easier to turn the rules into a regex
 - 20a. Classic backtracking, but with a lot of setup in order to generate the neighbouring states and and performing validity checks. Super cool !

Some cool links:
 - [the subreddit](reddit.com/r/adventofcode) where the community gathers
 - [Jonathan Paulson](https://www.youtube.com/channel/UCuWLIm0l4sDpEe28t41WITA)'s channel. One of the best competitors codes then explains its solutions every day. That's very impressive to watch, and the explanations are a goldmine to learn things.
 - [mjpieters](https://github.com/mjpieters/adventofcode/tree/master/2020) has idiomatic Python solutions in notebooks
 - [Advent of Code serie in rust](https://fasterthanli.me/series/advent-of-code-2020), by fasterthanlime. A great introduction to how experienced rustaceans think in the language.
 - [Visualization](https://www.reddit.com/r/adventofcode/comments/kcpdbi/2020_day_11_part_2luaroblox_waiting_room/) of the waiting room (day 11)
 - [Visualization](https://www.reddit.com/r/adventofcode/comments/kcw50x/day_7_all_the_bag_rules_in_full_colour/) of the bags (day 7)
 - Some [behind the scene](https://www.reddit.com/r/adventofcode/comments/k9lt09/postmortem_2_scaling_adventures/) details on the issues on the first days, and about [how AoC works under the hood](https://www.youtube.com/watch?v=bS9882S0ZHs).
 - [Upping the ante](https://www.reddit.com/r/adventofcode/comments/kcybyr/2002_day_14_part_2_but_what_if_the_input_is_harder/) is a category where some extra constraints are added to the problems, like longer inputs that discards bruteforce or new rules
 - [Getting Crafty](https://www.reddit.com/r/adventofcode/wiki/gettincrafty) shows some very creative ideas.
 - [How To Leaderboard](https://blog.vero.site/post/advent-leaderboard), by Betaveros, the… leader of the leaderboard.
 - [tourist](https://www.youtube.com/watch?v=97tieEKfvBs) is one of the best competitive programmers. He streams CodeForce problems, and that's… another level entirely.
 - [cp-algorithms](https://cp-algorithms.com/) which provides A LOT of great information regarding algorithms used for competitive programming.

Nice retrospectives:
 - julia idiomatic solutions: https://blog.kdheepak.com/advent-of-code-2020-retrospective.html
 - notes on AoC in Rust: https://explog.in/notes/aoc.html