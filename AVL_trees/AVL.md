<h2>AVL trees notes</h2>
<hr>

- It is also known as one of the self-balancing trees. Purpose? => Avoid Skewdness
- There is a balance (aka threshold) which will ensure that we don't have a skedness. If it's broken `=>` we'll have our tree rebalanced

<ol>
	<li>Balance</li>
	<li>Rotations</li>
	<li>Implementation</li>
</ol>

<hr>
<h3>Balance</h4>


- Let's imagine our tree:
```bash
	 n
	/ \
       Tl  Tr
```
- Then, we have a <b>height</b> of a tree.
	+ it's 0 if we have only **root**
	+ it's `-1 || null` if we doesn't have anything

- Set of actions:
	+ `H = max(H(Tl), H(Tr)) + 1`
	+ `B(n) = H(Tl) - H(Tr)`. This is a formula for balance<br>
		Further down we'll use `B` to say that we calc. balance, <b>simple height</b>
	+ AVL Tree = |B(n)| <= 1 where || means `abs()` && 1 can be parameterized

- Let's peruse the example below:
	+ Example below is a balanced tree as: **B(3) = 1 - 0 => 1**
	+ If `B` is positive => <i>left-heavy</i>
	+ If `B` is negative => <i>right-heavy</i>
		* It shows which part dominates the equation
	+ B(0) = 0; B(2) = 0 hence B(1) is 0 **BUT** when we come back to 3,<br>
		we add + 1 after 1, hence we have heigh of 1. Then, H(4) = -1 - (-1) = 0

```bash
	    3
	   / \
	  1   4
	 / \
	0   2
```

- Now, let's peruse non-AVL tree:
```bash
	     4
	    /
	   3
	  /
	 2
	/ \
       1   0
```

- After eyeboll, we come to the closing: 2 - (-1) = 2 + 1 = 3 => broken the **threshold** && it's not the AVL Tree.
- And if we wanted to calc. the balance:
	+ B(1) = -1 - (-1) = 0
	+ B(0) = -1 - (-1) = 0
	+ B(2) = 0 - 0 = 0. Then we add 1 if we calc. height (see above)
	+ B(3) = 0 - (-1) = 1
	+ B(4) = 1 - (-1) = 2

<hr>
<h3>Rotations</h4>

<h5>Overview</h5>
- It is how we'll maintain the <b>balance</b> aka fix imbalance

- There are 2 so-called **heavy** situations:
	* left-heavy: when left part is bigger:
		* How to fix it?
			<ol>
				<li>right</li>
				<li>left-right</li>
			</ol>
	* right-heavy: when right part is bigger
		* How to fix it?
			<ol>
				<li>left</li>
				<li>right-left</li>
			</ol>
	* There are always 2 nodes in a tangle. Look at the **screen 1**:
		+ first one is before **rotation** && second one is after **rotation**
		+ y < x
		+ **red** < y && < x
		+ **blue** >= y && < x
		+ **purple** >= y && >= x

<h5>1.1 Right rotation</h5>

- Let's inser values 3,2,1
	+ H(1): max(-1,-1) + 1 = 0
	+ H(2): max(0,-1) + 1 => 1
	+ H(3): max(1,-1) + 1 => 2
- If we calc. simple Balance:
	+ B(1) = -1 - (-1) = 0
	+ B(2) = 0 - (-1) = 1
	+ B(3) = 1 - (-1) = 2

- We're <i>left-heavy</i> as we have positive integer
- Start rotation:
	+ focus only at **x** && **y**
```bash
     3       2
    /	    / \
   2    => 1   3
  /
 1
```

<h5>1.2 Left-right</h5>

- Let's insert values 3,1,2
	+ H(2): max(-1,-1) + 1 = 0
	+ H(1): max(-1,0) + 1 = 1
	+ H(3): max(1,-1) + 1 = 2

- Now let's calc. Balance:
	+ B(2) = -1 - (-1) = 0
	+ B(1) = 0 - (-1) = 1
	+ B(3) = 1 - (-1) = 2

- If we do <i>right</i> rotation, then it'll give us skewed tree to the right

```bash
    3       1
   / 	     \
  1   =>     3 - BAD as it has -2 overall balance
   \	    /
    2	   2
```

- That's why we use **left-right** rotation where:
	+ at first apply **left** to 1 && 2
	+ then apply **right** to 2 && 3:

```bash
            3       3     2
	   /       /     / \
	  1   =>  2  => 1   3 
	   \     /
	    2   1
```

<h5>2.1 Left rotation</h5>

- Let's insert values 1,2,3. Opposite of **screen1**
	+ Again, focus only on **x** && **y** where former is 1 && latter is 2

- If we calc **Balance**:
	+ B(3) = -1 - (-1) = 0
	+ B(2) = 0 - (-1) = 1
	+ B(1) = -1 - 1 = -2

- Let's calc. height before <i>rotation</i>:
	+ H(3) = max(-1,-1) + 1 = 0
	+ H(2) = max(0,-1) + 1 = 1
	+ H(1) = max(1,-1) + 1 = 2

```bash
	1                2
	 \              / \
	  2      =>    1   3
	   \
	    3
```

<h5>2.2 Right-left</h5>

- Let's insert the following: 1,3,2 && calc. balance before <i>rotations</i>
	+ B(2) = -1 - (-1) = 0
	+ B(3) = 0 - (-1) = 1
	+ B(1) = -1 (left subtree) - 1 = -2

- Height before rotation: 2

```bash
	1        1          2  
	 \        \        / \
	  3  =>    2   => 1   3
	 /          \
	2            3
```

<h4>Screenshots</h4>

1. ![Alt text](img/first_screen.jpg?raw=true)
