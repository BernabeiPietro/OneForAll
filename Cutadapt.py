import os


def cutadapt(mp,trunc):
     dir_element = filter(lambda x: (".fastq.gz" in x), os.listdir(mp.path_datainput))
     for name_of_file in dir_element:
        input_fq_qz = mp.path_datainput + "/" + name_of_file
        mp.output_fq_qz = mp.path_cutadapt + "/trimmed_" + trunc + name_of_file
        os.system("cutadapt -l " + trunc + " -m " + trunc + " -o " + mp.output_fq_qz + " " + input_fq_qz)
