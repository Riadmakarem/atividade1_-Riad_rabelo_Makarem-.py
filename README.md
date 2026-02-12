# Repositório de atividades de Programação em Python II


## Instrução aos alunos
- A atividades devem ser commitadas em seus respectivos diretórios;
- O padrão do nome do arquivo deve ser: `atividadeX_<nome_do_aluno>.py`;
- Uma PR deve ser aberta e comentada/respondida na atividade correspondente no Classrrom (https://classroom.google.com/c/ODQ0MTEzMTUwMDM1?cjc=wn3z536f);

## Atividades

### Atividade 1 - Listas e Dicionários
- Crie uma lista de alunos contendo: nome, email, idade e sigla do curso;
E.G: 
````json
[
  {"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
  {"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
  {"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
  {"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]
````
- Crie uma lista de cursos disponíveis contendo a sigla;
````python
["CCP", "ADS", "IA", "EGC"]
````
- Crie uma função que receba a lista de alunos e valide segundo os seguintes critérios:
   - O nome deve conter pelo menos 3 caracteres;
   - O email deve conter um "@" e um ".";
   - A idade deve ser maior ou igual a 16 anos;
   - A sigla do curso deve existir no dicionário de cursos disponíveis;
- A função deve retornar uma lista de alunos válidos e uma lista de alunos inválidos, juntamente com a lista de motivos da invalidação.