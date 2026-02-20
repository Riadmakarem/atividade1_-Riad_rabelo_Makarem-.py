# lista de alunos
alunos = [
	{"nome": "Brendo", "email": "brendo.matos@ciesa.br", "idade": 32, "curso": "CCP"},
	{"nome": "Eva", "email": "eva@ciesa.br", "idade": 15, "curso": "ADS"},
	{"nome": "Ed", "email": "ed@ciesabr", "idade": 12, "curso": "DIR"},
	{"nome": "Joao", "email": "joao@cies.abr", "idade": 18, "curso": "ADS"},
]

# lista de cursos disponíveis
cursos_disponiveis = ["CCP", "ADS", "IA", "EGC"]

def validar_alunos(alunos, cursos_disponiveis):
	alunos_validos = []
	alunos_invalidos = []
	for aluno in alunos:
		motivos = []
		# nome
		if len(aluno["nome"]) < 3:
			motivos.append("Nome com menos de 3 caracteres")
		# email
		email = aluno["email"]
		if "@" not in email or "." not in email[email.index("@"):]:
			motivos.append("Email inválido")
		# idade
		if aluno["idade"] < 16:
			motivos.append("Idade menor que 16 anos")
		# curso
		if aluno["curso"] not in cursos_disponiveis:
			motivos.append("Curso não disponível")
		if motivos:
			alunos_invalidos.append({"nome": aluno["nome"], "motivos": motivos})
		else:
			alunos_validos.append(aluno)
	return alunos_validos, alunos_invalidos

# Exemplos:
alunos_validos, alunos_invalidos = validar_alunos(alunos, cursos_disponiveis)
print("Alunos válidos:", alunos_validos)
print("Alunos inválidos:", alunos_invalidos)
