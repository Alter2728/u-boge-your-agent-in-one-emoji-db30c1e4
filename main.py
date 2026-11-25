import os

# Octopus: many arms working in parallel, each sensing and acting on its own
# while one mind coordinates them — like subagents and tools run at once.
EMOJI = "🐙"


def main():
    assert len(EMOJI) == 1
    assert len(EMOJI.strip()) == 1
    assert "\n" not in EMOJI
    assert "\r" not in EMOJI

    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    data = EMOJI.encode("utf-8")

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(data)

    with open(output_path, "rb") as f:
        readback = f.read()

    assert readback == data
    assert not readback.endswith(b"\n")
    assert len(readback.decode("utf-8").strip()) == 1


if __name__ == "__main__":
    main()
