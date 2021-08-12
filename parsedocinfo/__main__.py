import argparse
import json
import logging
from pathlib import Path
import parse_docinfo

logging.basicConfig(level=logging.INFO)

def _cli() -> any:
    """
    CLI helper.

    Returns:
        a argparse.Namespace object, that looks very much like a NamedTuple
    """

    parser = argparse.ArgumentParser()

    cmd = parser.add_argument_group("General options")
    cmd.add_argument(
        "--input",
        dest="input",
        required=True,
        help="Input file")
    cmd.add_argument(
        "--output",
        dest="outfile",
        required=True,
        help="Output file.")

    return parser.parse_args()


if __name__ == "__main__":
    args = _cli()

    with open(Path(args.input)) as f:
        data = f.read()
        f.close()

    with open(Path(args.outfile),"w") as f:
        logging.info(f"Writing docinfo from {args.input} as JSON to {args.outfile}")
        f.write(json.dumps(parse_docinfo.parse(data)))
        f.close()

