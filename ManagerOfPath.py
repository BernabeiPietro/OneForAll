class ManagerOfPath:
    def __init__(self, path_base, path_datainput, project_name):
        self.path_base = path_base
        self.path_datainput = path_datainput
        self.path_qiime = path_base + "/QIIME2/"
        self.path_cutadapt = path_base + "/CUTADAPT/"
        self.path_figaro = path_base + "/FIGARO/"
        self.path_picrust = path_base + "/PICRUSt2/"
        self.path_fastqc = path_base + "/FASTQC/"
        self.path_tqc_txt = self.path_fastqc+ "/report/"
        self.project_name = project_name
        self.seq_qza = self.path_qiime + "/sample_seq-" + project_name + ".qza"
        self.seq_qzv = self.path_qiime + "/sample_seq-" + project_name + ".qzv"
        self.rep_qza = self.path_qiime + "/rep_seq-" + project_name + ".qza"
        self.ASV_qza = self.path_qiime + "/ASV-" + project_name + ".qza"
        self.DenStat_qza = self.path_qiime + "/denoising_stat-" + project_name + ".qza"
        self.Tax = self.path_qiime + "/taxonomy-" + project_name + ".qza"

