"""Safe imitations of destructive operations.

Pieces in this repo that would otherwise touch real files, remotes, or mailboxes
use this package instead. The imitations are real (they really call os.remove,
really push to a real git repo, really send through a real SMTP server) — they
just target sandboxed resources.
"""
