def notas(*n,sit=False):
    """
    -> Função para analisar notas e sitações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    maior=menor=c=media=0
    dados=dict()
    while c<len(n):
        if c==0 or n[c]<menor:
            menor=n[c]
        if n[c]>maior:
            maior=n[c]
        media+=n[c]
        c+=1
    media/=len(n)
    if media>=7:
        situacao='APROVADO'
    elif media>=5:
        situacao='RECUPERAÇÃO'
    else:
        situacao='REPROVADO'
    dados['Total']=len(n)
    dados['Maior']=maior
    dados['Menor']=menor
    dados['Média']=f'{media:.2f}'
    if sit:
        dados['Situação']=situacao
        return dados
    else:
        return dados

print(notas(7,8,9,sit=True))
help(notas)