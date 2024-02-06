class Board:
    __board: list[list[str]] = [[" "] * 3] * 3

    @classmethod
    def print_state(cls) -> None:
        for i in range(5):
            if i % 2 == 0:
                for j in range(5):
                    if j % 2 == 0:
                        print(cls.__board[i // 2][j // 2], end="")
                    else:
                        print(" | ", end="")
            else:
                for i in range(5):
                    if i % 2 == 0:
                        print("-", end="")
                    else:
                        print("   ", end="")
            print()
        return

    @classmethod
    def mark_at(cls, row: int, col: int, symbol: str) -> None:
        cls.__board[row][col] = symbol
        return

    @classmethod
    def game_state(cls) -> int:
        pass


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.symbol: str | None = None
        return

    def __repr__(self) -> str:
        return f"Player's Name: {self.name} and Symbol: {self.symbol}"

    def set_symbol(self, symbol: str) -> None:
        self.symbol = symbol
        return

    def play(self, row: int, col: int) -> None:
        Board.mark_at(row - 1, col - 1, self.symbol)
        print(f"{self.name} played at ({row}, {col})")
        Board.print_state()
        return


def play() -> None:
    print("Welcome to the Tic Tac Toe game!\n")
    Board()
    

def main() -> None:
    play()


if __name__ == "__main__":
    main()
