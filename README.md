# Cliente de LLM robusto y asíncrono

Cliente unificado para OpenAI o Anthropic. Valida la entrada con Pydantic, responde en un solo bloque o en streaming, y ante un fallo de red o de límite de uso devuelve un error controlado.

## Cómo correrlo

Requiere Python 3.12.

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e .
cp .env.example .env
```

Completa en `.env` la clave del proveedor elegido y ejecuta:

```bash
.venv/bin/python main.py
```

La pregunta fija es «¿Qué es la entropía?». Primero se imprime la respuesta completa. Después se imprimen los tokens a medida que llegan. Si el proveedor falla, el script muestra el error y termina.

## Variables de entorno

| Variable | Uso |
| --- | --- |
| `LLM_PROVIDER` | `openai` (por defecto) o `anthropic` |
| `OPENAI_API_KEY` | Clave de OpenAI. Obligatoria si el proveedor es `openai` |
| `ANTHROPIC_API_KEY` | Clave de Anthropic. Obligatoria si el proveedor es `anthropic` |

Una clave en blanco se trata como ausente. El valor queda en `SecretStr` y no se imprime.

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```
