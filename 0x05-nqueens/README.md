## N QUEENS(aka CHESS QUEENS)
The <strong>N Queens problem</strong> is a classic problem in computer science and mathematics that involves placing N chess queens on an NxN chessboard in such a way that no two queens threaten each other. In other words, no two queens should be placed in the same row, column, or diagonal on the chessboard.<br> There are various methods used in tackling the N Queens problem:

<h2>BACKTRACKING METHOD</h2>
The <strong>backtracking method</strong> is a recursive algorithm that systematically builds candidate solutions to the problem and abandons a candidate solution as soon as it determines that the solution cannot be completed.<br> The algorithm works as follows:
<ol>
<li>Start with an empty chessboard.</li>
<li>Place a queen in the first column of the first row.</li>
<li>Move to the second column of the second row and try to place a queen there.</li>
<li>If a queen can be placed in the second column of the second row without attacking the queen in the first column of the first row, move to the third column of the third row and try to place a queen there.</li>
<li>If a queen cannot be placed in the second column of the second row without attacking the queen in the first column of the first row, go back to the second column of the second row and try placing the queen in the next row (third row).</li> 
<li>If a queen cannot be placed in any row of the second column without attacking the queen in the first column of the first row, backtrack to the first column of the first row and try placing the queen in the next row (second row).</li>
<li>Continue this process until a queen can be placed in the last column of the last row without attacking any of the previously placed queens.</li>
<li>If a placement of a queen results in a conflict with a previously placed queen, the algorithm backtracks to the previous queen and tries a different position for the current queen.</li>
<li>If all positions for the current queen have been tried without success, the algorithm backtracks further until it finds a previously placed queen that has an untried position.</li> 
<li>This process continues until a solution is found or all possible configurations have been tried.</li>
</ol>
<em>The N Queens problem is known to have a solution for any value of N greater than or equal to 4</em>, and the number of distinct solutions increases rapidly with N. The number of distinct solutions for N=8 is 92, while the number of solutions for N=9 is 352, and the number of solutions for N=10 is 724. For larger values of N, the number of distinct solutions becomes prohibitively large to compute exhaustively, and more efficient algorithms are required to solve the problem.<br>
The statement <em>"The N Queens problem is known to have a solution for any value of N greater than or equal to 4"</em> is based on mathematical proof.
<br>
It has been shown that the problem has no solutions for N = 2 and N = 3, but for any value of N greater than or equal to 4, a solution always exists. The proof for this statement relies on showing that the problem can be reduced to a simpler problem that has a known solution.
<br>
For example, it has been shown that the N Queens problem can be reduced to the problem of placing non-attacking <em><mark>rooks</mark></em> on an NxN chessboard. Since there is a known formula for the number of ways to place non-attacking rooks on a chessboard, the existence of a solution for the N Queens problem follows.<br>
<h3>THE ROOK</h3>
In chess, a <strong>rook</strong> is a piece that moves horizontally or vertically on the chessboard. The rook can move any number of squares along <em><strong>the rank (rows) or file (columns)</strong></em>, but cannot move diagonally.<br>

When placing N non-attacking rooks on an NxN chessboard, the rooks are placed on the board such that no two rooks occupy the same row or column. This means that if you place rook1 on rank1 and rook2 on rank2, you do not have to place rook1 on file1 and rook2 on file2 to avoid any interference or collision when moving the rooks.
<br>
In the case of the <em><strong>N Queens problem</strong></em>, each queen is assigned to a different row, and the problem is to place the queens on the board such that no two queens attack each other. This means that no two queens should be on the same row, column, or diagonal.
<br>
<h2>SYMMETRIES METHOD</h2>
Another approach is to exploit the symmetries of the problem and reduce the search space by considering only a subset of all possible placements. This approach is more efficient than the exhaustive search and can be used to compute the number of distinct solutions for larger values of N.
<br>
<h2>ITERATIVE DEEPENING METHOD</h2>
Additionally, researchers have used advanced algorithms such as iterative deepening, bit-wise operations, and parallel computing to calculate the number of distinct solutions for the N Queens problem. These methods involve a combination of mathematical analysis and computer programming and may not be easy to understand without a strong background in computer science and mathematics.
<br>
<h2>REAL WORLD APPLICATIONS</h2>
The N Queens problem has many real-world applications, including in robotics, scheduling, and graph theory. It is also used as a benchmark problem in computer science to evaluate the performance of algorithms and hardware.