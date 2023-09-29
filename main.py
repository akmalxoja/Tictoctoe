import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class TicTacToeGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 600, 600)

        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'

        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = QPushButton('', self)
                button.setGeometry(col * 200, row * 200, 200, 200)
                button.clicked.connect(lambda _, r=row, c=col: self.button_clicked(r, c))
                self.buttons.append(button)

    def button_clicked(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row * 3 + col].setText(self.current_player)

            if self.check_winner():
                QMessageBox.information(self, "Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                QMessageBox.information(self, "Draw", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_game(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
        for button in self.buttons:
            button.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToeGame()
    game.show()
    sys.exit(app.exec_())