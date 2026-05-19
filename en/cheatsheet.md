# Cheatsheet

> This file is for you if you have 2 minutes — and want to see everything on one page.

The book is about delivering information so it doesn't need to be asked twice. Below — all rules and limits in one list.

---

## 18 rules

### Quality of a single message

1. **Ready-to-use form.** Not raw data — something the receiver can act on. Do the work that's cheap for you and expensive for them.
2. **Don't make the receiver fetch the information.** Bring it where they are. Not "here's a link."
3. **Concrete values, not just the error type.** Not "file not found" but "file not found: /etc/app/config.yaml".
4. **All task parameters present.** The executor shouldn't have to guess. If a parameter is unknown — say so explicitly.
5. **Don't confirm a task you don't understand.** Clarify *before* "ok", not while doing.
6. **With time to act.** A notification that arrives when action is no longer possible is not a notification — it's a statement of fact.
7. **Ask about obstacles before launching.** One question: "is there anything that might block this?"
8. **Add context.** The receiver only sees the message. The "why" is in your head until you say it.

### Communication systems

9. **Shared vocabulary at the boundary of responsibilities.** The same word must not mean different things on both sides.
10. **Protocol instead of conversation.** For recurring interactions — fixed states and transitions, not freeform talk.
11. **Format is a contract over time.** Don't change the format silently — the receiver has a pipeline built on it.
12. **Words → structure, when unambiguity matters.** Fields, enums, schemas — not "add some info about the source."

### Environment and carriers

13. **Test in the receiver's environment, not yours.** Slides from the back row, images on a phone, documents in print.
14. **Don't stay silent when you can see a rule is being broken.** "Maybe I'm being picky" is more expensive than awkward feedback.
15. **Link text is information, not a placeholder.** Not "here", but "the paper *Attention is all you need*".
16. **If it doesn't work in your environment — tell the sender.** Silent suffering fixes nothing.

### Negotiations

17. **The channel and format are the receiver's call, not the sender's.** Don't pick unilaterally. Ask: "how do you prefer to receive this?"
18. **A contract changes explicitly when circumstances change.** Don't cling to a stale contract, but also don't retreat from it silently.

---

## 6 limits: when the rules don't apply

1. **Confidentiality.** Sometimes full compliance = a leak.
2. **Autonomy and learning.** "Ready" deprives the receiver of the path, when the path is the point of the task.
3. **Honest "I don't know."** Better an explicit gap than fabricated detail.
4. **Receiver already knows.** Repetition costs more than it helps.
5. **Out of your zone.** Don't transmit, don't clarify, don't signal about what isn't yours.
6. **Cost of compliance > benefit.** Small, one-off, urgent things don't deserve the ritual.

---

## Where next

- Full rules and limits — currently in [`../ru/rules.md`](../ru/rules.md) and [`../ru/limits.md`](../ru/limits.md) (translation in progress).
- System view — [`../ru/map.md`](../ru/map.md).
- Live cases that produced these rules — [`../ru/examples/`](../ru/examples/).
