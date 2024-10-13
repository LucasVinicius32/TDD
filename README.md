# Tarefa de TDD com Python

Este projeto implementa testes unitários utilizando a técnica de **Test Driven Development (TDD)** para validar as classes `Employee`, `Person`, `PersonDAO` e `SalaryCalculator`.

## Pré-requisitos

- **Python 3.10** ou superior
- **unittest**, que é o framework de testes unitários embutido no Python



## Instalação

1. Clone o repositório em sua máquina local:
    ```bash
    git clone https://github.com/LucasVinicius32/TDD.git
    cd repositorio
    ```

2. Crie e ative um ambiente virtual para o projeto:
    ```bash
    python -m venv venv
    source venv/bin/activate    # No Windows: venv\Scripts\activate
    ```

3. Certifique-se de estar na pasta raiz do projeto antes de rodar os testes:
    ```bash
    cd project
    ```

## Executando os Testes

 maneiras principais de rodar os testes:

### 1. Rodar Todos os Testes

utilizar o comando `unittest discover`:

```bash
python -m unittest discover -s tests
```

## Saída Esperada

Saida: 
```bash
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```