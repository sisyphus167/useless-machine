# A letter to future me

*This file was first written for me, later — the one person most 
likely to add another piece. Now it's also for you, if you're reading 
this with a piece in mind.*

## A good useless piece has

1. **A clear thesis.** You can say in one sentence what the piece *is*. 
   "A class whose constructor turns it off" is a thesis. "Some over-engineered 
   code" is not.
2. **Faithfulness to the thesis.** No extra features, no escape hatches. 
   If the thesis is "it always fails", it always fails. Don't add a 
   `--succeed` flag.
3. **Autonomy.** It doesn't import from other pieces. `sandbox/` is the 
   only permitted shared code.
4. **Self-reliance.** The README explains the piece to a reader who has 
   not been told anything else.

## A bad useless piece

- **Tries to be useful secretly.** A progress bar that's secretly 
  informative is a real progress bar in a costume. Delete it.
- **Explains its own joke.** No `# lol because it's like Shannon's thing` 
  comments. Let the piece be what it is.
- **Uses mocks or dry-run flags to fake destructiveness.** Use `sandbox/`. 
  The piece should read as if it is really doing the thing.
- **Faction-hops.** Pick one; the piece gets the clarity of its faction 
  in return.

## House rules

- **Number by arrival order.** Never renumber. 03 is the third piece you 
  made, and it stays 03, even if later you think it's weak.
- **Language: one or two, but never mechanical.** A piece can be in one 
  language (whichever carries the voice) or bilingual (中 + en, as the 
  root README and the starter pieces are). What you must not do is 
  translate word-for-word: if you go bilingual, write each version with 
  its own voice. A translation that reads as a translation strips both 
  sides of voice.
- **Commit each piece on its own.** One piece per commit. The history 
  is the exhibition catalog.
- **If a piece needs >1 file, split by what a reader wants to read 
  separately.** Not by technical layer.

## The two temptations

1. **"This is a really clever trick, I should add it."** If it's useful, 
   it probably doesn't belong. Clever ≠ useless.
2. **"This piece is weak, let me delete it."** No. A mixed-quality 
   portfolio is honest. A curated-to-perfection one is a product pitch. 
   Leave it. Write a better one next to it.

## When to expand `sandbox/`

Only when a new piece genuinely needs it. The spec lists `fake_git` and 
`fake_net` as placeholders — add them when the piece that requires them 
is actually being written. Not before.

## External contributions

Welcome. If you have a piece in mind: open a PR. Use the next number in 
arrival order, follow the rules above, and let the manifesto speak in 
whatever voice the piece wants. I'll read it the way I'd read my own — 
carefully, and against one question: *is this useless in the right way?*

---

# 给未来的自己的一封信

*这封信原本是写给以后要再往这个仓库里塞东西的我自己的。现在也写给你——如果你手上有件作品想放进来。*

## 一件好的 useless 作品要有

1. **一个清晰的论点。** 你能用一句话说清楚这件作品**是**什么。"一个构造函数把自己关掉的类"是论点；"一些过度工程的代码"不是。
2. **对论点忠诚。** 没有多余功能，没有退路。如果论点是"它总是失败"，那它就总是失败。不要加 `--succeed` 参数。
3. **自洽。** 不从别的作品 import。`sandbox/` 是唯一被允许的共享代码。
4. **自足。** README 要能向一个完全没有背景的读者把这件作品讲清楚。

## 一件糟糕的 useless 作品

- **偷偷地有用。** 一个其实告诉你真实进度的进度条，只是穿了戏服的真进度条。删掉。
- **解释自己的笑点。** 不要写 `# lol 像香农那个` 之类的注释。让作品自己成为它自己。
- **用 mock 或 dry-run 假装破坏性。** 用 `sandbox/`。作品读起来要像它真的在做那件事。
- **派别摇摆。** 选一派；作品因此获得那一派独有的清晰感。

## 约定

- **按到达顺序编号。** 不重新编号。03 就是你做的第三件，哪怕你后来觉得它写得不好。
- **语言：一种或两种，但不做机械翻译。** 一件作品可以单语（哪种能把 manifesto 撑起来就用哪种），也可以中英双语（像根 README 和启动集那样）。**不能做的**是字对字翻译——如果要双语，每一份都要自己说话。翻译腔的双语让两边都失掉声音。
- **每件作品独立一个 commit。** 一件一个。git 历史就是展览的目录。
- **如果一件作品需要多个文件，按"读者想分开看什么"来拆分。** 不按技术分层拆。

## 两种诱惑

1. **"这招挺巧的，我加进来吧。"** 如果它有用，就多半不该进来。巧 ≠ 无用。
2. **"这件太弱了，删了吧。"** 不。水平参差不齐的作品集是诚实的；精修到完美的作品集是产品宣传。留着。在它旁边再写一件更好的。

## 何时扩展 `sandbox/`

只有当一件新作品真正需要的时候。spec 里写了 `fake_git` 和 `fake_net` 作为预留——等到真正要写那件需要它们的作品时再加。不提前加。

## 外部贡献

欢迎。如果你手上有一件作品：开一个 PR，用下一个可用的编号，让 manifesto 用它自己想要的声音说话。照上面的规则来。我会用读自己作品的方式读它——仔细地读，对着一个问题：*它在正确的意义上无用吗？*
