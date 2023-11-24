import mysql.connector
from mysql.connector import Error
import datetime



def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', user='projdbpy', password='Pa$$w0rd', port='3306',
                                      database='projpy', buffered=True, autocommit=True)
def get_results():
    try:
        connect = open_dbconnection()
        if connect:
            cursor = connect.cursor(dictionary=True)

            # Récupérer les résultats quand on appuie sur terminer
            cursor.execute("""
                SELECT players.pseudo, exercices_has_played.duration, exercices_has_played.dateAndHour, exercices_has_played.nbTotal, exercices_has_played.nbOk
                FROM exercices_has_played
                INNER JOIN players ON exercices_has_played.players_id = players.id
                ORDER BY exercices_has_played.dateAndHour DESC
            """)
            all_results = cursor.fetchall()

            if all_results:
                return all_results
            else:
                print("Aucun résultat a été trouvé.")
                return None

    except Error as e:
        print(f"Erreur pendant la récupération des résultats : {e}")

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            print(" La connexion à la base de données a été fermée")

def get_userid(player_pseudo):
    try:
        connect = open_dbconnection()
        if connect:
            cursor = connect.cursor()

            # Récupérer l'id du joueur
            cursor.execute(f"SELECT id FROM players WHERE pseudo = '{player_pseudo}'")
            user_row = cursor.fetchone()

            print(f"Résultat de la requête du joueur '{player_pseudo}': {user_row}")

            if user_row:
                user_id = user_row[0]
                return user_id
            else:
                print(f"Le joueur possèdant le pseudo '{player_pseudo}' n'est pas dans la base de données.")
                return None

    except Error as e:
        print(f"Erreur pendant la récupération de l'id du joueur : {e}")

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            print("La connexion à la base de données a été fermée")

def get_exerciseid(exercise_name):
    try:
        connect = open_dbconnection()
        if connect:
            cursor = connect.cursor()

            # Récupération de  l'id de l'exercice
            cursor.execute(f"SELECT id FROM exercices WHERE exercice_name = '{exercise_name}'")
            exercise_row = cursor.fetchone()

            if exercise_row:
                exercise_id = exercise_row[0]
                return exercise_id
            else:
                print(f"L'exercice avec le nom '{exercise_name}' n'est pas dans la base de données.")
                return None

    except Error as e:
        print(f"Erreur pendant la récupération de l'id de l'exercice : {e}")

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            print("La connexion à la base de données a été fermée")

def save_result(exercise_name, players_pseudo, start_date, duration, nb_trials, nb_ok):
    try:
        connect = open_dbconnection()
        if connect:
            cursor = connect.cursor()

            # Récupérer l'id du joueur ou en ajouter un s'il n'est pas dans la base de données
            user_id = get_userid(players_pseudo)

            if user_id is not None:
                print(f"Le joueur '{players_pseudo}' à déjà été créé. Id: {user_id}")
            else:
                # Ajouter un joueur et récupérer l'id
                cursor.execute(f"INSERT INTO players (pseudo) VALUES ('{players_pseudo}')")
                connect.commit()
                user_id = cursor.lastrowid  # Récupérer l'id après avoir ajouté à la base de données
                print(f"Le joueur '{players_pseudo}' à été ajouté. Id: {user_id}")

            # Affichage du pseudo
            print("Résultat enregistré pour le joueur:", players_pseudo)

            # Ajout de l'exercice
            exercise_id = get_exerciseid(exercise_name)
            if exercise_id is None:
                cursor.execute(f"INSERT INTO exercices (exercice_code) VALUES ('{exercise_name}')")
                connect.commit()
                exercise_id = cursor.lastrowid  # Récupérer l'id.
                print(f"Exercice '{exercise_name}' a été ajouté. Id: {exercise_id}")

            # Insérer le résultat dans la table exercices_has_played
            cursor.execute(
                f"INSERT INTO exercices_has_played (duration, dateAndHour, nbTotal, nbOk, players_id, exercices_id) "
                f"VALUES ('{duration}', '{start_date}', {nb_trials}, {nb_ok}, {user_id}, {exercise_id})"
            )

            connect.commit()
            print("Le résultat a été enregistré")

    except Error as e:
        print(f"Erreur pendant l'enregistrement du résultat dans la base de données: {e}")

    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            print("Connexion fermée")