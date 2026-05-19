# say-once

> Книга о том, как сказать один раз — и быть понятым.
> Say it once. Be understood.

[Русский](#русский) · [English](#english)

---

## Русский

Люди всегда передавали информацию неточно — и платили за это переспросами, переделками, потерянным временем. Мы привыкли и считаем нормой.

Сегодня задачи всё чаще выполняют ИИ-агенты. Они не переспрашивают — они делают. Цена неточной формулировки резко выросла.

Эта книга — про навык передавать информацию так, чтобы получатель мог действовать сразу и правильно. Неважно кто это: коллега, пользователь интерфейса или агент.

### Где это работает

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

### С чего начать

Книга устроена слоями — от короткой шпаргалки до сырых заметок. Заходи на свой уровень:

| У тебя есть | Иди сюда |
|---|---|
| 2 минуты | [`cheatsheet.md`](cheatsheet.md) — все правила и границы одной страницей |
| 20 минут | [`rules.md`](rules.md) — каждое правило подробно, с признаком нарушения и границами применимости |
| 5 минут после | [`limits.md`](limits.md) — шесть семейств: когда правила не работают |
| Хочешь увидеть систему целиком | [`map.md`](map.md) — связи правил: семьи, пары, архетипы, стадии задачи, роли |
| Любишь читать первоисточники | [`examples/`](examples/) — живые кейсы, на которых правила выведены |
| Хочешь смежное | [`references.md`](references.md) — Грайс, Норман, Розенберг, ШСМ и другие |

### Контрибьютору

- Хочешь дописать книгу — [`AGENTS.md`](AGENTS.md) (правила и шаблоны для агентов и людей)
- Хочешь увидеть процесс на практике — [`WRITING_WITH_CLAUDE.md`](WRITING_WITH_CLAUDE.md)
- Сырые мысли, идеи будущих правил — [`thoughts.md`](thoughts.md)

---

## English

People have always conveyed information imprecisely — and always paid for it with re-asking, redoing, lost time. We've grown used to it and consider it normal.

Today, tasks are increasingly performed by AI agents. They don't ask again — they just do. The cost of an imprecise formulation has sharply increased.

This book is about the skill of delivering information so the receiver can act immediately and correctly. It doesn't matter who they are: a colleague, a user of an interface, or an agent.

### Where this applies

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

### Where to start

The book is layered, from a short cheatsheet to raw notes. (Most content is in Russian; English translation is upcoming.)

| You have | Go here |
|---|---|
| 2 minutes | [`cheatsheet.md`](cheatsheet.md) — all rules and limits on one page |
| 20 minutes | [`rules.md`](rules.md) — each rule with its violation signal and applicability limits |
| 5 minutes more | [`limits.md`](limits.md) — six families of cases where the rules don't apply |
| Want to see the whole system | [`map.md`](map.md) — rule families, pairs, archetypes, lifecycle, roles |
| Want primary sources | [`examples/`](examples/) — real-life cases that produced the rules |
| Want related reading | [`references.md`](references.md) — Grice, Norman, Rosenberg, and more |

### For contributors

- [`AGENTS.md`](AGENTS.md) — rules and templates for AI and human contributors (in Russian).
- [`WRITING_WITH_CLAUDE.md`](WRITING_WITH_CLAUDE.md) — typical workflow and a sample dialogue (in Russian).

---

## License

TBD
