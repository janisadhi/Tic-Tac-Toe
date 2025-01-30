# Flask-based Tic Tac Toe Application

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Game state variables
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
status = "Player X's turn"

@app.route('/')
def index():
    indexed_board = [(i, [(j, cell) for j, cell in enumerate(row)]) for i, row in enumerate(board)]
    return render_template('index.html', board=indexed_board, status=status)

@app.route('/move', methods=['POST'])
def move():
    global current_player, status
    row = int(request.form['row'])
    col = int(request.form['col'])

    if board[row][col] == '':
        board[row][col] = current_player
        if check_winner():
            status = f"Player {current_player} wins!"
        elif all(cell != '' for row in board for cell in row):
            status = "It's a draw!"
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            status = f"Player {current_player}'s turn"

    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player, status
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    status = "Player X's turn"
    return redirect(url_for('index'))

def check_winner():
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '' or board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)

