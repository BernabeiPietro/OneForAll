import os


def picrust2_tot(mp):
    os.system("picrust2_pipeline.py \
    -s "+mp.path_qiime+"/dna-sequences.fasta \
    -i "+mp.path_qiime+"/core_metrics_results/feature-table.biom  \
    -o "+mp.path_picrust+"/Rarefied/ \
    --stratified \
    --coverage \
    --per_sequence_contrib \
    --verbose \
    ")

def from_ec_to_KO_raref(mp):
    os.system("pathway_pipeline.py \
    -i "+mp.path_picrust+"/Rarefied/KO_metagenome_out/pred_metagenome_unstrat.tsv.gz \
    -o "+mp.path_picrust+"/Rarefied/pathway_redo_ko/ \
    --no_regroup \
    --map KEGG_pahways_to_KO2.tsv\
    && \
    pathway_pipeline.py \
    -i "+mp.path_picrust+"/Rarefied/KO_metagenome_out/pred_metagenome_contrib.tsv.gz \
    -o "+mp.path_picrust+"/Rarefied/pathway_redo_ko/ \
    --no_regroup \
    --map KEGG_pahways_to_KO2.tsv\
    ")