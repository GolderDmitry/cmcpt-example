# Notion Sync — пример CMCPT для Runturu

Минимальный проект MCP-сервера для каталога Runturu: манифест `runturu-mcp.json`,
Dockerfile и сервер на FastAPI.

## Как загрузить

1. Подключите MCP-агента разработчика: `https://runturu.com/dev/<ваш-slug>/mcp`.
2. Попросите агента: «проверь https://github.com/GolderDmitry/cmcpt-example».
3. Агент клонирует репозиторий в карантин, прогонит проверки и создаст черновик.
4. Администратор увидит отчёт и активирует шаблон.

## Требования

- `runturu-mcp.json`, `Dockerfile`, `README.md`, `server/` или `main.py`;
- контейнер слушает 8080, MCP — `/mcp`, health — `/health`;
- egress только по `permissions.network`;
- секреты не хранятся в коде.
