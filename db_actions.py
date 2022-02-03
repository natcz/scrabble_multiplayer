from db_players import History, Player, get_session


def get_history():
    session = get_session()
    records = session.query(History).all()
    records = sorted(records,
                     key=lambda player: player.get_points(),
                     reverse=True)
    return records


def get_players():
    session = get_session()
    return session.query(Player).all()


def save_winner(winner):
    session = get_session()
    session.add(winner)
    session.commit()


def save_player(player):
    session = get_session()
    session.add(player)
    session.commit()
