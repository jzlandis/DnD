# DnD
Tools For Basic DnD
[Reference Rule Book][1]
[1]: http://media.wizards.com/2016/downloads/DND/PlayerBasicRulesV03.pdf

* characterInit.py

Tryout the characterInit.py file to generate starting ability scores (per chapter 1 step 3 in the pdf)

First way:
```shell
$ python characterInit.py
Select the method for choosing abilities:
[0] Generate random values per ch1.3
[1] Use the presets (15,14,13,12,10,8)
>>> 0
1th four d6 rolls are  5,  6,  2,  2, top 3 sum to 13, this will yield a modifier of  1
2th four d6 rolls are  3,  6,  4,  2, top 3 sum to 13, this will yield a modifier of  1
3th four d6 rolls are  2,  4,  5,  2, top 3 sum to 11, this will yield a modifier of  0
4th four d6 rolls are  1,  5,  3,  4, top 3 sum to 12, this will yield a modifier of  1
5th four d6 rolls are  2,  3,  3,  1, top 3 sum to  8, this will yield a modifier of -1
6th four d6 rolls are  4,  4,  2,  3, top 3 sum to 11, this will yield a modifier of  0
Your available scores and modifiers are as follows
--AbilityScore- ----Modifier---
       13               1      
       13               1      
       12               1      
       11               0      
       11               0      
        8              -1      
```

Second way:
```shell
$ python characterInit.py
Select the method for choosing abilities:
[0] Generate random values per ch1.3
[1] Use the presets (15,14,13,12,10,8)
>>> 1
Your available scores and modifiers are as follows
--AbilityScore- ----Modifier---
       15               2      
       14               2      
       13               1      
       12               1      
       10               0      
        8              -1      
```
