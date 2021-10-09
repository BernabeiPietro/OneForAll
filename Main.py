import Cutadapt
import Figaro
import PICRUSt2_Tot
import PICRUSt2_rarefied
import QIIME2_body
import QIIME2_import
import QIIME2_tail
import Save_condition
import dim_min_sample_finder
import fastQC
import open_qza_to_PICRUSt2
import trunc_cuta_finder
from ManagerOfPath import ManagerOfPath



if __name__ == '__main__':
    md={}
    #esiste un cond_file? se si usa quello (da scriverlo)
    print("Insert path of reads to reads: path/00.RawData/trimmate_qiime2/")
    path_reads = str(input())
    print("Insert path to write with '/' ")
    path_write = str(input())
    print("nome progetto (no_space):")
    project_name=str(input())
    mp = ManagerOfPath(path_write, path_reads, project_name)

    print("sequenza amplificata?")
    md["seq_ampstr"]=str(input())
    print("N of treads? (max 16)")
    md["tread"] = str(input())
    print("where is metadata")
    md["metadata"] = str(input())
    print("Insert metadata column to group data in weighted unifrac :")
    md["col_met"] = str(input()or "0") #potrebbero essere più di una e per ognuna andrebbe corso il comando: "qiime diversity beta-group-significance" in QIIME2_tail.py
    print("classifier path")
    md["classifier"] = str(input())
    print("amplicon lenght [V4 291,V3-V4 465]")  # da chiedere all'inizio http://omegabioservices.com/index.php/16s-reference/
    md["a_l"] = str(input())
    print("RunPICRUSt2 with rarefied ASV table? Y or N")
    raref_option = str(input())


    Save_condition.save_cond_md(md,mp)
 #   Save_condition.save_cond_mp(mp)

    #inizia da qua il programma

    md["primer_lenght"]=fastQC.run_fastqc(md,mp)
    #genero il file qzv
    QIIME2_import.q_import(mp)
    md["trunc_cuta"] =trunc_cuta_finder.trunc_find(mp)
    Cutadapt.cutadapt(mp, md)
    md["trunc_f"], md["trunc_r"] = Figaro.run_figaro(mp, md)
    QIIME2_body.qiime_body(md, mp)
    md["dim_min_sample"]= dim_min_sample_finder.dim_min_sample(mp,md)
    QIIME2_tail.q_tail(md,mp)
    open_qza_to_PICRUSt2.open_qza_to_picrust_tot(mp)
    PICRUSt2_Tot.picrust2_tot(mp)
    PICRUSt2_Tot.from_ec_to_KO_tot(mp)
    if raref_option=="Y":
        open_qza_to_PICRUSt2.open_qza_to_picrust_rarefied(mp)
        PICRUSt2_rarefied.picrust2_tot(mp)
        PICRUSt2_rarefied.from_ec_to_KO_raref(mp)
    print("Ho finito, felice di servirti!")

