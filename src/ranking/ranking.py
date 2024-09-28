''' Os dados viriam assim:

aluno = ler_arquivo_json('exemplo_aluno.json')
bd = ler_arquivo_json('exemplo_base_de_dados.json')
'''


def eh_primeiro(aluno, outro_aluno, disciplina):
    if (aluno['curso'] != outro_aluno['curso']):
        if (aluno['curso'] == disciplina['CURSO']):
            return 0  # O atual é antes, não soma
        if (outro_aluno['curso'] == disciplina['CURSO']):
            return 1  # O outro é antes, soma

        # Se um dos dois está no turno correto
        if (aluno['curso'][-1] != outro_aluno['curso'][-1]):
            if (aluno['curso'][-1] == disciplina['CURSO'][-1]):
                return 0  # O atual é antes, não soma
            if (outro_aluno['curso'][-1] == disciplina['CURSO'][-1]):
                return 1  # O outro é antes, soma

    if (aluno['creditos'] > outro_aluno['creditos']):
        return 0  # O atual é antes, não soma
    elif (aluno['creditos'] < outro_aluno['creditos']):
        return 1  # O outro é antes, soma

    if (aluno['cr'] > outro_aluno['cr']):
        return 0  # O atual é antes, não soma
    elif (aluno['cr'] < outro_aluno['cr']):
        return 1  # O outro é antes, soma

    return 1  # Se empatar, vamos supor que o outro é antes


def tem_disciplina(aluno, disciplina):
    for d in aluno['grade']:
        if d['NOME'] == disciplina['NOME']:
            return True
    return False


def achar_ranking(aluno, bd):
    posições = []
    for disciplina in aluno['grade']:
        ranking = 1
        quantidade = 1
        for outro_aluno in bd:
            if tem_disciplina(outro_aluno, disciplina):
                ranking += eh_primeiro(aluno, outro_aluno, disciplina)
                quantidade += 1
        posições.append((disciplina['NOME'], ranking, quantidade))
    return posições
