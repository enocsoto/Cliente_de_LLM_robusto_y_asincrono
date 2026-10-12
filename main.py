"""Ejemplo: una respuesta completa y después el mismo prompt en streaming."""

import asyncio
import logging

from dotenv import load_dotenv

from async_llm_manager import AsyncLLMManager, settings_from_env
from schemas import ChatMessage


async def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    load_dotenv()
    manager = AsyncLLMManager(settings_from_env())
    messages = [ChatMessage(role="user", content="¿Qué es la entropía?")]

    response = await manager.generate(messages)
    if response.error:
        print(response.error)
    else:
        print(response.content)

    async for token in manager.stream(messages):
        print(token, end="", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(main())
