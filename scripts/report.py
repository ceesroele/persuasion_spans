"""Create comparison reports on generated metrics for evaluating persuasion span
model evaluations."""
import json
import re
import pandas as pd
import typer
from typing import Optional
from pathlib import Path
from spacy.cli._util import Arg, Opt


def create_report(
    paths_input: Path = Opt('metrics', "--paths_input", "-pi", help="Input directory with metrics JSONs", dir_okay=True),
    paths_output: Path = Opt(None, "--paths_output", "-po", help="Output directory for reports", dir_okay=True),
    spans_key: str = Opt("sc", "--spans-key", help="spancat spans_key"),
):
    """Create CSV file with reported metrics for different models trained for persuasion spans"""
    print("Creating report", paths_input, paths_output)
    files = ['config_sm', 'config_lg', 'config_trf']
    prefix = f'spans_{spans_key}'
    for ngrams in ['16', '32']:
        per_label = {}
        totals = {'precision': [], 'recall': [], 'f1': []}
        headers = []
        for fname in files:
            r = re.compile('.*_([a-z]+)')
            m = r.match(fname)
            headers.append(m.group(1))
            with open(paths_input / f'{fname}_{ngrams}.json', 'r') as f:
                obj = json.load(f)

                # Totals
                totals['precision'].append(obj[f'{prefix}_p'])
                totals['recall'].append(obj[f'{prefix}_r'])
                totals['f1'].append(obj[f'{prefix}_f'])

                # Per type
                d = obj[f'{prefix}_per_type']
                for k, v in d.items():
                    if k not in per_label.keys():
                        per_label[k] = []
                    per_label[k].append(v['f'])

        totals_df = pd.DataFrame(totals, index=headers)
        per_label_df = pd.DataFrame(per_label, index=headers).T

        print(totals_df)
        print(per_label_df)

        if paths_output is None:
            paths_output = paths_input
        totals_df.to_csv(paths_output / f'totals_{ngrams}.csv')
        per_label_df.to_csv(paths_output / f'per_label_{ngrams}.csv')


if __name__ == '__main__':
    typer.run(create_report)
