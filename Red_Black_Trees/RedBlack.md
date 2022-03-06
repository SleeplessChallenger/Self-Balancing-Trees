<h2>Red Black tree notes</h2>

- This tree is BST as well as AVL-Trees

1. `root` is always black
2. no `red-red` parent-child relationship. I.e. some in the	
	chain must be black
3. number of black nodes from `root` to node with **less** than
	2 children should be the same. What does it mean? =><br>

```bash
		B                B
	  /	  \            /   \
	 B    null        R     B
	/ \              / \   /  
    B null          B   B  R
```
See, in the first tree path from `root` (aka B) to `null`: 1 black node. In the second path: `B` - `B` - `null` -> 2 black nodes. Same with the last-longest path.

For comparision, let's look at the second tree. `B` - `R` - `B` (left) and `B` - `R` - `B` (right) have same number of black nodes. If you inspect right subtree: same number of black nodes

<h3>Rules for R-B trees creation</h3>

1. If no `root` -> insert node as **black** root
2. Insert new leaf node as **red**:
	* If parent is black -> done
	* If parent is red -> Conflict!!

a. first sub-case where we insert `4` as leaf node
```bash
		  10-B
	    /     \
	  -10-R   20-B
	  / \     /  \
   -20-B 6-B null 25-R
 		/
	   4-R	
```

b. second sub-case where we also insert `4`, but now it's parent is red
```bash
		 10-B
	  /        \
	-10-R     20-B
	/  \      /    \
  -20-B 6-B  15-R 25-R
        /  \
       2-R  8-R  
        \
         4-R
```
<h4>Steps to follow</h4>

1. Look at the colour of the parent's sibling which is
8 in our case. **If it's red** => re-colour both (parent and it's sibling) to black & check again: `2-R -> 2-B & 8-R -> 8-B`

	1.1. Next, if parent of those 2-above-changed-nodes isn't `root`
of the tree -> re-colour it (in Red)
	1.2 Now, re-checking step. We see the following picture:
```bash
		 10-B
	  /        \
	-10-R     20-B
	/  \      /    \
  -20-B 6-R  15-R 25-R
        /  \
       2-B  8-B  
        \
         4-R
```
	Again red-red relationship in `10 - 6`. Steps resemble the ones above: look at parent's (10) sibling which is 20 in our case. It's black: **Look below for 3**

2. In 1.1 there is second case: if parent of leaf-node parent & sibling is `root`?
```bash
		 10-B
	  /        \
	-10-B     20-B
	/  \      /    \
  -20-B 6-R  15-B 25-B
        /  \
       2-B  8-B  
        \
         4-R
```
	1.1 Do all the steps as above. However, after we've changed
		colour of `-10` & `20` from Red to Black, we check their parent. In this case it's `root` of all the tree => stop here

All in all, we keep rechecking the parent & subling till there is Red-Red relationship

3. If sibling is **Black** or **absent** at all. In this situation we have 4 cases:
	- right rotation
	- left-right rotation
	- left rotation
	- rigth-left rotation

PS: yeah, they resemble AVL-Tree rotations

<h4>If sibling is absent</h4>

<h5>Right rotation</h5>

Let's insert 13 as new leaf node
```bash
		10-B
	  /      \
	-10-B    20-B
	  \       /
	   7-R   15-R 
             /
            13-R  	
```
1. Firstly, as usual, there is red-red conflict. We look at the sibling of parent (== `15`), but it's missing. We make:
	* **right rotation** The left part of the tree will be the same, but in the right subtree there will be changes
	* switch colours of `x` & `y`. Recall `x` & `y` from AVl-Tree

```bash
		10-B
	  /      \
	-10-B    15-B - Becomes Black
	  \       /  \
	   7-R  13-R  20-R	- Becomes Red
```

<h5>Left-right rotation</h5>

Let's insert `17`

```bash
		10-B
	  /      \
	-10-B    20-B
	  \       /
	   7-R   15-R 
	   		   \
	   	      17-R
```

1. At first make `left rotation`
```bash
		10-B
	  /      \
	-10-B    20-B
	  \       /
	   7-R   17-R 
	   		 /
	   	   15-R
```

2. Then make `right`
```bash
		 10-B
	  /       \
	-10-B     17-R -> change to Black
	  \       /   \
	   7-R   15-R 20-B -> change to Red
```

3. Same as in `right` rotation: re-colour `x` and `y` (i.e. swap colours)

<h5>Right rotation</h5>

# TODO: self-study

<h5>Right-left rotation</h5>

# TODO: self-study

<h4>If sibling is black</h4>


