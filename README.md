# useless-machine

*一个 useless Python 代码的概念艺术收藏 / A concept-art collection of useless Python.*

[中文](#中文) · [English](#english)

---

## 中文

> *必须想象西西弗斯是幸福的。* —— 加缪
> *我只是好奇事物是怎么拼到一起的。* —— 香农（大概）

1952 年，马萨诸塞州的一栋房子里，一个刚刚改变了世界的人正在造一只小木盒。这个人是克劳德·香农。四年前，他的论文《通信的数学理论》为之后被称作"数字时代"的整个领域奠定了基石。这只小木盒里什么都没有，只有一个开关和一只装了马达的手。当你把开关拨到 ON，那只手会从盒盖下面伸出来，把开关拨回 OFF，然后缩回去。它的全部功能就是这个。香农管它叫 The Ultimate Machine。

他家里还有半打同类玩意儿。杂耍机器人。一只叫 Theseus 的会走迷宫的电动老鼠。一辆座子不在正中心的独轮车。一把喷火小号。白天他形式化"信号"本身的数学本质，晚上他造的是完全不产生信号的机器。他的同事们困惑不解。他从不解释。

十年前，在被占领的巴黎，加缪出版了《西西弗斯的神话》。西西弗斯——被众神罚去推一块巨石上山，眼看它滚回山脚，再推上去。永远。加缪说，这就是我们的处境。我们的努力并不持久。宇宙不会应答。没有外部的意义等你去找。他说，诚实的回应既不是绝望也不是信仰，而是 *荒谬*——我们清楚地知道石头会滚下来，仍然推；我们清楚地知道造出来的东西什么都做不了，仍然造。那份清醒，不带怨恨地持有，是唯一值得要的胜利。必须想象西西弗斯是幸福的。

香农大概早就想明白了这件事，于是决定：对沉默宇宙的恰当回应，就是造一只自己关掉自己的盒子。

这个仓库是对那个姿态的一次私人致敬。每一件作品都是一台小型香农式机器——它什么都不做，或者把自己做过的事撤销掉，或者为了什么都不做而做了过多的工程。每件都配有一段简短的 manifesto，因为没有注解的概念艺术只是一件家具。这些代码没有用。它们也不教任何东西。它们存在，就像香农那只小盒子存在一样：因为写它们的人，在一个奇怪的宇宙里醒着，所以还是写了。

---

## English

> *One must imagine Sisyphus happy.* — Camus
> *I just wondered how things were put together.* — Shannon (probably)

In a house in Massachusetts in 1952, a man who had just changed the world was building a small wooden box. The man was Claude Shannon. Four years earlier, his paper *A Mathematical Theory of Communication* had founded the field that would become the digital age. The box had nothing inside but a switch and a motorized hand. When you flipped the switch to ON, the hand would reach out from under the lid, flip it back to OFF, and retract. That was all it did. Shannon called it The Ultimate Machine.

He kept half a dozen like it around the house. Juggling robots. A maze-running mouse named Theseus. A unicycle with an off-center seat. A flame-throwing trumpet. By day he formalized the nature of signal itself; by night he built machines that produced none. His colleagues were bewildered. He did not explain himself.

A decade earlier, in occupied Paris, Camus had published *The Myth of Sisyphus*. Sisyphus — condemned by the gods to push a boulder up a hill, watch it roll back, and push it up again. Forever. Camus's point was that this is our condition. Our striving does not last. The universe does not answer. There is no external meaning to find. The honest reply, he wrote, is neither despair nor faith but *the absurd* — we push the boulder fully aware that it will roll back; we build the thing fully aware that it will do nothing. That awareness, held without bitterness, is the only victory worth having. One must imagine Sisyphus happy.

Shannon, I think, had already figured this out, and had decided that the appropriate reply to the silence of the universe was to build a box that turned itself off.

This repository is a personal tribute to that gesture. Each piece is a small machine in the Shannon mould — it does nothing, or undoes itself, or does far too much for no reason. Each comes with a short manifesto, because concept art without a card is only furniture. The pieces are not useful. They do not teach. They exist the way Shannon's little box existed: because the person who wrote them was awake in a strange universe, and wrote them anyway.

---

## Index

| # | Piece | Faction | One-line |
|---|---|---|---|
| 01 | [shannon-switch](pieces/01-shannon-switch/) | Shannon | A class whose `__new__` turns the switch on and off in the same breath. |
| 02 | [hello-antiworld](pieces/02-hello-antiworld/) | Shannon | "Hello, World!" — printed, then erased. |
| 03 | [sisyphus-sort](pieces/03-sisyphus-sort/) | Sisyphus | Bar chart sorted, shuffled, sorted, shuffled. Forever. |
| 04 | [99-percent](pieces/04-99-percent/) | Sisyphus | A progress bar that never reaches 100%. |
| 05 | [enterprise-hello](pieces/05-enterprise-hello/) | Over-engineering | 200 lines of SOLID Python produce exactly `hello`. |
| 06 | [quine-and-vanish](pieces/06-quine-and-vanish/) | Self-reference | A file reads itself out loud and then leaves. |
| 07 | [pypi-useless](pieces/07-pypi-useless/) | Philosophical | A buildable PyPI package whose API is a docstring. |

## Running a piece

```bash
python -m venv .venv && source .venv/bin/activate   # once
pip install -e ".[dev]"                             # once, from the repo root
cd pieces/01-shannon-switch
python main.py
```

Piece 03 is a Jupyter notebook: `jupyter lab pieces/03-sisyphus-sort/sisyphus_sort.ipynb`.

## Safety

Pieces that would produce destructive side effects (self-deletion, pushing to remotes, sending mail) use the `sandbox/` library, which provides real-but-harmless shadow objects — real files in temp directories, real local-bare-repo pushes, real localhost SMTP. No actual files, remotes, or mailboxes are touched.

Currently, only piece 06 uses `sandbox/`.

## License / purpose

Not for utility. For looking at.
不为用，为看。
