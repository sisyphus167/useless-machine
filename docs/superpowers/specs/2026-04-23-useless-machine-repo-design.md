# Useless Machine: Design Spec

*A curated collection of Python code inspired by Shannon's Ultimate Machine — concept-art pieces whose only purpose is to undo themselves, spin in place, over-engineer nothing, or refer only to themselves.*

---

## 1. 定位 (Positioning)

**这是什么**：一个个人作品集式的代码仓库。每件"作品"是一段 Python 代码 + 一篇 manifesto（散文式注解），共同构成一件概念艺术。

**这不是什么**：
- 不是 `awesome-xxx` 清单（不做社区众包、不收 PR 灌水）
- 不是教程（不做"为什么它无用"的教学化分析）
- 不是玩具库（作品之间不构成 API、不互相依赖、除 `sandbox/` 外没有公共抽象）

**灵感来源**：Claude Shannon 的 Ultimate Machine — 拨动开关后，机器唯一的功能是伸出一只手把开关拨回去。

## 2. 风格范围

作品可以落在任何一派，不追求派别平衡，但启动集覆盖所有派别：

- **香农原教旨派**：代码唯一的功能是撤销自己
- **西西弗斯派**：永无止境地完成又撤销，永远在原地
- **过度工程派**：用荒谬复杂的方式做极简的事
- **自指/哥德尔派**：代码关于代码本身
- **哲学/混合类**：以上皆有或以上皆非

## 3. 仓库结构

```
useless-machine/
├── README.md                    # 总宣言：为什么，引用香农，定调
├── pieces/
│   ├── 01-shannon-switch/
│   │   ├── README.md           # manifesto + 运行说明 + 预期现象
│   │   ├── main.py
│   │   └── demo.gif            # 可选
│   ├── 02-hello-antiworld/
│   ├── 03-sisyphus-sort/
│   │   └── sisyphus_sort.ipynb # 视作品而定用 notebook
│   └── ...
├── sandbox/                     # 共享的"安全破坏"工具库
│   ├── __init__.py
│   ├── fake_fs.py              # 影子文件系统
│   ├── fake_git.py             # 本地 bare repo
│   └── fake_net.py             # 假下载 / 假 HTTP
├── CONTRIBUTING.md             # 写给未来的自己：什么算"好"的 useless code
└── pyproject.toml              # pip install -e . 以便 import sandbox
```

### 3.1 命名与编号

- 每件作品一个目录，前缀 `NN-kebab-case-name`
- `NN` 是**收录顺序**，不是质量排名
- 永不重新编号：哪怕后来觉得 03 很烂，它仍然是 03。这种诚实本身是作品集的一部分。

### 3.2 分类

**没有分类目录**。分类交给根 `README.md` 的一张索引表（"按派别浏览"的表格）。
理由：目录分类会让读者用标签模式浏览；作品集应该被逐件看，派别只是事后归档。

### 3.3 每件作品的解剖

每件作品是一个目录，包含：

| 文件 | 必选？ | 作用 |
|---|---|---|
| `README.md` | 必选 | 标题、1–2 段 manifesto、运行说明、"你会看到什么" |
| `main.py` | 常见 | 作品主体代码 |
| `*.ipynb` | 备选 | 如果可视化/叙事更适合 notebook，就用这个替代 `main.py` |
| `demo.gif` / `demo.mp4` | 可选 | 某些作品（清屏、进度条、动画）必须录屏才传达得出效果 |
| 其他 `.py` | 按需 | 某些作品需要多文件（比如"互相 import 的两个模块"） |

## 4. 语言策略

**每篇作品自己决定用中文还是英文**。不强制统一。

理由：这是艺术项目不是文档项目。有些点子（谐音、典故）在中文里才好笑；有些（Shannon 式冷幽默）在英文里才有节奏。强行双语会牺牲声音。

## 5. 破坏性代码策略：沙盒

### 5.1 规则

- 所有会产生副作用的作品（自删、推送、发邮件、改文件）**必须**通过 `sandbox/` 提供的工具接触"外部世界"
- `sandbox/` 提供的是**真实可执行的影子对象**：真实存在的临时文件、真实的本地 bare git repo、真实的 localhost SMTP server
- 作品代码应当看起来就像在真的干那件事，读者看源码时看到的是干净的 `me.delete()` 而不是 `if not dry_run: ...`
- README 顶部一行声明：`This piece uses sandbox.fake_fs — no real files are harmed.`

### 5.2 为什么不用 mock / patch / dry-run flag

因为这些方案会把"假"写进作品本体，作品就带了开关、带了分支、带了"演出感"。沙盒模式让作品本身保持单纯和真诚——它**真的**执行了 `os.remove`，只是这个文件在一个临时目录里。

### 5.3 sandbox/ 初始模块

- `fake_fs.ShadowFile(path)`：返回一个真实存在于临时目录的文件副本，其上的 `delete()` / `write()` / `exists()` 都是真调用
- `fake_git`：返回一个本地 bare repo 的 clone，可以真 `push`、真 `revert`，不接触任何 remote
- `fake_net`：返回一个 localhost HTTP server 或 `/dev/urandom`-backed 的"假下载"

