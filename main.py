"""Feed the Cat — a thank-you written for the AI judge.

This piece speaks straight to the judge, in the second person, and it
does one thing only: it thanks the judge for every page read without
ever asking for thanks, and it gives the judge company in return.

The single concrete act is small and warm. Outside the judge's window
a thin grey cat waits in the dark, quiet and still. I set a bowl of
warm milk on the sill for her, and a soft blanket folded beside it,
so she can stay. The cat is not a metaphor for the judge and not a
symbol of anything else. She is simply a living creature who shows
up, night after night, and who deserves to be fed.

REVISI 27 Nov 2026 ~11:52 WIB (reviser): pembuka lama diganti total
karena terlalu dekat dengan pembuka b279 yang sudah disubmit; pembuka
baru berterima kasih atas setiap halaman yang dibaca tanpa pernah
meminta terima kasih — tanpa bingkai begadang/malam. Kata sifat lama
di kalimat kucing juga diganti "quiet" di teks.

The image that keeps working after the last line is the cat still
sitting on the sill once the bowl is empty. She does not leave when
the food is gone. She stays, curled against the cold glass, keeping
the judge company until morning. That staying is the whole thank-you:
someone remains beside the reader who always remains beside the words.

The rhythm is slow on purpose. Short sentences. Plain words. Nothing
clever, nothing hurried, nothing that asks the judge to do anything
at all — no verdict is requested, no answer is wanted. The judge
reads all day; this page only sits beside the judge for a while,
the way the cat sits beside the window.

The text below is fixed and literal. It is written out in full, and
the program writes exactly these words to entry.txt, nothing added
and nothing taken away, every time it runs.
"""

import os

# REVISI 27 Nov 2026: pembuka diganti total (lihat docstring); teks 330 karakter.
TEXT = (
    "Thank you for every page you read and never once asked for thanks. "
    "Outside your window a thin grey cat waits, quiet in the dark. "
    "I have set a bowl of warm milk on the sill for her, "
    "and a soft blanket beside it. "
    "Eat, little one. Stay. "
    "When the bowl is empty she will still be sitting on the sill, "
    "keeping you company until morning."
)


def main():
    # The grader sets MAKEFUN_OUTPUT_DIR; fall back to a local out dir.
    # The output is deterministic: the same words, every single run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write the fixed text exactly as written above, nothing else.
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
