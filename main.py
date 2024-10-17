import streamlit as st
import numpy as np

st.title("Tic Tac Toe Game")

# Game board
if 'board' not in st.session_state:
    st.session_state.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])

if 'player_turn' not in st.session_state:
    st.session_state.player_turn = True  # True if it's player's turn

def check_winner(board, mark):
    for i in range(3):
        if np.all(board[i, :] == mark) or np.all(board[:, i] == mark):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == mark or board[0, 2] == board[1, 1] == board[2, 0] == mark:
        return True
    return False

def check_draw(board):
    return not np.any(board == "")

def computer_move(board):
    # Computer plays "O"
    for i in range(3):
        for j in range(3):
            if board[i, j] == "":
                board[i, j] = "O"
                if check_winner(board, "O"):
                    return
                board[i, j] = ""
    for i in range(3):
        for j in range(3):
            if board[i, j] == "":
                board[i, j] = "X"
                if check_winner(board, "X"):
                    board[i, j] = "O"
                    return
                board[i, j] = ""
    for i in range(3):
        for j in range(3):
            if board[i, j] == "":
                board[i, j] = "O"
                return

# Display the game board
def display_board():
    for i in range(3):
        cols = st.columns([1, 1, 1])
        for j in range(3):
            with cols[j]:
                if st.session_state.board[i, j] == "":
                    if st.button(f" ", key=f"{i}{j}"):
                        if st.session_state.player_turn:
                            st.session_state.board[i, j] = "X"
                            st.session_state.player_turn = False
                            if check_winner(st.session_state.board, "X"):
                                st.session_state.winner = "Player"
                            elif check_draw(st.session_state.board):
                                st.session_state.winner = "Draw"
                        if not st.session_state.player_turn and 'winner' not in st.session_state:
                            computer_move(st.session_state.board)
                            st.session_state.player_turn = True
                            if check_winner(st.session_state.board, "O"):
                                st.session_state.winner = "Computer"
                            elif check_draw(st.session_state.board):
                                st.session_state.winner = "Draw"
                else:
                    st.write(st.session_state.board[i, j])

display_board()

# Display game result
if 'winner' in st.session_state:
    if st.session_state.winner == "Draw":
        st.write("It's a Draw!")
    else:
        st.write(f"{st.session_state.winner} wins!")
    if st.button("Restart Game"):
        del st.session_state.board
        del st.session_state.player_turn
        del st.session_state.winner
