import os


def cutadapt(mp, trunc_cuta):
     dir_element = filter(lambda x: (".fastq.gz" in x), os.listdir(mp.path_datainput))
     for name_of_file in dir_element:
        input_fq_qz = mp.path_datainput + "/" + name_of_file
        mp.output_fq_qz = mp.path_cutadapt + "/trimmed_" + trunc_cuta + name_of_file
        os.system("cutadapt -l " + trunc_cuta + " -m " + trunc_cuta + " -o " + mp.output_fq_qz + " " + input_fq_qz)
