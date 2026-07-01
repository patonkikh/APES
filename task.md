# AI Product Engineering Skills Platform (APES)

> Бизнес-требования (BRD) и техническое задание (SRS)

---

# 1. Описание проекта

## Название

**AI Product Engineering Skills Platform (APES)**

Рабочее название.

---

# 2. Цель проекта

Разработать крупнейшую открытую библиотеку профессиональных Engineering Skills для современных AI-агентов.

Платформа должна предоставлять Skills, которые помогают выполнять реальные инженерные задачи по стандартизированным методологиям, а не просто генерируют текст по запросу.

Каждый Skill представляет собой законченную методику выполнения одной профессиональной задачи.

Проект ориентирован на использование в:

- Cursor
- Claude Code
- LobeHub
- Cline
- Roo Code
- GitHub Copilot
- OpenAI Agents
- Windsurf
- других агентных IDE

---

# 3. Проблема рынка

Большинство существующих Skills:

- являются обычными промптами;
- используют Role Play ("You are...");
- не описывают процесс принятия решений;
- не проверяют собственный результат;
- не используют профессиональные методологии;
- не выявляют ошибки;
- не содержат критериев качества;
- не предназначены для Enterprise-разработки.

Такие Skills подходят для генерации текста, но не для выполнения инженерной работы.

---

# 4. Концепция проекта

Основная идея проекта — заменить подход "Role Prompt" на "Engineering Playbook".

Каждый Skill описывает:

- как эксперт решает задачу;
- какие этапы необходимо пройти;
- какие проверки необходимо выполнить;
- какие ошибки необходимо искать;
- какой результат считается качественным.

Skill не играет роль.

Skill реализует процесс.

---

# 5. Основные принципы

Каждый Skill должен:

- решать только одну задачу;
- использовать инженерную методологию;
- работать последовательно;
- выполнять внутреннюю проверку результата;
- использовать измеримые критерии качества;
- формировать стандартизированный результат;
- рекомендовать следующий Skill в цепочке разработки.

---

# 6. Формат распространения

Каждый Skill распространяется как один файл:

skill.md

Это обеспечивает полную совместимость со всеми существующими каталогами Skills.

Дополнительная документация размещается только в репозитории.

Пользователь устанавливает исключительно файл skill.md.

---

# 7. Структура репозитория

skills/

    product/

        prd-generator/

            skill.md

            README.md

    architecture/

    rag/

    security/

    ai/

    jira/

    enterprise/

    startup/

---

# 8. Требования к skill.md

Каждый Skill представляет собой единый Markdown-файл.

Внутри файла допускаются следующие логические разделы.

# Purpose

Что выполняет Skill.

---

# Workflow

Последовательность действий.

---

# Decision Rules

Правила принятия решений.

---

# Validation

Как проверить качество результата.

---

# Anti-patterns

Типичные ошибки.

---

# Best Practices

Лучшие практики.

---

# Output Structure

Структура результата.

---

# Next Skills

Какие Skills рекомендуется использовать далее.

Запрещается использовать платформозависимый синтаксис.

---

# 9. Общие требования к Skills

Каждый Skill обязан:

- не использовать Role Play;
- не использовать "You are...";
- не использовать вымышленные роли;
- не предполагать неизвестные данные без явного указания;
- выявлять противоречия;
- проверять полноту результата;
- использовать лучшие инженерные практики;
- учитывать безопасность;
- учитывать масштабируемость;
- учитывать сопровождаемость.

---

# 10. Каталог Skills

## Product

### Discovery

- Idea Validator
- Problem Statement Builder
- Customer Interview Planner
- JTBD Interview Generator
- Persona Generator
- Product Discovery Assistant
- User Research Analyzer
- Opportunity Solution Tree
- Product Hypothesis Builder
- Value Proposition Designer

### Strategy

- Product Vision Builder
- Product Strategy Advisor
- Product Roadmap Generator
- OKR Builder
- KPI Generator
- North Star Metric Advisor
- Feature Prioritization
- Competitor Analyzer
- Market Gap Analyzer
- Product Risk Analyzer

### Delivery

- PRD Generator
- Epic Generator
- User Story Generator
- Story Mapping
- Acceptance Criteria Generator
- Sprint Planner
- Release Planner
- Changelog Generator
- Product Documentation Generator
- Stakeholder Update Generator

---

## Business Analysis

- Business Requirements Generator
- Functional Requirements Generator
- Non Functional Requirements Generator
- Use Case Generator
- BPMN Assistant
- Business Rules Validator
- Process Optimizer
- Gap Analysis
- Requirements Reviewer
- Traceability Matrix Builder

---

## Architecture

- Solution Architecture
- Architecture Review
- ADR Generator
- System Context Builder
- Container Diagram Builder
- Component Diagram Builder
- API Designer
- Integration Planner
- Data Flow Analyzer
- Scalability Advisor

---

## Software Engineering

- Monolith Split Advisor
- Microservice Advisor
- Event Driven Architecture
- CQRS Advisor
- DDD Assistant
- Database Review
- API Review
- Technical Debt Analyzer
- Refactoring Advisor
- Performance Review

---

## AI Engineering

- AI Solution Architect
- Prompt Engineer
- Prompt Reviewer
- Prompt Optimizer
- Context Engineering
- Multi-Agent Planner
- AI Workflow Builder
- AI Evaluation Builder
- AI Cost Optimizer
- AI Latency Optimizer

