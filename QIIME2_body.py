import os


#metadata
#dim_min_sample
#col_met

def generate_trunk(md,mp):
    trunk=0 #dovrebbe essere "trunc"
    return trunk


def qiime(md, mp):
    # os.system("conda activate qiime2-2021.4")
    os.system("conda activate qiime2-2021.4 \
    && \
    qiime dada2 denoise-paired \
    --i-demultiplexed-seqs " + mp.seq_qza + " \
    --p-trim-left-f " + md["primer_lenght"] + " \
    --p-trim-left-r " + md["primer_lenght"] + " \
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
    --o-visualization " + mp.path_qiime + "/rep_seq-" + mp.project_name + ".qzv \
    && \
    qiime metadata tabulate \
    --m-input-file " + mp.DenStat_qza + " \
    --o-visualization  " + mp.path_qiime + "/denoising_stat-" + mp.project_name + ".qzv \
    && \
    qiime feature-classifier classify-sklearn \
    --i-classifier " + classifier + " \
    --i-reads " + mp.rep_qza + " \
    --o-classification " + mp.Tax + " \
    && \
    qiime metadata tabulate \
    --m-input-file  " + mp.Tax + " \
    --o-visualization " + mp.path_qiime + " /taxonomy-" + mp.project_name + ".qzv \
    && \
    qiime taxa barplot \
    --i-table " + mp.ASV_qza + " \
    --i-taxonomy " + mp.Tax + " \
    --m-metadata-file " +  md["metadata"] + " \
    --o-visualization " + mp.path_qiime + " /barplot-" + mp.project_name + ".qzv  \
    && \
    mkdir " + mp.path_qiime + "/Tree/ \
    && \
    qiime alignment mafft \
    --i-sequences " + mp.rep_qza + " \
    --o-alignment " + mp.path_qiime + "/Tree/aligned_rep_seqs.qza \
    --p-n-threads " + md["tread"] + " \
    && \
    qiime alignment mask \
    --i-alignment " + mp.path_qiime + "/Tree/aligned_rep_seqs.qza \
    --o-masked-alignment " + mp.path_qiime + "/Tree/masked_aligned_rep_seqs.qza \
    && \
    qiime phylogeny fasttree \
    --i-alignment " + mp.path_qiime + "/Tree/masked_aligned_rep_seqs.qza \
    --o-tree " + mp.path_qiime + "/Tree/unrooted_tree.qza \
    --p-n-threads " + md["tread"] + " \
    && \
    qiime phylogeny midpoint-root \
    --i-tree " + mp.path_qiime + "/Tree/unrooted_tree.qza \
    --o-rooted-tree " + mp.path_qiime + "/Tree/rooted_tree.qza \
    ")
    #vai di QIIME2_tail


