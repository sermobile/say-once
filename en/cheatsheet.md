# Cheatsheet

> This file is for you if you have 2 minutes — and want to see everything on one page.

The book is about delivering information so it doesn't need to be asked twice. Numbers below match [`../ru/rules.md`](../ru/rules.md) (full rules are still in Russian for now).

> Rule numbers are canonical — they appear in `rules.md` in the order they were discovered. The grouping here is by meaning, so numbers within each section won't run consecutively (e.g. "1, 3, 8, 15"). Related rules sit together instead of being scattered across a flat list of 18.

---

## 18 rules

### What goes in one message

- **1. Ready-to-use form.** Not raw data — something the receiver can act on (like this cheatsheet versus "go read all of [`rules.md`](../ru/rules.md)"). Do the "last mile" that's cheap for you (context in your head) and expensive for them.
- **3. Concrete values, not just the error type.** Not "file not found" but "file not found: /etc/app/config.yaml".
- **8. Add context.** The receiver only sees the message. Why you're sending it lives in your head until you say so. *(The "this file is for you if…" block at the top is rule 8 in action — without it, you'd have no idea who this cheatsheet is for.)*
- **15. Link text is information, not a placeholder.** Not "[here](../ru/rules.md#правило-15-текст-ссылки--это-информация-а-не-плейсхолдер)" but "[rule 15 in `ru/rules.md`](../ru/rules.md#правило-15-текст-ссылки--это-информация-а-не-плейсхолдер)". Both links point to the same place, but the first one tells the reader nothing until they click.

### Setting a task

- **4. All task parameters.** The executor shouldn't have to guess. If a parameter is unknown — say so explicitly.
- **6. With time to act.** A notification that arrives when action is no longer possible isn't a notification — it's a statement of fact. *(Case: [20 people at a restricted facility gate](../ru/examples/restricted_facility.md) learned about 24-hour passes the moment they arrived.)*
- **7. Ask about obstacles before launching.** One question: "is there anything that might block this?"
- **17. Channel and format are the receiver's call.** Ask: "how do you prefer to receive this — meeting, ticket, voice note?" Don't pick unilaterally.

### Taking the task / receiver's voice

- **5. Don't confirm a task you don't understand.** Clarify *before* "ok", not while doing. Mentally simulate the task end-to-end before agreeing.
- **14. Don't stay silent when you can see something will go wrong.** "Maybe I'm being picky" is more expensive than awkward feedback (predictive).
- **16. Tell the sender if it doesn't work in your environment.** Silent suffering fixes nothing (reactive, after receiving).

### Consumption environment

- **2. Don't make the receiver fetch the information.** Bring it where they are. Not "here's a ticket, take a look."
- **13. Test in the receiver's environment, not yours.** Slides from the back row, images on a phone, documents in print.

### Communication systems (the rules of the game)

- **9. Shared vocabulary at the boundary of responsibilities.** The same word must not mean different things in neighboring teams. *(For example, "done": to the developer — deployed; to QA — passed the checks; to product — in users' hands.)*
- **10. Protocol instead of conversation.** For recurring interactions — fixed states and transitions (like "target identified → engage → shot").
- **11. Format is a contract over time.** Don't change the format silently — the receiver has a pipeline built on it. *(Case: [a sudden switch from CSV to TXT](../ru/examples/format_stability.md) broke someone else's scripts.)*
- **12. Words → structure when unambiguity matters.** Fields, enums, schemas — not "add some info about the source."
- **18. A contract changes explicitly when circumstances change.** Don't cling to a stale contract, but don't retreat from it silently either. External changes (regulation, API, market) count.

---

## 6 limits: when the rules don't apply

1. **Confidentiality.** Sometimes full compliance = a leak (secrets, PII, third-party visibility).
2. **Autonomy and learning.** A ready-made solution deprives the receiver of the path when the path itself is the point of the task.
3. **Honest "I don't know."** Better an explicit gap than fabricated detail. The sender doesn't always know everything either.
4. **Receiver is already in the loop.** Repetition costs more than it helps.
5. **Out of your zone.** Don't transmit, don't clarify, don't signal about what isn't yours.
6. **Cost of compliance > benefit.** Small, one-off, urgent things don't deserve the formal ritual.

---

## Where next

- Full rules and limits — currently in [`../ru/rules.md`](../ru/rules.md) and [`../ru/limits.md`](../ru/limits.md) (translation in progress).
- System view — [`../ru/map.md`](../ru/map.md).
- Live cases that produced these rules — [`../ru/examples/`](../ru/examples/).
