# Teste back-end Biome-hub

Implementar uma TODO List utilizando Python, Django e outras bibliotecas/tecnologias que achar necessário.

**FEITOS**
- Possibilidade de criar uma nova conta, realizar login e recuperação de senha;
- CRUD de TODO Lists: criar, remover, editar o título;
- CRUD de tarefas: para cada TODO List, possibilidade de criar tarefas, editar, remover, marcar com concluída e adicionar uma deadline;
- Possibilidade de atribuir uma tarefa para um usuário;

**NÃO FIZ**
- Relatório diário via e-mail de tarefas concluídas naquele dia e próximas prioridades, baseado no deadline;
- Possibilidade de solicitar um relatório, enviando a data de início e fim, em um endpoint REST com autenticação utilizando token. A resposta do endpoint deve ser imediata, informando se é possível a geração do relatório e, se sim, para qual e-mail será enviado. A geração e envio via e-mail deve acontecer de forma assíncrona (em background);
- Possibilidade de fazer login no usuário `admin@biome-hub.com`, onde seu password será `xxyyzz` onde `xx` será o dobro do dia atual, `yy` será o dobro do mês e `zz` a hora atual (sempre 6 caracteres);


Para rodar o projeto:

``
python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
``

ou


``
docker-compose up
``