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

- After we've inserted, `parent` of leaf and it's sibling
	will never be black, it's always red. But after further
	recolouring we may end up with `sibling` being black.

- Insert 4 as a leaf node

```bash
		 10-B
	  /			\
	 -10-R 		20-B
	 /    \      /  \
	-20-B 6-B  15-R  30-R
		  /  \
		 1-R 9-R	 
		  \
		  4-R
```

1. Make `parent` & `sibling` of parent **black**

```bash
		 10-B
	  /			\
	 -10-R 		20-B
	 /    \      /  \
	-20-B 6-R  15-R  30-R
		  /  \
		 1-B 9-B	 
		  \
		  4-R
```

2. So, we create a red-red situation: `6-10`
	=> fix it by looking at sibling of parent, where:
		- parent: -10
		- sibling: 20
	=> We see that sibling is **black**. Solution? -> some rotation

But which rotation is an option? Let's see: `6` is a **right** child
	of `-10` && `-10` is a **left** child of `10`. As a result, we need to do: Left rotation followed by right rotation.
	<ul><p>Position of node followed by required rotation</p>
		<li>LL -> Right</li>
		<li>RL -> Left-Right</li>
		<li>RR -> Left</li>
		<li>LR -> Right-Left</li>
	</ul>

<b>PS: We need to start identification of the desired rotation<br>
	from current **red** to the closest root<b>

2.1 Make left rotation at first (10-x, 6-y)
```bash
		 10-B
	   /      \
	  6-R     20-B
     /   \     /    \
   -10-R 9-B  15-R 30-R
   /  \
 -20-B 1-B
        \
         4-R
```

2.2 Make right rotation then: x-10, y-6 && flip colours of `x` & `y`
```bash
		 6-R -> B
	  /		    \
	 -10-R	10-B -> R
	 /  \	    /   \
  -20-B 1-B   9-B  20-B
	 	  \        /    \
	 	   4-R    15-R 30-R	 	 
```


# TODO: In article write eveyrthing in greater detail: how rotation is done

<h4>Why do rotations work?</h4>

- Let's assume we have a very large tree where only some chunk is
seen to us:
- why `n-2`: we already have 2 black nodes
- why `n-1`: in this subtree we have 1 black node

```bash
	nodes
		\
		 2-B
	   /    \
	  1-B    3-R
	  / \   /  \
	  v  w  x   4-R
	n-2 n-2 n-1 / \
	  		    y  z
	  		   n-1 n-1	
```
- Steps:
	* see that `3-4` have red-red relationship
	* start from the current node: `4` is a right child of `3` & `3` is righ child of `2` and -> Left rotation
	* Where `x`: 2 & `y`: 3. Why like that? => we need to do
		only Right rotation, hence we start from the closest root
	* don't forget to do the re-colouring 

	- Reasons:
		* new `root` is black: no red-red relationship
		* num of black nodes in subtrees:
			- v: n-2
			- w: n-2
			- x: n-1
			- y: n-1
			- z: n-1
		=> everything stays the same and works fine

```bash
		nodes
			\
			 3-R -> B
			 /    \
	  	 2-B -> R 4-R
		  / \	  / \
	  	1-B	 x    y  z
	  	/ \
	  	v  w
```

<h5>Why is R-B tree more efficient than AVL-tree?</h5>
	- In latter after rotation we may face further rotations
		in upper levels of the tree
	- In R-B tree we did only one set of rotations and finish

<h4>Construction of Red-Black tree from scratch</h4>

1. nodes: 10, 20, -10, 15, 17, 40, 50, 60
2. Concise algorithm:
```bash
	if (empty) Black Node
	else
		create Red leaf node
		if (parent is Black) done
		else
			if (parent's sibling is red)
				if (parent' sibling is root)
					recolour
				else
					recolour && recheck
			else // black
				if (LL) rotate right
				if (LR) rotate right-left
				if (RL) rotate left-right
				if (RR) rotate left
```

# FIXME: compare algorithm with drawings at the beginning

All in all, this kind of trees helps to maintain self-balancing factor with the help of colours. As you can see, there are rotations as in AVL-Tree, however, AVL-tree keeps balance with the help of `balance`, whilst Red-Black tree does it via colours.
