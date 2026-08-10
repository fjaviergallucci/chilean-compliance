"""MCP binding over the Chilean compliance corpus.

The server is a thin adapter: it exposes the seven operations defined in
``corpus/_agent-policy.md`` as MCP tools and delegates every one of them to
``tools.corpus_api``. Policy lives in the corpus, not here.
"""
