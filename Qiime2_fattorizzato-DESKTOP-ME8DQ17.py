


cartella=

qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path /home/giacomobernabei/Documenti/Paper_vino/After_figaro/Manifest_file_campioni2.csv \
  --output-path /home/giacomobernabei/Documenti/Paper_vino/After_figaro/Campioni/seq_campioni_paper_vino.qza \
  --input-format PairedEndFastqManifestPhred33V2 \