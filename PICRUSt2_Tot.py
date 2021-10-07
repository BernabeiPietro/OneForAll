import os


def picrust2_tot(mp):
    os.system("picrust2_pipeline.py \
    -s "+mp.path_qiime+"/dna-sequences.fasta \
    -i "+mp.path_qiime+"/feature-table.biom  \
    -o "+mp.path_picrust+"/TOT/ \
    --stratified \
    --coverage \
    --per_sequence_contrib \
    --verbose \
    ")

def from_ec_to_KO_tot(mp):
    os.system("pathway_pipeline.py \
    -i "+mp.path_picrust+"/TOT/KO_metagenome_out/pred_metagenome_unstrat.tsv.gz \
    -o "+mp.path_picrust+"/TOT/pathway_redo_ko/ \
    --no_regroup \
    --map KEGG_pahways_to_KO2.tsv\
    && \
    pathway_pipeline.py \
    -i "+mp.path_picrust+"/TOT/KO_metagenome_out/pred_metagenome_contrib.tsv.gz \
    -o "+mp.path_picrust+"/TOT/pathway_redo_ko/ \
    --no_regroup \
    --map KEGG_pahways_to_KO2.tsv\
    ")
#/home/lab/anaconda3/envs/picrust2/lib/python3.6/site-packages/picrust2/default_files/pathway_mapfiles/KEGG_pathways_to_KO2.tsv è un file custom che deve andare con il programma.