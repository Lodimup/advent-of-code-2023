def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns a list of lines.
    Args:
        file_path (str): Path to the input file.
    Returns:
        list[str]: List of lines.
    """
    with open(file_path, "r") as f:
        data = f.read()

        return data.split("\n")