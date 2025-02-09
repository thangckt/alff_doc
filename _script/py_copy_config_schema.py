import requests


def read_schema_text(yaml_schema_file: str) -> str:
    """Read text from a file."""
    with open(yaml_schema_file, "r") as f:
        text = f.read()
    text = "\n```yaml\n" + text + "\n```\n"
    return text

def append_schema_text(yaml_schema_file: str, text_file: str):
    """Append text to a file."""
    schema_text = read_schema_text(yaml_schema_file)
    with open(text_file, "a") as f:
        f.write(schema_text)
    return







##### ANCHOR: udpate the blog posts
def main():
    ### Post 1
    append_schema_text(yaml_schema_file="./alff/util/script/ase_script/schema_ARG_ASE.yaml", text_file="./_docs/schema/ase_config.md")


    return


if __name__ == "__main__":
    main()
