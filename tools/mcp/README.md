# MCP server — chile-compliance

Exposes the corpus to **any MCP-speaking client**: ChatGPT connectors, Claude Desktop,
Cursor, Continue, and others. One server, one policy, every host.

## Why MCP rather than uploading files

The corpus is built for *verifiable citations*. The decision tree in
`corpus/_agent-policy.md` depends on two things a document-upload workflow cannot give
you: retrieving an **exact** citation in full, and **traversing** the cross-reference
graph from a law article into the CMF regulation that implements it.

Semantic retrieval over uploaded knowledge files returns plausible-looking fragments.
It answers many questions acceptably and then, without signalling it, misses the
law → NCG bridge that turns "what does the law say?" into "what must we actually file,
build, and report?" This server does exact retrieval, so the citation an answer rests on
is the citation you can click through and verify.

The server also passes the full text of `corpus/_agent-policy.md` to the client as its
MCP `instructions`, so a connecting model inherits the behavioural policy — including
the effective-date discipline — without a second copy being maintained anywhere.

## Install

```bash
git clone https://github.com/fjaviergallucci/chilean-compliance.git
cd chilean-compliance
python -m pip install -r tools/mcp/requirements.txt   # Python 3.11+
```

Verify it starts:

```bash
python -m tools.mcp.server        # serves MCP over stdio; Ctrl-C to stop
```

## Tools

Each maps to one operation in `corpus/_agent-policy.md`.

| Tool | Operation | Arguments |
|---|---|---|
| `search_topics` | LOCATE | `query` |
| `get_article` | RETRIEVE | `citation`, `include_spanish=false` |
| `get_definition` | DEFINE | `term` |
| `get_scenario` | SCENARIO | `query` (feature description or scenario number) |
| `get_cross_references` | TRAVERSE | `citation` |
| `get_spanish_original` | ORIGINAL | `citation` |
| `get_corpus_status` | STATUS | — |

**Citation grammar:** `19.628 Art. 8 bis`, `Ley 21.521 Art. 3(2)`, `NCG 502 §IV.C.3.1`,
`NCG 530 §II.A`. Ordinal spacing is forgiving — `Art. 8bis` and `Art. 8 bis` both work.

English is the default surface; Spanish is returned only when asked for, via
`include_spanish` or `get_spanish_original`. Unresolvable input comes back as a
structured `error` field rather than a transport failure, so a model can correct the
citation and retry.

## Client configuration

Replace `/abs/path/to/chilean-compliance` with your clone's absolute path. On Windows
use the full `python.exe` path or `py`.

### Claude Desktop

`claude_desktop_config.json` (Settings → Developer → Edit Config):

```json
{
  "mcpServers": {
    "chile-compliance": {
      "command": "python",
      "args": ["-m", "tools.mcp.server"],
      "cwd": "/abs/path/to/chilean-compliance"
    }
  }
}
```

### Claude Code

```bash
claude mcp add chile-compliance --cwd /abs/path/to/chilean-compliance -- python -m tools.mcp.server
```

Note that Claude Code users generally want the **plugin** instead — it needs no server
process. See the repository README. The MCP server is for other hosts.

### ChatGPT

Connectors are configured in ChatGPT's settings under Connectors / Developer mode;
availability depends on your plan, and a stdio server must run somewhere the client can
reach. For a purely local setup, point the connector at the same command above. To share
the corpus with a team, run the server behind an HTTP transport instead:

```bash
python -c "from tools.mcp.server import build_server; build_server().run(transport='streamable-http')"
```

and expose that endpoint to your ChatGPT workspace.

### Cursor

`.cursor/mcp.json` in the project, or the global equivalent:

```json
{
  "mcpServers": {
    "chile-compliance": {
      "command": "python",
      "args": ["-m", "tools.mcp.server"],
      "cwd": "/abs/path/to/chilean-compliance"
    }
  }
}
```

## Architecture

```
corpus/_agent-policy.md      policy — what the agent must do (host-neutral)
        |
        +-- skills/.../SKILL.md    binding: Claude Code tools
        +-- tools/mcp/server.py    binding: MCP tools  --> tools/corpus_api.py
                                                             |
                                                   corpus/ + indexes/
```

`tools/corpus_api.py` does the resolving and is pure stdlib — it parses the indexes into
memory on first use, with no database. `server.py` is a thin adapter over it. Behaviour
changes belong in the policy file, not in either binding.

## Not legal advice

This corpus is a structured citation aid, not legal advice. For decisions carrying
material risk, consult Chilean counsel.