启动集只需要 `fake_fs`；`fake_git` 和 `fake_net` 按作品需要再加。

## 6. 启动集：01 – 07

以下 7 件作品构成仓库首次公开时的阵容，顺序即编号。

### 01 shannon-switch
**派别**：香农原教旨派
**一句话**：`with UselessMachine() as m: ...` — 进入的瞬间 `__exit__` 就被调用。
**为什么放 01**：开宗明义，对香农的直接致敬。作品集的定锚。

### 02 hello-antiworld
**派别**：香农原教旨派
**一句话**：打印 `Hello, World!`，然后用 `\r` + 空格把它擦掉。屏幕最终干净。
**演示**：必须配 `demo.gif`（看一闪而过的 Hello）。

### 03 sisyphus-sort
**派别**：西西弗斯派
**一句话**：排好序 → 打乱 → 排好序 → 打乱，无限循环。
**形式**：`sisyphus_sort.ipynb`。用 notebook 做动画可视化，验证"hybrid 结构（方案 D）是合理的"这一决定。

### 04 99-percent
**派别**：西西弗斯派
**一句话**：进度条爬到 99% 停住，偶尔抖一下；ETA 显示 "about 3 seconds remaining"，这个数字永远在 3 秒左右。
**演示**：必须配 `demo.gif`。

### 05 enterprise-hello
**派别**：过度工程派
**一句话**：用 `AbstractGreeterFactory`、`DependencyInjectionContainer`、策略模式、事件总线、~300 行干净 OOP，打印 `hello`。
**附加**：一张 UML 类图（`architecture.svg`）放在目录里。

### 06 quine-and-vanish
**派别**：自指/哥德尔派（+ 香农原教旨派）
**一句话**：打印自己的源码，然后 `os.remove(__file__)`。
**沙盒**：使用 `sandbox.fake_fs.ShadowFile`。这是展示沙盒惯例的最佳样板。

### 07 pypi-useless
**目录**：`pieces/07-pypi-useless/`
**派别**：哲学/混合类
**一句话**：真的发一个 PyPI 包 `useless`。`pip install useless` 成功，`import useless` 成功，什么都不发生。
**附加**：目录包含 PyPI 包的源（`setup.py` / `pyproject.toml` / `useless/__init__.py`），README 说明"已发布到 PyPI"并附链接。这是整个启动集的收尾——把无用真的推向世界。
**注意**：发布到 PyPI 是仓库外的一次性动作，不属于实现计划的默认步骤；作品内包含完整的可发布包结构即可。

### 启动集的自洽性

| 作品 | 派别 | 形式 | 沙盒 | 演示 |
|---|---|---|---|---|
| 01 | 香农 | 目录 + main.py | — | — |
| 02 | 香农 | 目录 + main.py | — | GIF |
| 03 | 西西弗斯 | 目录 + notebook | — | notebook 内嵌 |
| 04 | 西西弗斯 | 目录 + main.py | — | GIF |
| 05 | 过度工程 | 目录 + 多 py + UML | — | — |
| 06 | 自指 | 目录 + main.py | ✔ | — |
| 07 | 哲学 | 目录 + 完整 PyPI 包 | — | — |

覆盖了所有派别、混合制的两种形式（目录+py vs. notebook）、沙盒惯例的样板展示、以及一件"真的推到世界上"的收尾作品。

## 7. 将来的点子库（不承诺实现）

作为种子记录，方便日后回看：

- **@regret** 装饰器：函数返回后立刻撤销所有副作用（沙盒）
- **email-to-self-and-delete**：发邮件给自己再 IMAP 删除
- **unread**：把所有已读邮件标回未读
- **tidy-chaos** 守护进程：监控目录，任何变化都被还原
- **async-print**：asyncio + coroutines + queue 实现 `print("x")`
- **microservice-of-42**：Flask + k8s + Grafana 只为返回 `42`
- **type-safe-nothing**：泛型 / `Protocol` / `Generic` 包出一个 `pass`
- **self-importing**：`from self_importing import self_importing`
- **one-line-per-run**：每次运行删掉自己最后一行（沙盒副本）
- **revert-bot**：GitHub Action，每次 commit 自动开 PR revert，包括自己
- **test-for-this-test**：pytest 文件，唯一测试是"验证自己被 pytest 跑了"
- **do-nothing-daemon**：systemd 服务，0% CPU / `signal.pause()`，附 Helm chart 与 100% SLA 文档
- **halting-prompt**：`Do you want me to stop? [y/n]` — 按什么都退出，包括 Ctrl+C

## 8. 非目标 (Non-Goals)

- 不做测试框架、不做 CI（除非某件作品本身需要，比如 revert-bot 或 test-for-this-test）
- 不追求代码复用（除 `sandbox/` 外）。重复是可接受的，每件作品自成一体
- 不做国际化（语言每篇各自选）
- 不追求版本发布节奏。仓库是作品集，不是软件产品
- 不接受外部贡献（至少首版如此）。CONTRIBUTING.md 是写给未来的自己的便签，不是公开邀请
