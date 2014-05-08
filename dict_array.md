|	lists			|         dictionaries	|
|-------------------------------|---------------------	|
|slice notation (L[1:2])		| none			|
|L[i] = assigns element to index i, and i has to be an index | L[i] = assigns value to key i, i can be any immutable type
|for loop goes on values   	 | for loop goes on keys       	      	      	       	|
| L.remove(value) 		 | none							|
| L.pop(index)			 | D.pop(key)						|
| del L[index]			 | del D[key]						|
| max(L)			 | max(D) highest index with any string > a number	|
| sorted(L)			 | sorted(D) returns sorted(D.keys())			|
| len(L)			 | len(D) is len(D.keys()) 				|
| L1 + L2			 | + doesn't work!? 					|