import pandas as pd
import sys

name=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'EFFECT', 'PUTATIVE_IMPACT', 'GENE_NAME', 'GENE_ID', 'FEATURE_TYPE', 'FEATURE_ID', 'TRANSCRIPT_TYPE', 'EXON_INTRON_RANK', 'HGVSc', 'HGVSp', 'cDNA_POSITION_AND_LENGTH', 'CDS_POSITION_AND_LENGTH', 'PROTEIN_POSITION_AND_LENGTH', 'DISTANCE_TO_FEATURE', 'ERROR']

def info_splitter(tsv_file, output_file):
    ann_table = pd.read_csv(tsv_file, sep='\t', comment='#', names=name)
    split_INFO = ann_table.INFO.str.split(';', expand=True)[[0, 1, 2, 3, 4]]
    ann_table.insert(7, 'DEPTH', split_INFO[0].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(8, 'ALLELE_FREQUENCY', split_INFO[1].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(9, 'STRAND_BIAS', split_INFO[2].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(10, 'DP4', split_INFO[3].apply(lambda x: x[x.find('=')+1:]))
    ann_table.insert(11, 'ANNOTATIONS', split_INFO[4].apply(lambda x: x[x.find('=')+1:]))
    ann_table=ann_table.drop(['INFO'], axis=1)
    ann_table=ann_table.sort_values(by=['QUAL'], ascending=False)
    ann_table.to_excel(output_file, index=False)
    

tsv_file = sys.argv[1]
output_file = sys.argv[2]
info_splitter(tsv_file, output_file)