---

## RAG

- RAG Architecture Designer
- Chunking Strategy Advisor
- Embedding Strategy Advisor
- Retriever Optimizer
- Hybrid Search Advisor
- Query Rewriter
- Context Optimizer
- Metadata Optimizer
- Citation Validator
- Hallucination Analyzer
- Retrieval Evaluator
- Benchmark Generator
- Knowledge Gap Detector
- Synthetic Dataset Generator
- RAG Performance Advisor

---

## AI Security

- Prompt Injection Detector
- Prompt Leak Detector
- Jailbreak Analyzer
- AI Threat Modeling
- AI Risk Assessment
- Secure Prompt Generator
- Guardrails Builder
- Secret Detector
- PII Leakage Detector
- OWASP LLM Reviewer
- AI Governance Advisor
- Trust Boundary Analyzer
- Secure Context Builder
- Compliance Checker
- AI Red Team Assistant

---

## MCP

- MCP Server Generator
- MCP Client Generator
- MCP Tool Generator
- MCP Registry Builder
- MCP Testing Assistant
- MCP Security Review
- MCP Performance Review
- MCP Documentation Generator
- MCP Deployment Advisor
- MCP Best Practices

---

## Jira

- Epic Planner
- Story Generator
- Acceptance Criteria Reviewer
- Duplicate Issue Detector
- Sprint Health Analyzer
- Dependency Analyzer
- Bug Root Cause Analyzer
- Story Point Advisor
- Backlog Grooming Assistant
- Release Readiness Checker

---

## Enterprise

- Enterprise Architecture Review
- Business Capability Mapping
- Security Architecture Review
- Integration Architecture
- Risk Register Builder
- Compliance Documentation
- Data Governance Advisor
- Migration Planner
- Enterprise AI Readiness
- Cloud Adoption Advisor

---

## Startup

- Startup Idea Validator
- AI SaaS Planner
- MVP Planner
- Pricing Strategy Advisor
- Product Market Fit Evaluator
- Investor Pitch Builder
- GTM Strategy Builder
- Unit Economics Advisor
- Competitive Analysis
- Growth Planner

---

## GitHub

- README Generator
- GitHub Project Planner
- Issue Generator
- Pull Request Reviewer
- Release Manager
- Semantic Version Advisor
- OSS Maintainer Assistant
- Documentation Reviewer
- Contribution Guide Builder
- Community Manager

---

# 11. Требования к качеству

Каждый Skill обязан:

- выполнять логическую проверку результата;
- выявлять противоречия;
- выявлять неоднозначности;
- выявлять пропущенные зависимости;
- выявлять отсутствующие входные данные;
- проверять полноту результата;
- предлагать улучшения.

---

# 12. Требования к разработке проекта

Разработка платформы должна выполняться поэтапно.

Приоритет разработки:

1. Product
2. Architecture
3. AI
4. RAG
5. AI Security
6. MCP
7. Jira
8. Enterprise
9. Startup
10. GitHub

Каждый Skill разрабатывается независимо и проходит ревью перед публикацией.

---

# 13. Инструкции AI-агенту разработки

Все работы над проектом должны выполняться последовательно.

Перед началом любой задачи AI-агент обязан:

1. Изучить README.md.
2. Изучить Roadmap.md.
3. Изучить TODO.md.
4. Изучить каталог docs/.
5. Определить текущее состояние проекта.
6. Составить краткий план реализации.
7. Определить изменяемые файлы.
8. Оценить влияние изменений на существующую структуру.

Во время разработки агент обязан:

- вносить минимально необходимые изменения;
- соблюдать единый стиль проекта;
- не создавать дублирование;
- не нарушать совместимость ранее созданных Skills;
- использовать существующие шаблоны и соглашения.

После завершения каждой задачи агент обязан:

- обновить README.md при необходимости;
- обновить Roadmap.md;
- обновить TODO.md;
- обновить CHANGELOG.md;
- актуализировать документацию в docs/;
- проверить связанные Skills на необходимость изменений.

Если изменение затрагивает архитектуру проекта, агент обязан обновить:

- Architecture.md;
- ADR (Architecture Decision Records).

Документация считается частью продукта. Любое изменение функциональности без соответствующего обновления документации считается незавершенной задачей.

---

# 14. Дорожная карта

## Этап 1

- разработка архитектуры платформы;
- создание стандартов Skills;
- публикация первых 10 Skills.

## Этап 2

- расширение библиотеки до 50 Skills;
- публикация в основных каталогах;
- сбор обратной связи.

## Этап 3

- расширение до 100 Skills;
- покрытие основных инженерных направлений;
- формирование единого стандарта Engineering Playbooks.

## Этап 4

- более 250 Skills;
- отраслевые библиотеки;
- локализация;
- автоматическая генерация новых Skills на основе единого шаблона.

---

# 15. Критерии успешности проекта

Проект считается успешным, если:

- создана библиотека не менее чем из 100 профессиональных Skills;
- все Skills используют единый стандарт Engineering Playbook;
- каждый Skill совместим с основными агентными IDE без модификации;
- библиотека покрывает полный жизненный цикл разработки программного продукта: от исследования идеи до сопровождения и эксплуатации;
- качество Skills превосходит типовые промпты за счет использования инженерных методологий, правил принятия решений, встроенной валидации и стандартизированных выходных артефактов.
