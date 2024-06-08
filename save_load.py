import pickle

def save_game(game, filename='game_state.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(game, f)

def load_game(filename='game_state.pkl'):
    with open(filename, 'rb') as f:
        game = pickle.load(f)
    return game
