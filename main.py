from loguru import logger
import typer

def main(test: str):
    print(f"Another {test}")

if __name__ == "__main__":
    typer.run(main)
