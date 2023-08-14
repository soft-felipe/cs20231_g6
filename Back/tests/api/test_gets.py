from fastapi.testclient import TestClient

def test_usuario_lista(client: TestClient) -> None:
    response = client.get("/usuario/listar")
    body = response.json()  # Todos os usuários
    assert response.status_code == 200


def test_dados_usuario(client: TestClient) -> None:
    response = client.get("/usuario/listar/2")   # User 2: Padrão
    body = response.json()
    assert response.status_code == 200
    assert body['username'] == 'felipe_moreira'


# -------- IMPORTANTE: Retirar a autenticação para rodar os testes locais -------- #

# Comandos RUN TESTS:
# $ cd Back/tests
# $ pytest

def test_all_projetos(client: TestClient):
    response = client.get("/projeto/1/listar")
    body = response.json()  # Se precisar printar o Body para visualizar
    assert response.status_code == 200


def test_projetos_criados(client: TestClient):
    response = client.get("/projeto/1/listar-criados")
    body = response.json()  # Se precisar printar o Body para visualizar
    assert response.status_code == 200


def test_infos_projetos(client: TestClient):
    response = client.get("/projeto/1")
    body = response.json()  # Se precisar printar o Body para visualizar
    assert response.status_code == 200


def test_get_etapas(client: TestClient):
    response = client.get("/etapa/1/listar-etapas")
    body = response.json()  # Se precisar printar o Body para visualizar
    assert response.status_code == 200


def test_get_tarefas(client: TestClient):
    response = client.get("/tarefas/1/3")
    body = response.json()  # Se precisar printar o Body para visualizar
    assert response.status_code == 200