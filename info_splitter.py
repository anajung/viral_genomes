import pandas as pd
import sys

name='CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tEFFECT\tPUTATIVE_IMPACT\tGENE_NAME\tGENE_ID\tFEATURE_TYPE\tFEATURE_ID\tTRANSCRIPT_TYPE\tEXON_INTRON_RANK\tHGVSc\tHGVSp\tcDNA_POSITION_AND_LENGTH\tCDS_POSITION_AND_LENGTH\tPROTEIN_POSITION_AND_LENGTH\tDISTANCE_TO_FEATURE\tERROR'.split('\t')

def info_splitter(tsv_file, output_file):
    ann_table = pd.read_csv(tsv_file, sep='\t', comment='#', names=name)
    split_INFO = ann_table.INFO.str.split(';', expand=True)[[0, 1, 2, 3, 4]]
    ann_table.insert(7, 'DEPTH', split_INFO[0].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(8, 'ALLELE_FREQUENCY', split_INFO[1].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(9, 'STRAND_BIAS', split_INFO[2].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(10, 'DP4', split_INFO[3].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(11, 'ANNOTATIONS', split_INFO[4].apply(lambda x: x[x.find('=')+1:]))
    ann_table=ann_table.drop(['INFO'], axis=1)
    ann_table.to_excel(output_file)

tsv_file = sys.argv[1]
output_file = sys.argv[2]
info_splitter(tsv_file, output_file)