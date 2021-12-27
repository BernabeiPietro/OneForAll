import os


def cutadapt(mp,md):
     dir_element = filter(lambda x: (".fastq.gz" in x), os.listdir(mp.path_datainput))
     for name_of_file in dir_element:
        input_fq_qz = mp.path_datainput + "/" + name_of_file
        mp.output_fq_qz = mp.path_cutadapt + "/trimmed_" + md["trunc_cuta"] + name_of_file
        os.system("cutadapt -l " + md["trunc_cuta"] + " -m " + md["trunc_cuta"] + " -o " + mp.output_fq_qz + " " + input_fq_qz)
