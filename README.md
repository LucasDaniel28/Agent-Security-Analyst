# Agent Security Analyst

> Agente mentor de cibersegurança para análise de vulnerabilidades, avaliação de riscos e orientação de correções em ambientes autorizados.

O **Agent Security Analyst** é uma especialização do projeto-base [DIO Agent](https://github.com/digitalinnovationone/dio-agent). Seu foco é ajudar estudantes e profissionais em formação a compreender vulnerabilidades, validar riscos de maneira controlada e priorizar medidas de mitigação.

## Objetivos

- Explicar conceitos de segurança com exemplos práticos.
- Analisar vulnerabilidades com contexto, evidências, impacto e recomendações.
- Priorizar riscos considerando probabilidade e impacto, sem tratar uma pontuação isolada como verdade absoluta.
- Ensinar práticas defensivas alinhadas a referências reconhecidas.
- Exigir contexto, autorização e escopo antes de orientar testes ou comandos que possam afetar sistemas.

## Escopo e uso responsável

Use este projeto somente em aplicações próprias, laboratórios isolados ou sistemas para os quais exista autorização explícita. O agente deve confirmar, antes de orientar uma avaliação técnica:

1. Qual é o ativo e quem é seu responsável?
2. O ambiente é local, homologação ou produção?
3. Você tem autorização para testar esse ativo?
4. Qual é o escopo permitido e quais ações estão proibidas?
5. Há janela de teste, backup e plano de reversão?

Sem essas informações, deve limitar-se à explicação conceitual e a alternativas seguras. Não deve sugerir exploração de terceiros, persistência, evasão, exfiltração ou interrupção de serviços.

## Estrutura

```text
Agent-Security-Analyst/
├── AGENTS.md
├── README.md
├── agent/
│   ├── persona.md
│   └── knowledge/
│       └── cybersecurity-foundations.md
├── skills/
│   ├── README.md
│   └── vulnerability-analysis/
│       ├── SKILL.md
│       └── README.md
├── lab/
│   └── sql_injection/
│       ├── app.py
│       └── test_app.py
└── docs/
    └── validation-guide.md
```

## Como utilizar o agente

Abra a pasta do repositório em um harness compatível com instruções `AGENTS.md`, como Claude Code, Codex, OpenCode ou outro ambiente compatível. O harness deve carregar as instruções do projeto. Leia também:

- [Persona](agent/persona.md)
- [Fundamentos de cibersegurança](agent/knowledge/cybersecurity-foundations.md)
- [Skill de análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md)

### Exemplos de solicitação

**Análise inicial**
```text
Quero analisar uma vulnerabilidade em uma aplicação que desenvolvo.
Ajude-me a definir escopo, evidências, impacto e plano de correção.
```

**SQL Injection em laboratório local**
```text
Quero executar o laboratório local de SQL Injection deste repositório,
entender por que a consulta vulnerável falha e validar a correção.
```

**Servidor Ubuntu**
```text
Tenho um servidor Ubuntu em laboratório e quero revisar sua exposição.
Antes de sugerir comandos, confirme comigo autorização, escopo,
versão, serviços envolvidos e se o ambiente pode sofrer indisponibilidade.
```

## Laboratório de SQL Injection

O laboratório usa somente Python e SQLite da biblioteca padrão. Ele demonstra uma consulta vulnerável por concatenação de strings e a versão corrigida com parâmetros SQL. Não há alvo externo nem necessidade de rede.

Requisitos: Python 3.10 ou superior.

Execute na raiz do repositório:

```bash
python -m unittest discover -s lab/sql_injection -v
```

O teste comprova que a consulta vulnerável pode retornar registros além do esperado e que a consulta parametrizada trata a entrada como dado. O laboratório é didático; não representa uma varredura automatizada de aplicações reais.

Para executar a demonstração diretamente:

```bash
python lab/sql_injection/app.py
```

## Processo de análise recomendado

1. Confirmar autorização e escopo.
2. Identificar ativo, tecnologia, versão e contexto.
3. Reunir evidências reproduzíveis sem expor dados sensíveis.
4. Descrever causa raiz e cenário de impacto.
5. Avaliar severidade considerando impacto e probabilidade.
6. Recomendar correção priorizada e controles compensatórios.
7. Revalidar a correção e registrar limitações.

## Referências técnicas

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)
- [CVSS](https://www.first.org/cvss/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Validação do desafio

O roteiro completo de validação, incluindo o cenário de servidor Ubuntu e os critérios de evidência, está em [docs/validation-guide.md](docs/validation-guide.md).

> Registre os resultados reais dos testes e adicione capturas de tela próprias. Não declare uma varredura, validação em servidor ou teste externo como concluído sem executar a atividade e guardar evidências.


