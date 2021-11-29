import os
def q_import (mp):
    os.system(
    "qiime tools import \
        --type 'SampleData[PairedEndSequencesWithQuality]' \
        --input-path "+mp.path_datainput+"  \
        --output-path " + mp.seq_qza + " \
        --input-format CasavaOneEightSingleLanePerSampleDirFmt \
        && \
        qiime demux summarize \
        --i-data " + mp.seq_qza + " \
        --o-visualization " +mp.seq_qzv+" \
      ")

#i file devono essere .fastq.gz e non fq.gz bisogna rinominarli
