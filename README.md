## Chess posisitons

#### Context
The goal of the project is to build a model able to recognize the existence of chess pieces on a chess board, classify them into pawn, bishop, rook, knight, queen or king and generate a [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) description based on a schematic image of a chess board.

#### Dataset
The dataset contains **100.000 images** of a randomly generated chess positions, divided into 80.000 images for training set and 20.000 images for test set.

The dataset has:
- 5-15 pieces (2 kings and 3-13 pawns/pieces);
- 896 board/piece style combinations (28 styles of chess boards and 32 styles of chess pieces); 
- all images are 400 by 400 px;
- all images were generated on [Chess.com](https://www.chess.com/);
- some positions may be illegal such as both kings are under check;
- images labels are in a filename in Forsyth–Edwards Notation format, but with dashes instead of slashes.

Pieces were generated with the following probability distribution:
- 30% for pawn;
- 20% for bishop;
- 20% for knight;
- 20% for rook;
- 10% for queen;
- 100% for king.

Remember: all chess games start with **16 pawns, 4 bishops, 4 rooks, 4 knights, 2 queens** an **2 kings**.

#### Acknowledgements
https://www.kaggle.com/koryakinp/chess-positions

https://github.com/tlehman/fenparser
