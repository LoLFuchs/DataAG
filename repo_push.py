from github import Github

# Zugriffstoken für die Authentifizierung
access_token = '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'

# GitHub-Repository Informationen
repository_name = 'LoLFuchs/DataAG'  # Ersetzen Sie 'username/repository' durch den tatsächlichen Benutzernamen und Repositorynamen
file_path = 'test.txt'  # Pfad zur Textdatei im Repository
commit_message = 'Update der Textdatei'

# Verbindung zur GitHub-API herstellen
g = Github(access_token)

# Repository und Datei abrufen
repo = g.get_repo(repository_name)
file = repo.get_contents(file_path)

# Aktuellen Inhalt der Datei abrufen
current_content = file.decoded_content.decode()

# Neuen Text hinzufügen
new_text = current_content + '\nDies ist der neue Text, der hinzugefügt wurde.'

updated_file = repo.update_file(file.path, commit_message, new_text, file.sha)

# Ausgabe der Commit-Details
print("Commit:", updated_file.commit.sha)
print("Datei-URL:", updated_file.content.html_url)
