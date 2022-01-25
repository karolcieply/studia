import java.util.*;

public class Main {
    public static void main(String args[]) {
        GameBoard g = new GameBoard();
        boolean[][] test = g.getCurrent();
        for (int i = 1; i <= 10 - 2; i++) {
            for (int j = 1; j <= 10 - 2; j++) {
                System.out.print(test[i][j]);
                System.out.print(" ");
            }
            System.out.println("");
        }
        g.calculateFuture();
        test = g.getCurrent();
        for (int i = 1; i <= 10 - 2; i++) {
            for (int j = 1; j <= 10 - 2; j++) {
                System.out.print(test[i][j]);
                System.out.print(" ");
            }
            System.out.println("");
        }
    }

}

class GameBoard {
    private boolean[][] current = {
            {
                    false, false, false, false, false, false, false, false, false, false
            },
            {
                    false, true, true, false, false, false, false, false, false, false
            },
            {
                    false, true, true, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, false, false, false, false, false, false
            },
            {
                    false, false, false, false, false, false, false, false, false, false
            }
    };
    private boolean[][] future = {
            {
                    false, false, false, false, false, false, false, false, false, false
            },
            {
                    false, true, true, false, false, false, false, false, false, false
            },
            {
                    false, true, true, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, false, false, false, true, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, true, false, false, false, false, false
            },
            {
                    false, false, false, false, false, false, false, false, false, false
            },
            {
                    false, false, false, false, false, false, false, false, false, false
            }
    };

    GameBoard() {
        // current = new boolean[BOARD_HEIGHT][BOARD_WIDTH];
    }

    public boolean[][] getCurrent() {
        return current;
    }

    public void calculateFuture() {
        for (int i = 1; i <= 10 - 2; i++) {
            System.out.println(this.current[2][7]);
            for (int j = 1; j <= 10 - 2; j++) {
                int aliveNeighbours = this.current[i][j] ? -1 : 0;
                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        if (this.current[i + x][j + y]) {

                            aliveNeighbours += 1;
                        }
                    }
                }
                if (aliveNeighbours == 3 ||
                        (aliveNeighbours == 2 && this.current[i][j])) {
                    this.future[i][j] = true;
                } else {
                    this.future[i][j] = false;
                }
            }
        }
        this.current = this.future;
    }

    public void changeState(int x, int y) {
        current[x][y] = !current[x][y];
    }

}