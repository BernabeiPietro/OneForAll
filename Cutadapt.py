import os


def cutadapt(mp,md):
     dir_element = filter(lambda x: (".fastq.gz" in x), os.listdir(mp.path_fastq_raw))
     for name_of_file in dir_element:
        input_fq_qz = mp.path_fastq_raw + name_of_file
        mp.output_trimmed = mp.path_pathbase + "/trimmed/"  + name_of_file.split("raw")[0]
        os.system("cutadapt -u "+md["Barcode_length"] + mp.output_fq_qz + " " + input_fq_qz)
