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

    # args = init_arg_parser().parse_args()
    #
    # examples = pkl.load(open(args.source_file_name, 'rb'))
    # decodes = pkl.load(open(args.input_file_name, 'rb'))

    examples = pkl.load(open("/home/keyit/code/tranX/data/conala/test.var_str_sep.bin", 'rb'))
    decodes = pkl.load(open("decodes/conala/conala.lstm.hidden256.embed128.action128.field64.type64.dr0.3.lr0.001.lr_de0.5.lr_da15.beam15.vocab.var_str_sep.src_freq3.code_freq3.bin.train.var_str_sep.bin.glorot.par_state.seed0.bin.test.decode", 'rb'))

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

    # with open(args.output_file_name, 'w') as fp:
    #     json.dump(outputs, fp, indent=4)
