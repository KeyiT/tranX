import pickle as pkl
import argparse
import json
from datasets.conala.conala_eval import tokenize_for_bleu_eval

def init_arg_parser():
    arg_parser = argparse.ArgumentParser()

    #### General configuration ####
    arg_parser.add_argument('-s', "--source_file_name", type=str, help='Model Input File Path.')
    arg_parser.add_argument('-i', "--input_file_name", type=str, help='Input File Path.')
    arg_parser.add_argument('-o', "--output_file_name", type=str, help='Output File Path.')

    return arg_parser


if __name__ == '__main__':

    args = init_arg_parser().parse_args()

    examples = pkl.load(open(args.source_file_name, 'rb'))
    decodes = pkl.load(open(args.input_file_name, 'rb'))

    for example in examples:
        setattr(example, 'reference_code_tokens', tokenize_for_bleu_eval(example.meta['example_dict']['snippet']))

    outputs = list()

    hypotheses = [hyp_list[0].decanonical_code_tokens if hyp_list else [] for hyp_list in decodes]
    src_sents = [e.src_sent for e in examples]
    references = [e.reference_code_tokens for e in examples]

    for hyp, sent, ref in zip(hypotheses, src_sents, references):
        outputs.append(
            {"prediction": hyp, "sentence": sent, "reference": ref}
        )

    with open(args.output_file_name, 'w') as fp:
        json.dump(outputs, fp, indent=4)
