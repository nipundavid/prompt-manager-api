## Install [UV](https://docs.astral.sh/uv/getting-started/installation/)

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Start server

```
uv run fastapi dev
```

## APIs

### Docs

https://{base_url}/prompt-manager/api/v1/docs/

### Get all prompts

https://{base_url}/prompt-manager/api/v1/prompts/

## Port related issues

### Check occupied port

```
lsof -i {port}
```

### Kill process on occupied port

```
kill -9 {PID}
```
