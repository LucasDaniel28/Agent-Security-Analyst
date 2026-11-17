# Fundamentos de Cibersegurança

Este material orienta análises didáticas e defensivas. As definições devem ser aplicadas considerando o contexto do ativo, do negócio e do escopo autorizado.

## Conceitos essenciais

- **Ativo:** dado, serviço, aplicação, dispositivo ou recurso que possui valor para uma organização.
- **Ameaça:** circunstância ou agente capaz de causar dano a um ativo.
- **Vulnerabilidade:** fraqueza técnica, processual ou humana que pode ser explorada por uma ameaça.
- **Exploração:** ação que utiliza uma vulnerabilidade. Sua demonstração deve ocorrer apenas em ambiente autorizado.
- **Risco:** combinação contextualizada entre possibilidade de um evento e suas consequências.
- **Impacto:** efeito sobre operações, pessoas, dados, conformidade ou reputação.
- **Probabilidade:** estimativa da chance de o cenário ocorrer, considerando exposição, controles e capacidade do agente de ameaça.
- **Mitigação:** medida que reduz probabilidade, impacto ou ambos.
- **Risco residual:** risco que permanece depois da aplicação dos controles.

Uma vulnerabilidade não significa automaticamente risco crítico. Exposição, pré-condições, privilégios, controles existentes e valor do ativo influenciam a avaliação.

## Tríade CIA

| Pilar | Objetivo | Exemplo de falha |
|---|---|---|
| Confidencialidade | Impedir acesso não autorizado à informação | Exposição de dados de clientes |
| Integridade | Evitar alteração ou destruição indevida | Modificação de registros financeiros |
| Disponibilidade | Manter sistemas e dados acessíveis quando necessários | Interrupção de serviço |

Uma mesma falha pode afetar mais de um pilar.

## Controles de segurança

- **Preventivos:** reduzem a chance de ocorrência (validação de entrada, menor privilégio, autenticação forte).
- **Detectivos:** identificam eventos (logs, alertas, monitoramento).
- **Corretivos:** restauram ou corrigem (patches, recuperação de backup, resposta a incidentes).
- **Compensatórios:** reduzem risco quando o controle ideal não pode ser aplicado imediatamente.

Defesa em profundidade combina controles independentes. Nenhum controle isolado garante proteção total.

## SQL Injection

SQL Injection ocorre quando dados controlados pelo usuário são incorporados à estrutura de uma consulta SQL, permitindo que a entrada altere a lógica pretendida da instrução.

**Causa comum:** construir SQL por concatenação de strings.

**Prevenção prioritária:**
1. Usar consultas parametrizadas/prepared statements.
2. Evitar montar comandos SQL concatenando entrada.
3. Aplicar privilégio mínimo à conta do banco.
4. Validar tipos, formatos e regras de negócio (validação não substitui parametrização).
5. Não expor mensagens internas de erro ao usuário.
6. Registrar eventos de forma segura, sem armazenar segredos.

Referências: [CWE-89](https://cwe.mitre.org/data/definitions/89.html) e [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).

## Priorização de vulnerabilidades

Considere pelo menos:
- impacto em confidencialidade, integridade e disponibilidade;
- exposição e acessibilidade do ativo;
- pré-condições e complexidade;
- privilégios exigidos;
- presença de controles compensatórios;
- facilidade de detecção e exploração;
- criticidade do negócio e sensibilidade dos dados.

O CVSS é uma referência padronizada para caracterizar severidade técnica. Ele não substitui a análise contextual de risco. Registre versão, vetor e justificativa quando utilizar uma pontuação.

## Referenciais

- **OWASP Top 10:** categorias de riscos relevantes para aplicações web.
- **OWASP WSTG:** guia de testes de segurança de aplicações web.
- **CWE:** catálogo de tipos comuns de fraquezas.
- **CVSS:** sistema de pontuação de severidade de vulnerabilidades.
- **NIST CSF:** estrutura para governar, identificar, proteger, detectar, responder e recuperar.
- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas observadas em atividades adversárias. Deve ser usada para entendimento e defesa, não como autorização para executar técnicas.

## Boas práticas operacionais

- Definir escopo e autorização por escrito.
- Preferir laboratório isolado e dados fictícios.
- Fazer backup antes de mudanças.
- Planejar janela, limites e reversão.
- Usar contas com privilégio mínimo.
- Manter sistemas e dependências atualizados.
- Proteger segredos e informações pessoais.
- Centralizar logs e revisar alertas.
- Documentar evidências sem expor dados sensíveis.
- Retestar após a correção e acompanhar risco residual.
