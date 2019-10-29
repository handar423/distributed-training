import json
import argparse

def main():
    """"""
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--log-path", type=str, required=True)
    _parser.add_argument("--output-path", type=str, required=True)
    args = _parser.parse_args()

    with open(args.log_path, 'r') as ifile:
        data = []
        for line in ifile:
            entry = json.loads(line)
            entry['ts'] *= 1e6
            entry['dur'] *=1e6
            data.append(entry)
    
    with open(args.output_path, 'w') as ofile:
        ofile.write(
            '[\n' + \
            ',\n'.join(json.dumps(s) for s in data) + \
            ']\n'
        )

if __name__ == "__main__":
    main()