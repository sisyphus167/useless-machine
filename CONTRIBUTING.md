# A letter to future me

*This file is written for the one person who is likely to add another 
piece to this repo — me, later.*

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

Not currently accepted. This is a closed exhibition. If someone opens a 
PR: thank them kindly and close it. Nothing personal — the coherence of 
the portfolio depends on one hand.
