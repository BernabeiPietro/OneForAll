import os

os.system(
"qiime tools import \
    --type 'SampleData[PairedEndSequencesWithQuality]' \
    --input-path " + mp.path_datainput + " \
    --output-path " + mp.seq_qza + " \
    --input-format CasavaOneEightSingleLanePerSampleDirFmt \
    && \
    qiime demux summarize \
    --i-data " + mp.seq_qza + " \
    --o-visualization " +mp.seq_qzv+" \
  ")


