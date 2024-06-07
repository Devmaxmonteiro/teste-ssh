import subprocess

# Substitua 'repository_url' pela URL do repositório GitHub que você deseja clonar
repository_url = 'https://github.com/orgs/softbluecursoscode/repositories'

def clone_repository(url):
    try:
        print(f"Clonando {url}...")
        result = subprocess.run(['git', 'clone', url], check=True)
        print("Clonagem concluída.")
    except FileNotFoundError:
        print("Erro: 'git' não encontrado. Certifique-se de que o Git está instalado e no PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao clonar o repositório: {e}")

if __name__ == "__main__":
    clone_repository(repository_url)
