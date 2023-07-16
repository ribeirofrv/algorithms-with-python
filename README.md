# Projeto de Resolução de Problemas e Otimização de Algoritmos

Este projeto foi desenvolvido durante o módulo de Introdução à Ciência da Computação do curso de Desenvolvimento Web da Trybe. O objetivo do projeto foi resolver problemas e otimizar algoritmos, desenvolvendo a capacidade de implementar soluções para diversos problemas do dia a dia.

Durante este projeto, foram exercitadas as seguintes habilidades:

- Lógica de programação;
- Capacidade de interpretação de problemas;
- Capacidade de interpretação de um código legado;
- Capacidade de otimização da resolução de problemas;
- Resolução de problemas e otimização de algoritmos sob pressão.

O projeto foi realizado utilizando a versão 3.10.6 do Python. Para garantir a compatibilidade e evitar conflitos entre diferentes projetos e bibliotecas, foi utilizado o recurso de ambiente virtual do Python.

## Configuração do Ambiente Virtual

Para configurar o ambiente virtual, siga os passos abaixo:

1. Crie o ambiente virtual executando o seguinte comando:

```bash
$ python3 -m venv .venv
```

2. Ative o ambiente virtual com o seguinte comando:

```bash
$ source .venv/bin/activate
```

3. Instale as dependências do projeto no ambiente virtual com o seguinte comando:

```bash
$ python3 -m pip install -r dev-requirements.txt
```

Certifique-se de ativar o ambiente virtual sempre que estiver trabalhando no projeto. Para desativar o ambiente virtual, execute o comando "deactivate".

O arquivo `dev-requirements.txt` contém todas as dependências necessárias para o projeto.

## Executando os Testes

Certifique-se de que o ambiente virtual está ativado antes de executar os testes.

Para executar os testes, utilize o seguinte comando:

```bash
$ python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o pytest. No entanto, se você tiver problemas com a configuração padrão e quiser uma saída mais completa, execute o seguinte comando:

```bash
$ python3 -m pytest -s -vv
```

Se precisar executar apenas um arquivo de testes específico, utilize o seguinte comando:

```bash
$ python3 -m pytest tests/nome_do_arquivo.py
```

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com melhorias para este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.
2. Crie um branch com sua feature/correção: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Minha nova feature'`.
4. Push para o branch criado: `git push origin minha-feature`.
5. Abra um Pull Request.
