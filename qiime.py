import os




def generate_trunk(md,mp):
    trunk=0
    return trunk


def qiime(md, mp):
    # os.system("conda activate qiime2-2021.4")
    os.system("conda activate qiime2-2021.4 \
    && \
    qiime tools import \
    --type 'SampleData[PairedEndSequencesWithQuality]' \
    --input-path " + mp.path_datainput + " \
    --output-path " + mp.seq_qza + " \
    --input-format CasavaOneEightSingleLanePerSampleDirFmt \
    && \
    qiime demux summarize \
    --i-data " + mp.seq_qza + " \
    --o-visualization " + mp.path_qiime + "/sample_seq-" + mp.project_name + ".qzv \
    && \
    qiime dada2 denoise-paired \
    --i-demultiplexed-seqs " + mp.seq_qza + " \
    --p-trim-left-f " + primer_left + " \
    --p-trim-left-r " + primer_right + " \
    --p-trunc-len-f " + md["trunc_f"] + " \
    --p-trunc-len-r " + md["trunc_r"] + " \
    --o-representative-sequences " + mp.rep_qza + " \
    --o-table " + mp.ASV_qza + " \
    --o-denoising-stats " + mp.DenStat_qza + " \
    --p-n-threads " + md["tread"] + " \
    && \
    qiime feature-table summarize \
    --i-table " + mp.ASV_qza + " \
    --o-visualization " + mp.path_qiime + "/ASV-" + mp.project_name + ".qzv \
    --m-sample-metadata-file " + md["metadata"] + " \
    && \
    qiime feature-table tabulate-seqs \
    --i-data " + mp.rep_qza + " \
    --o-visualization " + path_write + "/rep_seq-" + mp.project_name + ".qzv \
    && \
    qiime metadata tabulate \
    --m-input-file " + DenStat_qza + " \
    --o-visualization  " + path_write + "/denoising_stat-" + project_name + ".qzv \
    && \
    qiime feature-classifier classify-sklearn \
    --i-classifier " + classifier + " \
    --i-reads " + rep_qza + " \
    --o-classification " + Tax + " \
    && \
    qiime metadata " + tabulate + " \
    --m-input-file  " + Tax + " \
    --o-visualization " + path_write + " /taxonomy-" + project_name + ".qzv \
    && \
    qiime taxa barplot \
    --i-table " + ASV_qza + " \
    --i-taxonomy " + Tax + " \
    --m-metadata-file " + metadata + " \
    --o-visualization " + path_write + " /barplot-" + project_name + ".qzv  \
    && \
    mkdir " + path_write + "/Tree/ \
    && \
    qiime alignment mafft \
    --i-sequences " + rep_qza + " \
    --o-alignment " + path_write + "/Tree/aligned_rep_seqs.qza \
    --p-n-threads " + tread + " \
    && \
    qiime alignment mask \
    --i-alignment " + path_write + "/Tree/aligned_rep_seqs.qza \
    --o-masked-alignment " + path_write + "/Tree/masked_aligned_rep_seqs.qza \
    && \
    qiime phylogeny fasttree \
    --i-alignment " + path_write + "/Tree/masked_aligned_rep_seqs.qza \
    --o-tree " + path_write + "/Tree/unrooted_tree.qza \
    --p-n-threads " + tread + " \
    && \
    qiime phylogeny midpoint-root \
    --i-tree " + path_write + "/Tree/unrooted_tree.qza \
    --o-rooted-tree " + path_write + "/Tree/rooted_tree.qza \
    &&" \
        ####dim_min_sample = booooooo \
    "mkdir " + path_write + "/Rarefaction/" \
    "qiime diversity alpha-rarefaction \
    --i-table " + ASV_qza + " \
    --i-phylogeny " + path_write + "/Tree/rooted_tree.qza \
    --p-max-depth " + dim_min_sample + " \
    --m-metadata-file " + metadata + " \
    --p-metrics shannon \
    --p-metrics faith_pd \
    --p-metrics observed_features \
    --p-metrics gini_index \
    --p-metrics fisher_alpha \
    --p-metrics pielou_e \
    --p-metrics simpson_e \
    --p-metrics simpson \
    --p-metrics chao1 \
    --o-visualization " + path_write + "/Rarefaction/alpha_rarefaction.qzv \
    && \
    qiime diversity core-metrics-phylogenetic \
    --i-phylogeny " + path_write + "/Tree/rooted_tree.qza \
    --i-table " + ASV_qza + " \
    --p-sampling-depth " + dim_min_sample + " \
    --m-metadata-file " + metadata + " \
    --p-n-jobs-or-threads auto \
    --output-dir " + path_write + "/core_metrics_results \
    --verbose \
    && \
    qiime diversity alpha-group-significance \
    --i-alpha-diversity " + path_write + "/core_metrics_results/evenness_vector.qza \
    --m-metadata-file " + metadata + " \
    --o-visualization " + path_write + "/core_metrics_results/evenness_group_significance.qzv \
    --verbose \
    && \
    qiime diversity alpha-group-significance \
    --i-alpha-diversity " + path_write + "/core_metrics_results/shannon_vector.qza \
    --m-metadata-file " + metadata + " \
    --o-visualization " + path_write + "/core_metrics_results/shannon_group_significance.qzv \
    --verbose \
    && \
    qiime diversity alpha-group-significance \
    --i-alpha-diversity " + path_write + "/core_metrics_results/observed_features_vector.qza \
    --m-metadata-file " + metadata + " \
    --o-visualization " + path_write + "/core_metrics_results/observed_features_group_significance.qzv \
    --verbose" \
                  # vanno fatte variabili apposta per le colonne dei metadata
                                       "qiime diversity beta-group-significance \
    --i-distance-matrix " + path_write + "/core_metrics_results/weighted_unifrac_distance_matrix.qza \
    --m-metadata-file " + metadata + " \
    --m-metadata-column " + col_met + " \
    --o-visualization " + path_write + "/core_metrics_results/weighted_unifrac_" + col_met + "_significance.qzv \
    --p-permutations 9999 \
    ")

    #       dir_element = filter(lambda x: (".fastq.gz" in x), os.listdir(path))
    # for name_of_file in dir_element:
    #    input_fq_qz = path + "/" + name_of_file
    #   output_fq_qz = path_write + "/trimmed_" + name_of_file
    #  os.system("cutadapt -l " + trunc + " -m " + trunc + " -o " + output_fq_qz + " " + input_fq_qz)
