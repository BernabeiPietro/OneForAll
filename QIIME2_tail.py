import os
def q_tail(md,mp):
    os.system(" \
         mkdir " + mp.path_qiime + "/Rarefaction/ \
        qiime diversity alpha-rarefaction \
        --i-table " + mp.ASV_qza + " \
        --i-phylogeny " + mp.path_qiime + "/Tree/rooted_tree.qza \
        --p-max-depth " + md["dim_min_sample"] + " \
        --m-metadata-file " + md["metadata"] + " \
        --p-metrics shannon \
        --p-metrics faith_pd \
        --p-metrics observed_features \
        --p-metrics gini_index \
        --p-metrics fisher_alpha \
        --p-metrics pielou_e \
        --p-metrics simpson_e \
        --p-metrics simpson \
        --p-metrics chao1 \
        --o-visualization " + mp.path_qiime + "/Rarefaction/alpha_rarefaction.qzv \
        && \
        qiime diversity core-metrics-phylogenetic \
        --i-phylogeny " + mp.path_qiime + "/Tree/rooted_tree.qza \
        --i-table " + mp.ASV_qza + " \
        --p-sampling-depth " + md["dim_min_sample"] + " \
        --m-metadata-file " + md["metadata"] + " \
        --p-n-jobs-or-threads auto \
        --output-dir " + mp.path_qiime + "/core_metrics_results \
        --verbose \
        && \
        qiime diversity alpha-group-significance \
        --i-alpha-diversity " + mp.path_qiime + "/core_metrics_results/evenness_vector.qza \
        --m-metadata-file " +  md["metadata"] + " \
        --o-visualization " + mp.path_qiime + "/core_metrics_results/evenness_group_significance.qzv \
        --verbose \
        && \
        qiime diversity alpha-group-significance \
        --i-alpha-diversity " + mp.path_qiime + "/core_metrics_results/shannon_vector.qza \
        --m-metadata-file " +  md["metadata"] + " \
        --o-visualization " + mp.path_qiime + "/core_metrics_results/shannon_group_significance.qzv \
        --verbose \
        && \
        qiime diversity alpha-group-significance \
        --i-alpha-diversity " + mp.path_qiime + "/core_metrics_results/observed_features_vector.qza \
        --m-metadata-file " +  md["metadata"] + " \
        --o-visualization " + mp.path_qiime + "/core_metrics_results/observed_features_group_significance.qzv \
        --verbose \
     ")
    if md["col_met"]!=0:
        os.system(" \
            qiime diversity beta-group-significance \
            --i-distance-matrix " + mp.path_qiime + "/core_metrics_results/weighted_unifrac_distance_matrix.qza \
            --m-metadata-file " +  md["metadata"] + " \
            --m-metadata-column " + md["col_met"] + " \
            --o-visualization " + mp.path_qiime + "/core_metrics_results/weighted_unifrac_" + md["col_met"] + "_significance.qzv \
            --p-permutations 9999 \
        ")
    # vanno fatte variabili apposta per le colonne dei metadata