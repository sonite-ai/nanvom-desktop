# Desktop Sandbox Python Example

This is a basic example of how to use the Desktop Sandbox Python SDK with streaming and moving mouse around.

## How to run

### 1. Create `.env` file

```bash
cp .env.example .env
```

### 2. Set `NANOVM_API_KEY` in `.env` file

Get your API key at [app.nanovm.dev/dashboard](https://app.nanovm.dev/dashboard).

```bash
NANOVM_API_KEY="your_api_key"
```

### 3. Install dependencies

```bash
poetry install
```

### 4. Run

```bash
poetry run python main.py
```

