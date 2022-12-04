# calculield

This project perfoms the regular mathematical calculations on an infinite stream.

This has been categorised into 2 ways of accessing it.


**Glossory**:
**Item** | **Description** | **Value**
--- | --- | --- 
Show String | The character which halts the stream and perform the calculation | ? 
Iteration Stopper | In case of non show strings, to avoid infinite loops an iteration stopper number is used | 15
Sequence Breaker | The input sequence will break if any of the mentioned character appear | ```++	--	-* *-	-/	/-```



1. Regular python file based
	
	Under Core, yeilder.py takes in an argument and performs the mathematical operations.

	>```python 
	>python yeilder.py "1+1?\*(3\*2)/4?++" 
	>```
	>
	>_Result_
	>```
	>1+1 = 2 
	>1+1*(3*2)/4 = 2.5
	>1+1*(3*2)/43+4 = 5.1395
	>terminating the program due to a wrong sequence
	>ERROR
	>```

	>```python 
	>python yeilder.py "1 1 * 2 ? 1 + (3 ?* 2 ?/ 1 + 3 )?* 2 ? 1 + 3 ? * 7 ? + 8 7 9 ?"
	>```
	>
	>_Result_
	>```
	>11*2 = 22
    >11*21+(3 --> 11*21+3 = 234
    >11*21+(3*2 --> 11*21+3*2 = 237
    >11*21+(3*2/1+3) = 240.0
    >11*21+(3*2/1+3)*2 = 249.0
    >11*21+(3*2/1+3)*21+3 = 423.0
    >11*21+(3*2/1+3)*21+3*7 = 441.0
    >11*21+(3*2/1+3)*21+3*7+879 = 1320.0
    >11*21+(3*2/1+3)*21+3*7+87911*2 = 176263.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3 --> 11*21+3*2/1+3*21+3*7+87911*21+3 = 1846455.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3*2 --> 11*21+3*2/1+3*21+3*7+87911*21+3*2 = 1846458.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3*2/1+3) = 1846581.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3*2/1+3)*2 = 1846590.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3*2/1+3)*21+3 = 1846764.0
    >11*21+(3*2/1+3)*21+3*7+87911*21+(3*2/1+3)*21+3*7 = 1846782.0
    >('reached the max iterations:', 15)
	>```

		
	
2. Web app based
	
	This is built over the flask framework. 

	The calculated values over the provided input are shared on the same page with input also with the plotting values upto the calculated iterations.
	
	

**Special scenarios**

Brackets parsing :	
	



