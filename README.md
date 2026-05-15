# say-once

> Книга о том, как сказать один раз — и быть понятым.
> Say it once. Be understood.

[Русский](#русский) · [English](#english)

---

## Русский

### О чём это

Люди всегда передавали информацию неточно — и всегда за это платили: переспрашивали, переделывали, теряли время. Мы к этому привыкли и считаем нормой.

Сегодня задачи всё чаще выполняют ИИ-агенты. Они не переспрашивают — они делают. И цена неточной формулировки резко выросла.

Эта книга — про навык передавать информацию так, чтобы получатель мог действовать сразу и правильно. Неважно кто это: коллега, пользователь интерфейса или агент.

### Где работают эти правила

Правила одни и те же. Контекстов — три:

```
                  ┌──────────────────────────┐
                  │         ПРАВИЛА          │
                  └─────────────┬────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
       ▼                        ▼                        ▼

  ЧЕЛОВЕК ↔ ЧЕЛОВЕК       ЧЕЛОВЕК ↔ UI            ЧЕЛОВЕК ↔ АГЕНТ
  ─────────────────       ─────────────           ─────────────────
  чат, встречи,           сообщения               промпты,
  письма, задачи          об ошибках,             задачи для агента,
                          формы,                  инструкции,
                          уведомления             контексты
```

Правила не меняются. Меняется **цена ошибки**:

- **Человек ↔ человек:** переспрос, переделка, потеря времени. Привычно, терпимо.
- **Человек ↔ UI:** пользователь не понял, не нашёл, ушёл. Терпимо до конкурента.
- **Человек ↔ агент:** агент не переспросит. Он сделает не то, и ты узнаешь по результату.

В агентном мире эти правила перестают быть «хорошим тоном» — без них агент просто не выдаст нужный результат.

### Как устроен репозиторий

- [`preface.md`](preface.md) — предисловие
- [`rules.md`](rules.md) — свод правил, пополняется по мере накопления примеров
- [`map.md`](map.md) — карта правил: семейства, пары «отправитель ↔ получатель», архетипы
- [`examples/`](examples/) — реальные кейсы из жизни, на которых выведены правила
- [`thoughts.md`](thoughts.md) — необработанные мысли и заметки
- [`references.md`](references.md) — смежное чтение: книги, статьи, каналы по теме

### Как пополняется

Книга строится снизу вверх: сначала реальные примеры неудачной коммуникации, потом извлечение принципов. В `bot/` лежит Telegram-бот для сбора примеров на ходу.

### Как писать книгу вместе с ИИ-агентом

- [`AGENTS.md`](AGENTS.md) — инструкции для агентов: структура, шаблоны, тон, что можно и что нельзя.
- [`WRITING_WITH_CLAUDE.md`](WRITING_WITH_CLAUDE.md) — типовой воркфлоу и пример диалога с Claude.

---

## English

### What it's about

People have always conveyed information imprecisely — and always paid for it: asking again, redoing work, losing time. We've grown used to it and consider it normal.

Today, tasks are increasingly performed by AI agents. They don't ask again — they just do. And the cost of an imprecise formulation has sharply increased.

This book is about the skill of delivering information so the receiver can act immediately and correctly. It doesn't matter who they are: a colleague, a user of an interface, or an agent.

### Where these rules apply

The rules are the same. The contexts are three:

```
                  ┌──────────────────────────┐
                  │          RULES           │
                  └─────────────┬────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
       ▼                        ▼                        ▼

   HUMAN ↔ HUMAN            HUMAN ↔ UI              HUMAN ↔ AGENT
   ──────────────           ───────────             ───────────────
   chat, meetings,          error messages,         prompts,
   emails, tasks            forms,                  task briefs,
                            notifications           instructions,
                                                    context windows
```

The rules don't change. What changes is the **cost of breaking them**:

- **Human ↔ human:** asking again, redoing, lost time. Familiar, tolerable.
- **Human ↔ UI:** the user doesn't get it, doesn't find it, leaves. Tolerable until a competitor.
- **Human ↔ agent:** the agent won't ask again. It will do the wrong thing, and you'll learn about it from the result.

In the agent world, these rules stop being good manners — without them, the agent simply won't deliver what you need.

### Repository layout

- [`preface.md`](preface.md) — preface (in Russian)
- [`rules.md`](rules.md) — accumulated rules, grows as new examples come in
- [`map.md`](map.md) — rule map: families, sender ↔ receiver pairs, archetypes (in Russian)
- [`examples/`](examples/) — real-life cases from which the rules are derived
- [`thoughts.md`](thoughts.md) — raw thoughts and notes
- [`references.md`](references.md) — related reading: books, articles, channels (in Russian)

### How it grows

The book is built bottom-up: real examples of failed communication first, then principles extracted from them. The `bot/` directory contains a Telegram bot for collecting examples on the go.

### Writing with an AI agent

- [`AGENTS.md`](AGENTS.md) — agent instructions: structure, templates, tone, dos and don'ts (in Russian).
- [`WRITING_WITH_CLAUDE.md`](WRITING_WITH_CLAUDE.md) — typical workflow and sample dialogue with Claude (in Russian).

---

## License

TBD
