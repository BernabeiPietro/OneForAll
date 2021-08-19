import os


def picrust2(mp):
    os.system("picrust2_pipeline.py \
    -s "+mp.path_picrust+"/dna-sequences.fasta \
    -i "+mp.path_picrust+"/feature-table.biom  \
    -o "+mp.path_picrust+"/WDT/ \
    -p 1 \
    --stratified \
    --coverage \
    --per_sequence_contrib \
    --verbose \
    && \
    mv "+mp.path_picrust+"/WDT/* "+mp.path_picrust+" \
    && \
    rm "+mp.path_picrust+"/WDT/ \
              ")




