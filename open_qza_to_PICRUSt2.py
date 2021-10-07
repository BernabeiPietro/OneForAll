import os


def open_qza_to_picrust_tot(mp):
    os.system("7z e "+mp.ASV_qza+" *.biom -r")
    os.system("7z e "+mp.rep_qza+" *.fasta -r")


def open_qza_to_picrust_rarefied(mp):
    os.system("7z e " + mp.path_qiime + "/core_metrics_results/rarefied_table.qza *.biom -r")



