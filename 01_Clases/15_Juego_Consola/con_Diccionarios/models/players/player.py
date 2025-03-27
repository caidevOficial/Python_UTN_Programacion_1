
def create_player(name: str, symbol: str = 'X') -> dict:
    player = {
        "name": name,
        "movements": 0,
        "total_movements": 0,
        "symbol": symbol,
        "has_win": False
    }
    return player

def reset_status_player(player: dict) -> dict:
    player["movements"] = 0
    player["has_win"] = False
    return player

def increase_movements(player: dict, amount: int) -> dict:
    player['movements'] = player.get('movements') + amount
    return player

def get_player_name(player: dict) -> str:
    return player.get('name')

def get_player_movements(player: dict) -> int:
    return player.get("movements", 0)

def get_player_win(player: dict) -> bool:
    return player.get('has_win')

def get_player_symbol(player: dict) -> str:
    return player.get('symbol')

def get_player_total_movements(player: dict) -> int:
    return player.get('total_movements')

def update_player_total_movements(player: dict) -> None:
    player['total_movements'] += player.get('movements', 0)